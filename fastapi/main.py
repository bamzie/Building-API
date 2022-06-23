'''
Created on Jun 22, 2022

@author: McCaitlyn
'''
from turtle import up
from typing import List
from uuid import UUID, uuid4
from model import Update, User, Gender, Role

' Importing fastapi'
from fastapi import FastAPI, HTTPException

'creating instance of application'
app = FastAPI()

db: List[User] = [
    User(id = UUID('52d60b6f-06da-4837-8c76-edecf9cf5f23'),
         first_name = "McCaitlyn",
         last_name = 'Despues', 
         gender = Gender.female, 
         roles = [Role.student] 
         ),
    User(id = UUID('bddb67c6-49ae-4e1b-9485-92f93dc47ed2'),
         first_name = "Brian",
         last_name = 'Morales', 
         gender = Gender.male, 
         roles = [Role.student] 
         )
]
'instance of our app'
'this is our GET http request'
'currently the root (/) is the path'
@app.get("/")
async def root():
    'for now we return dictionary '
    return {"hello": "Bamz"}


@app.get("/api/v1/users")
async def fetch_users():
    return db; 


'''
The resource is our endpoint (post) and we 
are posting to our server. 
'''

@app.post("/api/v1/users")

async def register_user(user: User):
    '''
    This function takes a user and will append it to
    our db list. We return the user id 
    '''
    db.append(user)
    return {"id": user.id}

'''
Use to delete a resource(user in this case)
'''
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID): 
    for user in db: 
        if user.id == user_id: 
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} does not exist"
    )
'''
We know wil be updating a users first, middle, last name and roles.
'''
@app.put("/api/v1/users/{user_id}")
async def update_user(update_user: Update, user_id: UUID): 
    for user in db: 
        if user.id == user_id: 
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None: 
                user.middle_name = update_user.middle_name
            if update_user.roles is not None: 
                user.roles = update_user.roles
            return
    raise HTTPException(
        status_code=404,
        detail = f"User with id: {user_id} does not exist. Update failed"
    )

