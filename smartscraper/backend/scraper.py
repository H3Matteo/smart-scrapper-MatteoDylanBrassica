import pandas as pd
import json

CSV_URL = "https://www.data.gouv.fr/fr/datasets/r/5ccd6238-4fb0-4b2c-b14a-581909489320"
OUTPUT_JSON = "musees_data.json"

def download_and_clean():
    print("[INFO] Téléchargement des données des musées...")
    df = pd.read_csv(CSV_URL, sep=";")

    # Sélection des colonnes utiles
    keep_columns = [
        "Identifiant", "Nom_officiel", "Ville", "Departement",
        "Région", "Domaine_thematique", "Annee_creation", "Coordonnees"
    ]
    df = df[keep_columns].dropna(subset=["Identifiant", "Nom_officiel"])

    # Séparation latitude / longitude (corrigée)
    coords = df["Coordonnees"].str.extract(r"^\s*([^,]+)\s*,\s*([^,]+)\s*$")
    df["Latitude"] = coords[0]
    df["Longitude"] = coords[1]

    df = df.rename(columns={
        "Identifiant": "id",
        "Nom_officiel": "nom",
        "Ville": "ville",
        "Departement": "departement",
        "Région": "region",
        "Domaine_thematique": "theme",
        "Annee_creation": "annee"
    })
    df = df.drop(columns=["Coordonnees"])

    print(f"[OK] {len(df)} musées traités")

    # Export JSON
    records = df.to_dict(orient="records")
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"[✅] Données sauvegardées dans {OUTPUT_JSON}")

if __name__ == "__main__":
    download_and_clean()
