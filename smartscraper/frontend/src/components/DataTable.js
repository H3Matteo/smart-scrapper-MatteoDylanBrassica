export function DataTable({ data }) {
  if (data.length === 0) {
    return <p>Aucune donnée trouvée.</p>;
  }

  return (
    <table className="w-full border-collapse">
      <thead>
        <tr className="bg-gray-100">
          <th className="border px-2 py-1 text-left">Nom</th>
          <th className="border px-2 py-1 text-left">Adresse</th>
          <th className="border px-2 py-1 text-left">Ville</th>
          <th className="border px-2 py-1 text-left">Site web</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, i) => (
          <tr key={i} className="hover:bg-gray-50">
            <td className="border px-2 py-1">{item.nom}</td>
            <td className="border px-2 py-1">{item.adresse}</td>
            <td className="border px-2 py-1">{item.ville}</td>
            <td className="border px-2 py-1">
              {item.site_web ? (
                <a
                  href={item.site_web}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 underline"
                >
                  Lien
                </a>
              ) : (
                "N/A"
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
