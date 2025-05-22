// Barre de navigation responsive
'use client';
import Link from 'next/link';
import { useAuth } from './AuthProvider';

export default function Navbar() {
  const { user, logout } = useAuth();
  return (
    <nav className="w-full flex justify-between items-center py-4 px-6 bg-white shadow mb-8">
      <div className="font-bold text-xl text-blue-700">
        <Link href="/">Étudiant+</Link>
      </div>
      <div className="flex gap-4 items-center">
        <Link href="/formations" className="hover:underline">Formations</Link>
        {user && <Link href="/my-formations" className="hover:underline">Mes formations</Link>}
        {user && <Link href="/favorites" className="hover:underline">Favoris</Link>}
        {user ? (
          <>
            <Link href="/profile" className="hover:underline">Profil</Link>
            <button onClick={logout} className="ml-2 px-3 py-1 rounded bg-red-500 text-white">Déconnexion</button>
          </>
        ) : (
          <>
            <Link href="/login" className="hover:underline">Connexion</Link>
            <Link href="/register" className="hover:underline">Inscription</Link>
          </>
        )}
      </div>
    </nav>
  );
}
