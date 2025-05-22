import Image from "next/image";
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-blue-100 p-8">
      <h1 className="text-4xl font-bold mb-4 text-blue-800">Bienvenue sur Étudiant+</h1>
      <p className="mb-8 text-lg text-gray-700 max-w-xl text-center">
        Plateforme moderne pour gérer vos inscriptions, formations, favoris et supports de cours. Connectez-vous ou inscrivez-vous pour découvrir toutes les fonctionnalités !
      </p>
      <div className="flex gap-4">
        <Link href="/login" className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Connexion</Link>
        <Link href="/register" className="px-6 py-2 bg-white border border-blue-600 text-blue-700 rounded hover:bg-blue-50">Inscription</Link>
      </div>
      <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-4xl">
        <div className="bg-white rounded shadow p-6 flex flex-col items-center">
          <span className="text-2xl mb-2">🎓</span>
          <h2 className="font-semibold mb-1">Formations par thème</h2>
          <p className="text-gray-500 text-center">Explorez et inscrivez-vous à des formations variées selon vos intérêts.</p>
        </div>
        <div className="bg-white rounded shadow p-6 flex flex-col items-center">
          <span className="text-2xl mb-2">⭐</span>
          <h2 className="font-semibold mb-1">Favoris</h2>
          <p className="text-gray-500 text-center">Ajoutez des formations à vos favoris pour les retrouver facilement.</p>
        </div>
        <div className="bg-white rounded shadow p-6 flex flex-col items-center">
          <span className="text-2xl mb-2">📚</span>
          <h2 className="font-semibold mb-1">Supports de cours</h2>
          <p className="text-gray-500 text-center">Accédez à des vidéos et documents pour chaque formation.</p>
        </div>
      </div>
    </div>
  );
}
