from typing import Optional,List
from uuid import UUID,uuid4
from pydantic import BaseModel
from enum import Enum


# gender
class Gender(str,Enum):
    male="male"
    female="female"
    student="student"
# roles,you can specify other attributes in the same way
class Roles(str,Enum):
    admin="admin"
    user="user"
    student="student"

class Career(str,Enum):
    expert="expert"
    intermediate="intermediate"
    entry="entry"
    
# db
class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:Optional[str]
    last_name:Optional[str]
    middle_name:Optional[str]
    gender:Gender
    roles:List[Roles]
    career:Optional[List[Career]]

# update class
class Update_user(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    middle_name: Optional[str]
    roles:Optional[List[Roles]]
    career:Optional[List[Career]]
    