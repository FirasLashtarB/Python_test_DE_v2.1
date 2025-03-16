def process_data(data):
    relations = []
    for _, row in data["pubmed_csv"].iterrows():
        relations.append({
            "drug": row["title"],
            "journal": row["journal"],
            "date": row["date"],
            "source": "PubMed"
        })
    return relations