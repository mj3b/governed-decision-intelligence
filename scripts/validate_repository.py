#!/usr/bin/env python3
"""Run the repository reproducibility checks from one entry point."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Callable

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def run_command(command: list[str], cwd: Path | None = None) -> None:
    print(f"$ {' '.join(command)}")
    completed = subprocess.run(command, cwd=cwd or ROOT, check=False)
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed with exit code {completed.returncode}: {' '.join(command)}"
        )


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_yaml(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def assert_invalid(validator: Draft202012Validator, instance: object, label: str) -> None:
    if not list(validator.iter_errors(instance)):
        raise AssertionError(f"negative fixture unexpectedly validated: {label}")


def validate_schema() -> None:
    json_schema = load_json(ROOT / "schema" / "gdr.schema.json")
    yaml_schema = load_yaml(ROOT / "schema" / "gdr.schema.yaml")
    example = load_json(ROOT / "schema" / "gdr.example.json")

    Draft202012Validator.check_schema(json_schema)
    Draft202012Validator.check_schema(yaml_schema)
    checker = FormatChecker()
    json_validator = Draft202012Validator(json_schema, format_checker=checker)
    yaml_validator = Draft202012Validator(yaml_schema, format_checker=checker)

    json_errors = sorted(json_validator.iter_errors(example), key=lambda e: list(e.path))
    yaml_errors = sorted(yaml_validator.iter_errors(example), key=lambda e: list(e.path))
    if json_errors:
        raise AssertionError(f"JSON schema rejected example: {json_errors[0].message}")
    if yaml_errors:
        raise AssertionError(f"YAML schema rejected example: {yaml_errors[0].message}")

    if set(json_schema.get("required", [])) != set(yaml_schema.get("required", [])):
        raise AssertionError("JSON and YAML schemas define different top-level required fields")
    if set(json_schema.get("properties", {})) != set(yaml_schema.get("properties", {})):
        raise AssertionError("JSON and YAML schemas define different top-level properties")

    unknown = deepcopy(example)
    unknown["unexpected_research_field"] = True
    assert_invalid(json_validator, unknown, "unknown top-level field")

    missing = deepcopy(example)
    missing.pop("decision_question", None)
    assert_invalid(json_validator, missing, "missing decision_question")

    conditional = deepcopy(example)
    conditional["decision_outcome"]["outcome"] = "conditional_go"
    conditional["decision_outcome"]["conditions"] = []
    assert_invalid(json_validator, conditional, "conditional go without conditions")

    gate_four = deepcopy(example)
    gate_four["gate_classification"]["gate"] = "gate_4_hard_escalation"
    gate_four["gate_classification"]["escalation_required"] = False
    assert_invalid(json_validator, gate_four, "Gate 4 without escalation")

    print("schema validation: PASS")


def validate_gate_classifier() -> None:
    run_command(
        [sys.executable, "test_gate_classifier.py"],
        cwd=ROOT / "reference-implementation" / "gate-classifier",
    )
    print("gate classifier: PASS")


def validate_interop() -> None:
    run_command(
        [sys.executable, "test_driver.py"],
        cwd=ROOT / "examples" / "testvectors-interop",
    )
    print("interoperability fixtures: PASS")


def validate_citation() -> None:
    run_command(["cffconvert", "--validate"])
    print("citation metadata: PASS")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=("all", "schema", "gate", "interop", "citation"),
        default="all",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checks: dict[str, Callable[[], None]] = {
        "schema": validate_schema,
        "gate": validate_gate_classifier,
        "interop": validate_interop,
        "citation": validate_citation,
    }
    selected = checks.items() if args.only == "all" else [(args.only, checks[args.only])]

    try:
        for name, check in selected:
            print(f"\n== {name} ==")
            check()
    except (AssertionError, RuntimeError, OSError, ValueError) as exc:
        print(f"repository validation: FAIL\n{exc}", file=sys.stderr)
        return 1

    print("\nrepository validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
