'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { setToken } from '../../utils/auth';

// Page de connexion étudiant
export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    // MOCK: connexion toujours acceptée si email et mot de passe non vides
    if (!email || !password) {
      setError('Veuillez remplir tous les champs');
      return;
    }
    // Simule un token JWT
    setToken('mock-jwt-token');
    router.push('/profile');
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh]">
      <h1 className="text-2xl font-bold mb-4">Connexion Étudiant</h1>
      <form onSubmit={handleSubmit} className="bg-white p-8 rounded shadow w-full max-w-sm flex flex-col gap-4">
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required className="border p-2 rounded" />
        <input type="password" placeholder="Mot de passe" value={password} onChange={e => setPassword(e.target.value)} required className="border p-2 rounded" />
        {error && <div className="text-red-500 text-sm">{error}</div>}
        <button type="submit" className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Se connecter</button>
      </form>
    </div>
  );
}
