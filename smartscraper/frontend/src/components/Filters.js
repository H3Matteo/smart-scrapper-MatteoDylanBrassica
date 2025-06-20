import React from "react";

export function Filters({ setVille, setNom, setTheme, data }) {
  const uniqueThemes = Array.isArray(data)
    ? Array.from(
        new Set(
          data.flatMap((item) =>
            item.theme ? item.theme.split(",").map((t) => t.trim()) : []
          )
        )
      ).sort()
    : [];

  return (
    <div className="flex flex-wrap gap-4 justify-center mb-6">
      <input
        type="text"
        placeholder="Filtrer par ville"
        onChange={(e) => setVille(e.target.value)}
        className="p-2 border rounded w-60"
      />

      <input
        type="text"
        placeholder="Filtrer par nom"
        onChange={(e) => setNom(e.target.value)}
        className="p-2 border rounded w-60"
      />

      <input
        list="theme-options"
        placeholder="Filtrer par thème"
        onChange={(e) => setTheme(e.target.value)}
        className="p-2 border rounded w-60"
      />

      <datalist id="theme-options">
        {uniqueThemes.map((t, i) => (
          <option key={i} value={t} />
        ))}
      </datalist>
    </div>
  );
}
