// Utilitaire pour appels API avec gestion du JWT
import { getToken } from './auth';

const API_URL = 'http://localhost:8000';

export async function apiFetch(path: string, options: RequestInit = {}) {
  const token = getToken();
  // On force la création d'un objet headers de type Record<string, string>
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...Object.fromEntries(Object.entries(options.headers || {})),
  };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers,
    credentials: 'include',
  });
  if (!res.ok) {
    throw new Error(await res.text());
  }
  return res.json();
}
