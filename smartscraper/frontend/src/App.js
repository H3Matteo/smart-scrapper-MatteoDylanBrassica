import React, { useEffect, useState } from "react";
import { Filters } from "./components/Filters";
import { CardGrid } from "./components/CardGrid";

export default function App() {
  const [data, setData] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [ville, setVille] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/data")
      .then((res) => res.json())
      .then((result) => {
        setData(result);
        setFiltered(result);
      });
  }, []);

  useEffect(() => {
    if (ville === "") {
      setFiltered(data);
      return;
    }

    fetch(`http://localhost:5000/api/data/${ville}`)
      .then((res) => res.json())
      .then((res) => setFiltered(res));
  }, [ville]);

  const handleScrape = () => {
    fetch("http://localhost:5000/api/scrape", { method: "POST" })
      .then((res) => res.json())
      .then((res) => alert(res.message))
      .catch((err) => console.error(err));
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

      <Filters setVille={setVille} />

      <div className="card">
        <CardGrid data={filtered} />
      </div>
    </div>
  );
}
