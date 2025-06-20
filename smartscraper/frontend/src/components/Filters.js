export function Filters({ setVille, setNom, setTheme, themes }) {
  return (
    <div className="mb-6 flex flex-col sm:flex-row sm:space-x-[15px] space-y-3 sm:space-y-0 items-center justify-center">
      <input
        type="text"
        placeholder="Filtrer par ville"
        onChange={(e) => setVille(e.target.value)}
        className="px-4 py-2 rounded border border-gray-300 shadow-sm w-full sm:w-80"
      />
      <input
        type="text"
        placeholder="Filtrer par nom"
        onChange={(e) => setNom(e.target.value)}
        className="px-4 py-2 rounded border border-gray-300 shadow-sm w-full sm:w-80"
      />
      <input
        list="theme-options"
        placeholder="Filtrer par thème"
        onChange={(e) => setTheme(e.target.value)}
        className="px-4 py-2 rounded border border-gray-300 shadow-sm w-full sm:w-80"
      />
      <datalist id="theme-options">
        {themes.map((t, index) => (
          <option key={index} value={t} />
        ))}
      </datalist>
    </div>
  );
}
