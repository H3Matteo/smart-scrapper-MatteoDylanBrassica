export function Filters({ setVille }) {
  return (
    <div className="mb-6 flex flex-col sm:flex-row gap-4 justify-center">
      <input
        type="text"
        placeholder="Filtrer par ville"
        onChange={(e) => setVille(e.target.value)}
        className="px-4 py-2 rounded border border-gray-300 shadow-sm w-full sm:w-80"
      />
    </div>
  );
}
