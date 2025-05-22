// Utilitaires pour gestion du JWT et de la session utilisateur
export function setToken(token: string) {
  if (typeof window !== 'undefined') {
    localStorage.setItem('jwt', token);
  }
}

export function getToken(): string | null {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('jwt');
  }
  return null;
}

export function removeToken() {
  if (typeof window !== 'undefined') {
    localStorage.removeItem('jwt');
  }
}

export function isAuthenticated(): boolean {
  return !!getToken();
}
