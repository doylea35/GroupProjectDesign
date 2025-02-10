import os
from pydantic import BaseModel, EmailStr
from typing import Optional, List


class User(BaseModel):
    email: str # Primary Key ; en un futur plantejar fer-ho amb EmailStr, requerreix email validator
    name: str
    groups: Optional[List[str]] = None # List of Foreign Keys referencing Group.id

class Group(BaseModel): #_id as Primary key, automatically created, can be found using ObjectID
    members: List[str] # List of Foreign Keys referencing User.email
    name: str
    tasks: Optional[List[str]] = None # List of Foreign Keys referencing Task.id

class Task(BaseModel): #_id as Primary key, automatically created, can be found using ObjectID
    assigned_to: str # Foreign Key referencing User.email
    name: str
    description: str
    due_date: str
    status: str # ["To Do", "In Progress", "Completed"]
    group: str # Foreign Key referencing Group.id
    priority: str # ["Low", "Medium", "High"]
