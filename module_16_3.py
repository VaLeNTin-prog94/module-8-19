from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, Возраст: 18'}


@app.get('/users')
async def get_all_messages() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str = Path(min_length=5, max_length=20, description="Tolik"),
                      age: int = Path(ge=1, le=120, description='18')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = {'Имя': username, 'Возраст': age}
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = {'Имя': username, 'Возраст': age}
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'"User {user_id} has been deleted"'
