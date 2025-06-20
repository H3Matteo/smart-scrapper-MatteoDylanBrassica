import unittest
<<<<<<< HEAD
import pandas as pd
from scraper import download_and_clean, OUTPUT_JSON
import json
import os
=======
import json
import os
from scraper import download_and_clean
>>>>>>> ccc64942fc03a09cb58851ceda49ee38a56ff19d

class TestScraper(unittest.TestCase):

    def setUp(self):
<<<<<<< HEAD
        # Exécute le scraping une fois pour tester les données générées
        download_and_clean()

        # Charge le JSON généré
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_json_exists(self):
        """Le fichier JSON a bien été créé"""
        self.assertTrue(os.path.exists(OUTPUT_JSON))

    def test_data_not_empty(self):
        """Les données ne sont pas vides"""
        self.assertGreater(len(self.data), 0)

    def test_required_fields_exist(self):
        """Chaque musée possède les champs requis"""
        required_fields = {"id", "nom", "ville", "departement", "region", "theme", "annee", "Latitude", "Longitude"}
        for musee in self.data:
            self.assertTrue(required_fields.issubset(musee.keys()))

    def test_annee_format(self):
        """L’année doit être un entier ou None"""
        for musee in self.data:
            self.assertTrue(isinstance(musee["annee"], int) or musee["annee"] is None)

    def test_coordinates_format(self):
        """Latitude et longitude doivent être des floats ou None"""
        for musee in self.data:
            lat = musee["Latitude"]
            lon = musee["Longitude"]
            if lat is not None:
                self.assertIsInstance(lat, float)
            if lon is not None:
                self.assertIsInstance(lon, float)
=======
        # Exécuter le scraping pour être à jour
        download_and_clean()
        with open("musees_data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_json_not_empty(self):
        self.assertTrue(len(self.data) > 0, "Le fichier JSON est vide")

    def test_required_fields(self):
        required = {"id", "nom", "ville", "departement", "region", "theme", "annee", "Latitude", "Longitude"}
        for musee in self.data:
            self.assertTrue(required.issubset(musee.keys()), f"Champs manquants dans : {musee}")

    def test_coordinates_format(self):
        for musee in self.data:
            lat = musee["Latitude"]
            lon = musee["Longitude"]
            self.assertTrue(isinstance(lat, float) or lat is None, f"Latitude invalide : {lat}")
            self.assertTrue(isinstance(lon, float) or lon is None, f"Longitude invalide : {lon}")

    def test_annee_format(self):
        for musee in self.data:
            annee = musee["annee"]
            self.assertTrue(
                isinstance(annee, (int, float)) or annee is None,
                f"L'année n'est pas au bon format : {annee}"
            )

    def test_id_format(self):
        for musee in self.data:
            self.assertTrue(
                musee["id"].startswith("M") or musee["id"].startswith("B"),
                f"Identifiant incorrect : {musee['id']}"
            )
>>>>>>> ccc64942fc03a09cb58851ceda49ee38a56ff19d

if __name__ == "__main__":
    unittest.main()
