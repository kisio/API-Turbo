from uuid import uuid4,UUID
from fastapi import FastAPI, HTTPException
from typing import List

from models import Career, Gender, Roles, Update_user, User

app=FastAPI()

db: List[User]=[
    User(
        id=UUID("9c60d3aa-1b19-4f68-8da9-e1e9348bef88"),
        first_name="Derrick",
        last_name="selempo",
        gender=Gender.male,
        roles=[Roles.student],
        career=[Career.expert]
        ),
        
    User(
        id=UUID("4726914e-640b-4121-b680-1c32dcbc8ae4"),
        first_name="Mary",
        last_name="wangui",
        gender=Gender.female,
        roles=[Roles.user],
         career=[Career.intermediate]
        )
]
# initialize
@app.get("/")
async def root():
    return {"Hello":"Derrick"}

# fetch data from API
@app.get('/api/v1/users')
async def fetch_users():
    return db;

# post request
@app.post('/api/v1/users')

async def register_user(user:User):
    db.append(user)
    return {
        "id":user.id
    }

# update api
@app.put('/api/v1/users/{user_id}')
async def update_user(user_update:Update_user,user_id:UUID):
    # get the databse
    # Check if user exists
    for user in db:
        if user.id == user_id:
            # updates
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name==user_update.middle_name
            if user_update.roles is not None:
                user.roles ==user_update.roles
            if user_update.career is not None:
                user.career ==user_update.career
            return
        # raise exceptions
    raise HTTPException(
        status_code=404,
        detail=f" user with id {user_id} is hot air(does not exist)"
    )        
        
# delete data from api
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )