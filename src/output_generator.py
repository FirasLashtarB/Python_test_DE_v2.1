import json
from pathlib import Path


def save_output(data, output_path=None):
    if output_path is None:
        output_path = Path(__file__).resolve().parent.parent / "tests" / "output.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


