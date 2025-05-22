from fastapi import FastAPI
from app.routes import auth, users, departments, formations, enrollments
from app.core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Crée la base de données si elle n'existe pas
def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI(title="Gestion Étudiants & Formations", version="1.0.0")

# CORS (optionnel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(departments.router, prefix="/departments", tags=["departments"])
app.include_router(formations.router, prefix="/formations", tags=["formations"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])
