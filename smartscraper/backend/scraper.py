import pandas as pd
import json
import re
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CSV_URL = "https://www.data.gouv.fr/fr/datasets/r/5ccd6238-4fb0-4b2c-b14a-581909489320"
OUTPUT_JSON = "musees_data.json"
DB_URL = "sqlite:///musees.db"

Base = declarative_base()

class Musee(Base):
    __tablename__ = "musees"
    id = Column(String, primary_key=True)
    nom = Column(String)
    ville = Column(String)
    departement = Column(String)
    region = Column(String)
    theme = Column(String)
    annee = Column(Integer, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

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

    # Persistance en base
    print("[INFO] Insertion en base SQLite...")
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for r in records:
        annee = None
        if pd.notna(r["annee"]):
            match = re.search(r"\d{4}", str(r["annee"]))
            if match:
                annee = int(match.group())

        musee = Musee(
            id=r["id"],
            nom=r["nom"],
            ville=r["ville"],
            departement=r["departement"],
            region=r["region"],
            theme=r["theme"],
            annee=annee,
            latitude=float(r["Latitude"]) if pd.notna(r["Latitude"]) else None,
            longitude=float(r["Longitude"]) if pd.notna(r["Longitude"]) else None
        )
        session.merge(musee)

    session.commit()
    print("[✅] Insertion terminée dans la base SQLite")

if __name__ == "__main__":
    download_and_clean()