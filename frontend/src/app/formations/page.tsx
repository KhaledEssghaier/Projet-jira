'use client';
import { useEffect, useState } from 'react';

interface Formation {
  id: number;
  theme: string;
  description?: string;
}

function getFavorites(): Formation[] {
  if (typeof window === 'undefined') return [];
  const fav = localStorage.getItem('favorites');
  return fav ? JSON.parse(fav) : [];
}

function addFavorite(formation: Formation) {
  const favs = getFavorites();
  if (!favs.find(f => f.id === formation.id)) {
    favs.push(formation);
    localStorage.setItem('favorites', JSON.stringify(favs));
  }
}

function enrollFormation(id: number) {
  // Simule l'inscription locale
  let enrolled = JSON.parse(localStorage.getItem('enrolled') || '[]');
  if (!enrolled.includes(id)) {
    enrolled.push(id);
    localStorage.setItem('enrolled', JSON.stringify(enrolled));
  }
}

export default function FormationsPage() {
  const [formations, setFormations] = useState<Formation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [favIds, setFavIds] = useState<number[]>([]);
  const [enrolledIds, setEnrolledIds] = useState<number[]>([]);

  useEffect(() => {
    // MOCK: Simule des formations sans backend
    setTimeout(() => {
      setFormations([
        { id: 1, theme: 'Python', description: 'Cours Python' },
        { id: 2, theme: 'React', description: 'Cours React' },
        { id: 3, theme: 'Data Science', description: 'Introduction à la Data Science' },
      ]);
      setLoading(false);
    }, 500);
    // Charger les favoris
    setFavIds(getFavorites().map(f => f.id));
    // Charger les formations inscrites simulées
    setEnrolledIds(JSON.parse(localStorage.getItem('enrolled') || '[]'));
  }, []);

  const handleFavorite = (formation: Formation) => {
    addFavorite(formation);
    setFavIds(ids => [...ids, formation.id]);
  };

  const handleEnroll = (formation: Formation) => {
    enrollFormation(formation.id);
    setEnrolledIds(ids => [...ids, formation.id]);
  };

  if (loading) return <div className="text-center mt-16">Chargement...</div>;
  if (error) return <div className="text-center mt-16 text-red-500">{error}</div>;

  return (
    <div className="max-w-3xl mx-auto mt-8">
      <h1 className="text-2xl font-bold mb-6">Formations disponibles</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {formations.map(f => (
          <div key={f.id} className="bg-white rounded shadow p-4 flex flex-col">
            <div className="font-semibold text-blue-700 mb-1">{f.theme}</div>
            <div className="text-gray-600 mb-2">{f.description}</div>
            <div className="text-xs text-gray-400 mb-2">Supports : Vidéo, PDF (simulés)</div>
            <div className="flex gap-2 mt-2">
              <button
                className={`px-3 py-1 rounded ${favIds.includes(f.id) ? 'bg-yellow-400 text-white' : 'bg-gray-200 text-gray-700 hover:bg-yellow-200'}`}
                onClick={() => handleFavorite(f)}
                disabled={favIds.includes(f.id)}
              >
                {favIds.includes(f.id) ? 'Favori' : 'Ajouter aux favoris'}
              </button>
              <button
                className={`px-3 py-1 rounded ${enrolledIds.includes(f.id) ? 'bg-green-400 text-white' : 'bg-blue-600 text-white hover:bg-blue-700'}`}
                onClick={() => handleEnroll(f)}
                disabled={enrolledIds.includes(f.id)}
              >
                {enrolledIds.includes(f.id) ? 'Inscrit' : 'S’inscrire'}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
