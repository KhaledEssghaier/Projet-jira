from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base

# Association table for many-to-many between Student and Formation
student_formation = Table(
    'student_formation', Base.metadata,
    Column('student_id', Integer, ForeignKey('users.id')),
    Column('formation_id', Integer, ForeignKey('formations.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_student = Column(Boolean, default=True)
    role = Column(String, default="student")
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    department = relationship("Department", back_populates="students")
    formations = relationship("Formation", secondary=student_formation, back_populates="students")

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    students = relationship("User", back_populates="department")

class Formation(Base):
    __tablename__ = "formations"
    id = Column(Integer, primary_key=True, index=True)
    theme = Column(String, nullable=False)
    description = Column(String, nullable=True)
    students = relationship("User", secondary=student_formation, back_populates="formations")
