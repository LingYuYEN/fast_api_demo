from typing import Optional, List, Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


app.debug = True
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInfo(BaseModel):
    name: str
    phone: str
    id: int


class UserCreate(BaseModel):
    name: str
    phone: str


default_id = 4
user_arr = [
    {
        "name": "Louis",
        "phone": "091234876",
        "id": 1
    },
    {
        "name": "Hook",
        "phone": "09125394876",
        "id": 2
    },
    {
        "name": "Sam",
        "phone": "099384796",
        "id": 3
    },
]


@app.get("/users")
def get_user():
    return user_arr


@app.get("/users/{user_id}")
def get_user_from_id(
        user_id: int
):
    return user_arr[user_id - 1]


@app.put("/users/{user_id}")
def update_user(
        user_id: int,
        user: UserCreate
):
    user_arr[user_id - 1] = {
        "id": user_id,
        "name": user.name,
        "phone": user.phone,
    }
    return user_arr[user_id - 1]


@app.post("/users")
def post_user(
        user: UserCreate
):
    global default_id
    global user_arr
    user_dict = user.dict()
    user_dict['id'] = default_id
    default_id += 1
    user_arr.append(user_dict)
    return user_dict


@app.delete("/users/{user_id}")
def delete_user_from_id(
        user_id: int
):
    user_arr.remove(user_arr[user_id - 1])
    return user_arr


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=False, workers=1)
