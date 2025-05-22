from pydantic import BaseModel, EmailStr
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        from_attributes = True

class FormationBase(BaseModel):
    theme: str
    description: Optional[str] = None

class FormationCreate(FormationBase):
    pass

class Formation(FormationBase):
    id: int
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_student: Optional[bool] = True
    role: Optional[str] = "student"
    department_id: Optional[int] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    department: Optional[Department] = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class EnrollmentCreate(BaseModel):
    student_id: int
    formation_id: int

class Enrollment(BaseModel):
    student_id: int
    formation_id: int
    class Config:
        from_attributes = True
