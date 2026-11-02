#!/usr/bin/env python3
"""Comprueba los IDs documentados y genera un reporte de trazabilidad."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def first_column_ids(path, prefix):
    ids = []
    for line in read(path).splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.startswith("|") and re.fullmatch(prefix, cells[0]):
            ids.append(cells[0])
    return ids


def refs(value, prefix):
    return set(re.findall(r"\b" + prefix + r"\b", value))


def main():
    sources = {
        "REQ": first_column_ids("docs/SRS.md", r"REQ-\d{3}"),
        "CU": first_column_ids("docs/CU.md", r"CU-\d{3}"),
        "CLS": re.findall(r'<mxCell id="(CLS-[A-Za-z]+)"', read("modelos/clases.drawio")),
        "PRU": first_column_ids("pruebas/pruebas.md", r"PRU-\d{3}"),
    }
    rows = []
    for line in read("matrices/trazabilidad.md").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"REQ-\d{3}", cells[0]):
            rows.append((cells[0], refs(cells[2], r"CU-\d{3}"),
                         refs(cells[3], r"CLS-[A-Za-z]+"), refs(cells[4], r"PRU-\d{3}")))

    errors = []
    matrix_reqs = [row[0] for row in rows]
    if len(matrix_reqs) != len(set(matrix_reqs)):
        errors.append("Hay requisitos repetidos en la matriz.")
    for kind, ids in sources.items():
        if len(ids) != len(set(ids)):
            errors.append(f"Hay IDs {kind} repetidos en el artefacto de origen.")
    missing = set(sources["REQ"]) - set(matrix_reqs)
    extra = set(matrix_reqs) - set(sources["REQ"])
    if missing:
        errors.append("Requisitos sin fila: " + ", ".join(sorted(missing)))
    if extra:
        errors.append("Requisitos sin SRS: " + ", ".join(sorted(extra)))

    for i, kind in enumerate(("CU", "CLS", "PRU"), start=1):
        linked = set().union(*(row[i] for row in rows)) if rows else set()
        unknown = linked - set(sources[kind])
        unlinked = set(sources[kind]) - linked
        if unknown:
            errors.append(f"{kind} sin artefacto: " + ", ".join(sorted(unknown)))
        if unlinked:
            errors.append(f"{kind} sin requisito en matriz: " + ", ".join(sorted(unlinked)))
    for req, cus, classes, tests in rows:
        if not (cus and classes and tests):
            errors.append(f"{req} carece de CU, CLS o PRU en su fila.")

    covered = sum(bool(cus and classes and tests
                       and cus <= set(sources["CU"])
                       and classes <= set(sources["CLS"])
                       and tests <= set(sources["PRU"]))
                  for _, cus, classes, tests in rows)
    total = len(sources["REQ"])
    lines = [
        "# Reporte de trazabilidad (sesión 12)", "",
        "Generado con `python3 scripts/verificar-trazabilidad.py` a partir de los artefactos del repositorio.", "",
        f"Requisitos con CU, CLS y PRU: **{covered}/{total}**.",
        f"IDs de origen: {total} REQ, {len(sources['CU'])} CU, {len(sources['CLS'])} CLS y {len(sources['PRU'])} PRU.",
        "", "| Requisito | Casos de uso | Clases | Pruebas |", "|---|---|---|---|",
    ]
    for req, cus, classes, tests in rows:
        lines.append("| " + " | ".join((req, ", ".join(sorted(cus)),
                                       ", ".join(sorted(classes)), ", ".join(sorted(tests)))) + " |")
    lines += ["", "## Comprobación bidireccional", ""]
    lines += ["Sin vínculos de ID faltantes o sobrantes." if not errors else "Inconsistencias encontradas:"]
    lines += [f"- {error}" for error in errors]
    lines += ["", "La cobertura mide relaciones entre documentos. Las pruebas están documentadas; este reporte no acredita su ejecución.", ""]
    output = ROOT / "reportes/trazabilidad-s12.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"{output.relative_to(ROOT)}: {covered}/{total} requisitos vinculados, {len(errors)} inconsistencias")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
