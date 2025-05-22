'use client';
import { useState } from 'react';

interface Favorite {
  id: number;
  theme: string;
}

// Simule les favoris côté frontend (localStorage)
function getFavorites(): Favorite[] {
  if (typeof window === 'undefined') return [];
  const fav = localStorage.getItem('favorites');
  return fav ? JSON.parse(fav) : [];
}

export default function FavoritesPage() {
  const [favorites, setFavorites] = useState<Favorite[]>(getFavorites());

  const removeFavorite = (id: number) => {
    const updated = favorites.filter(f => f.id !== id);
    setFavorites(updated);
    localStorage.setItem('favorites', JSON.stringify(updated));
  };

  return (
    <div className="max-w-2xl mx-auto mt-8">
      <h1 className="text-2xl font-bold mb-6">Mes favoris</h1>
      {favorites.length === 0 ? (
        <div className="text-gray-500">Aucun favori enregistré.</div>
      ) : (
        <div className="grid grid-cols-1 gap-4">
          {favorites.map(f => (
            <div key={f.id} className="bg-white rounded shadow p-4 flex justify-between items-center">
              <div>{f.theme}</div>
              <button onClick={() => removeFavorite(f.id)} className="text-red-500 hover:underline">Supprimer</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
