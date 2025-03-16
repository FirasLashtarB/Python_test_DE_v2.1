import json
from collections import defaultdict


def load_output(file_path="tests/output.json"):
    """Charge le fichier JSON généré par la data pipeline."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def most_referenced_journal(data):
    """Trouve le journal qui mentionne le plus de médicaments différents."""
    journal_counts = defaultdict(set)
    for entry in data:
        journal_counts[entry["journal"].lower()].add(entry["drug"].lower())
    max_journal = max(journal_counts, key=lambda k: len(journal_counts[k]))
    return max_journal, len(journal_counts[max_journal])


def related_meds_for_drug(data, drug_name):
    """Trouve les médicaments mentionnés dans les mêmes journaux que le médicament donné (PubMed uniquement)."""
    journal_to_drugs = defaultdict(set)

    for entry in data:
        if entry["source"] == "PubMed":
            journal_to_drugs[entry["journal"].lower()].add(entry["drug"].lower())

    related_meds = set()
    for journal, drugs in journal_to_drugs.items():
        if drug_name.lower() in drugs:
            related_meds.update(drugs)

    related_meds.discard(drug_name.lower())  # Supprimer le médicament lui-même
    return list(related_meds)


if __name__ == "__main__":
    data = load_output()
    top_journal, count = most_referenced_journal(data)
    print(f"Journal qui mentionne le plus de médicaments : {top_journal} ({count} médicaments différents)")

    test_drug = "Diphenhydramine"
    related_meds = related_meds_for_drug(data, test_drug)
    print(f"Médicaments mentionnés avec {test_drug} dans PubMed : {related_meds}")