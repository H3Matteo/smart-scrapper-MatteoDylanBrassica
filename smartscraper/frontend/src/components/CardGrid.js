export function CardGrid({ data }) {
  if (data.length === 0) {
    return <p className="text-center text-gray-600">Aucune donnée trouvée.</p>;
  }

  return (
    <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
      {data.map((item, i) => (
        <div key={i} className="bg-white shadow-md rounded-lg p-4">
          <h2 className="text-xl font-semibold text-blue-700 mb-2">{item.nom}</h2>
          <p className="text-gray-700 text-sm mb-1"><strong>Adresse:</strong> {item.adresse}</p>
          <p className="text-gray-700 text-sm mb-1"><strong>Ville:</strong> {item.ville}</p>
          {item.site_web && (
            <a
              href={item.site_web}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block mt-2 text-sm text-blue-500 underline"
            >
              Voir le site
            </a>
          )}
        </div>
      ))}
    </div>
  );
}
