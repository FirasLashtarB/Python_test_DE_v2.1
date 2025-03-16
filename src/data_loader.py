import pandas as pd
import json
from pathlib import Path

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def load_data():
    base_path = Path(__file__).resolve().parent.parent / "data"
    return {
        "drugs": load_csv(base_path / "drugs.csv"),
        "pubmed_csv": load_csv(base_path / "pubmed.csv"),
        "pubmed_json": load_json(base_path / "pubmed.json"),
        "clinical_trials": load_csv(base_path / "clinical_trials.csv")
    }