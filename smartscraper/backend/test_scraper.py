import unittest
import pandas as pd
from scraper import download_and_clean, OUTPUT_JSON
import json
import os

class TestScraper(unittest.TestCase):

    def setUp(self):
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

if __name__ == "__main__":
    unittest.main()
