import unittest
import json
import os
from scraper import download_and_clean

class TestScraper(unittest.TestCase):

    def setUp(self):
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

if __name__ == "__main__":
    unittest.main()
