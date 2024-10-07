from fastapi import FastAPI, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List

users = []
app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_messages() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int):
    #user_id = max(x['id'] for x in users) + 1 if users else 1
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int, ):
    try:
        users[user_id - 1] = User(id=user_id, username=username, age=age)
        return User(id=user_id, username=username, age=age)
    except HTTPException:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        users.pop(user_id - 1)
        return f'"User {user_id} has been deleted"'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
