# Backend FastAPI – Gestion Étudiants & Formations

## Fonctionnalités principales
- Authentification JWT (inscription, connexion, profil étudiant)
- Gestion des utilisateurs (étudiants, rôles, activation/désactivation)
- Modèle Département lié aux étudiants
- Gestion des formations (CRUD) avec thème et description
- API REST pour l’inscription d’un étudiant à une formation
- Endpoints sécurisés (auth obligatoire)
- Documentation automatique via Swagger (OpenAPI)
- Base de données PostgreSQL avec SQLAlchemy
- Tests de base

## Installation

1. Créez un environnement virtuel Python :
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Installez les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```
3. Configurez la base de données PostgreSQL dans `.env`.
4. Lancez le serveur :
   ```powershell
   uvicorn app.main:app --reload
   ```

## Structure du projet
- `app/` : code source principal
  - `models/` : modèles SQLAlchemy
  - `schemas/` : schémas Pydantic
  - `routes/` : endpoints FastAPI
  - `core/` : configuration, sécurité, utilitaires
  - `tests/` : tests unitaires et d’intégration
- `requirements.txt` : dépendances Python
- `.env` : variables d’environnement

## Documentation API
Accédez à la documentation interactive :
- Swagger UI : http://localhost:8000/docs
- Redoc : http://localhost:8000/redoc

## Tests
Lancez les tests avec :
```powershell
pytest
```
