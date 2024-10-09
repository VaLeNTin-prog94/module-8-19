from fastapi import FastAPI, Path, Body, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated
from typing import List
from fastapi.templating import Jinja2Templates

users = []
app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request,
                                                    'users': users})


@app.get('/user/{user_id}')
async def get_users(
        request: Request,
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User Id')]) -> HTMLResponse:
    for user in users:
        if int(user.id) == user_id:
            return templates.TemplateResponse('users.html',
                                              {'request': request,
                                               'user': user})
        #raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{user_id}/{username}/{age}')
async def post_user(username: str, age: int):
    try:
        user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
        user = User(id=user_id, username=username, age=age)
        users.append(user)
    except HTTPException:
        raise HTTPException(status_code=404, detail="User was not found")


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
