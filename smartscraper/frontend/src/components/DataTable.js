export function DataTable({ data }) {
  if (data.length === 0) {
    return <p>Aucune donnée trouvée.</p>;
  }

  return (
    <table className="w-full border-collapse">
      <thead>
        <tr className="bg-gray-100">
          <th className="border px-2 py-1 text-left">Nom</th>
          <th className="border px-2 py-1 text-left">Ville</th>
          <th className="border px-2 py-1 text-left">Département</th>
          <th className="border px-2 py-1 text-left">Région</th>
          <th className="border px-2 py-1 text-left">Thème</th>
          <th className="border px-2 py-1 text-left">Année</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, i) => (
          <tr key={i} className="hover:bg-gray-50">
            <td className="border px-2 py-1">{item.nom}</td>
            <td className="border px-2 py-1">{item.ville}</td>
            <td className="border px-2 py-1">{item.departement}</td>
            <td className="border px-2 py-1">{item.region}</td>
            <td className="border px-2 py-1">{item.theme}</td>
            <td className="border px-2 py-1">{item.annee || "Inconnue"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
