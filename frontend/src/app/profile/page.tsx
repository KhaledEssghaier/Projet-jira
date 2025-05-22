'use client';
import { useAuth } from '../../components/AuthProvider';
import { useState } from 'react';

// Page de gestion de profil
export default function ProfilePage() {
  const { user, refresh } = useAuth();
  const [email, setEmail] = useState(user?.email || '');
  const [message, setMessage] = useState('');

  const handleUpdate = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage('');
    try {
      // Ici, on suppose un endpoint PATCH /users/{id} (à adapter selon backend)
      const res = await fetch(`http://localhost:8000/users/${user?.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('jwt')}`,
        },
        body: JSON.stringify({ email }),
      });
      if (!res.ok) throw new Error('Erreur lors de la mise à jour');
      setMessage('Profil mis à jour !');
      refresh();
    } catch (err: any) {
      setMessage(err.message);
    }
  };

  if (!user) return <div className="text-center mt-16">Veuillez vous connecter.</div>;

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh]">
      <h1 className="text-2xl font-bold mb-4">Mon Profil</h1>
      <form onSubmit={handleUpdate} className="bg-white p-8 rounded shadow w-full max-w-sm flex flex-col gap-4">
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} className="border p-2 rounded" />
        <button type="submit" className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Mettre à jour</button>
        {message && <div className="text-blue-600 text-sm">{message}</div>}
      </form>
    </div>
  );
}
