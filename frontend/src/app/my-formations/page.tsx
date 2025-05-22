'use client';
import { useEffect, useState } from 'react';
import { apiFetch } from '../../utils/api';

interface Formation {
  id: number;
  theme: string;
  description?: string;
}

export default function MyFormationsPage() {
  const [formations, setFormations] = useState<Formation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    // On suppose un endpoint /auth/me pour récupérer l'utilisateur et ses formations
    apiFetch('/auth/me')
      .then(user => setFormations(user.formations || []))
      .catch(() => setError('Erreur lors du chargement'))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="text-center mt-16">Chargement...</div>;
  if (error) return <div className="text-center mt-16 text-red-500">{error}</div>;

  return (
    <div className="max-w-3xl mx-auto mt-8">
      <h1 className="text-2xl font-bold mb-6">Mes formations</h1>
      {formations.length === 0 ? (
        <div className="text-gray-500">Aucune formation inscrite.</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {formations.map(f => (
            <div key={f.id} className="bg-white rounded shadow p-4 flex flex-col">
              <div className="font-semibold text-blue-700 mb-1">{f.theme}</div>
              <div className="text-gray-600 mb-2">{f.description}</div>
              <div className="text-xs text-gray-400 mb-2">Supports : Vidéo, PDF (simulés)</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
