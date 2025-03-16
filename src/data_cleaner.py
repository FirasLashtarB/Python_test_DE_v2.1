import pandas as pd

def clean_pubmed(df):
    """Nettoie et transforme les données PubMed."""
    df = df.dropna(subset=["id", "title", "date", "journal"])  # Supprime les lignes avec valeurs manquantes
    df = df[df["id"].astype(str).str.isnumeric()]  # Garde uniquement les IDs numériques
    df["id"] = df["id"].astype(int)  # Convertit en int après nettoyage
    return df

def clean_clinical_trials(df):
    """Nettoie les données Clinical Trials."""
    df = df.dropna()
    return df

def clean_data(data):
    """Nettoie toutes les sources de données."""
    data["pubmed_csv"] = clean_pubmed(data["pubmed_csv"])
    data["pubmed_json"] = clean_pubmed(data["pubmed_json"])
    data["clinical_trials"] = clean_clinical_trials(data["clinical_trials"])
    return data
