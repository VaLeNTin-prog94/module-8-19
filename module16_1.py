from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() :
    return f"Главная страница"


@app.get("/user/admin")
async def user_admin() :
    return f"Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_id_client(user_id:int=123) :
    return  f"Вы вошли как пользователь {user_id}"

@app.get("/user")
async def news(username:str,age:int) :
    return  f"Информация о пользователе . Имя {username}, Возраст {age}"
