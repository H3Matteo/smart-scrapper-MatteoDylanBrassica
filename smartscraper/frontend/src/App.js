import React, { useEffect, useState } from "react";
import { Filters } from "./components/Filters";
import { CardGrid } from "./components/CardGrid";

export default function App() {
  const [data, setData] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [ville, setVille] = useState("");
  const [nom, setNom] = useState("");
  const [theme, setTheme] = useState("");
  const [themes, setThemes] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/data")
      .then((res) => res.json())
      .then((result) => {
        setData(result);
        setFiltered(result);
        const allThemes = result.flatMap(m => m.theme ? m.theme.split(",") : []);
        const uniqueThemes = [...new Set(allThemes.map(t => t.trim()))];
        setThemes(uniqueThemes);
      });
  }, []);

  useEffect(() => {
    if (ville !== "") {
      fetch(`http://localhost:5000/api/data/${ville}`)
        .then((res) => res.json())
        .then((res) => setFiltered(res));
    } else if (nom !== "") {
      fetch(`http://localhost:5000/api/data/nom/${nom}`)
        .then((res) => res.json())
        .then((res) => setFiltered(res));
    } else {
      setFiltered(data);
    }
  }, [ville, nom, data]);

  useEffect(() => {
    if (theme === "") {
      setFiltered(data);
      return;
    }

    const filteredByTheme = data.filter((item) => {
      return item.theme && item.theme.toLowerCase().includes(theme.toLowerCase());
    });

    setFiltered(filteredByTheme);
  }, [theme, data]);

  const handleScrape = () => {
    fetch("http://localhost:5000/api/scrape", { method: "POST" })
      .then((res) => res.json())
      .then((res) => alert(res.message))
      .catch((err) => console.error("Erreur scraping:", err));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 font-sans">
      <header className="mb-6 text-center">
        <h1 className="text-3xl font-bold text-gray-800">SmartScraper</h1>
        <p className="text-gray-600">Données OpenData automatisées et filtrables</p>
        <button onClick={handleScrape} className="mt-4 px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Re-scraper les données
        </button>
      </header>

      <Filters setVille={setVille} setNom={setNom} setTheme={setTheme} themes={themes} />

      <div className="card">
        <CardGrid data={filtered} />
      </div>
    </div>
  );
}
