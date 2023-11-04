from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import time

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    # ваш код здесь
    return {"message": "Hello World"}

@app.post('/post')
def post(item: Timestamp):
    item.id = len(post_db)
    item.timestamp = datetime.datetime.now().hour
    return {"id": item.id, "timestamp": item.timestamp}

@app.get('/dog')
def dog(dog: Dog):
    return dog

# ваш код здесь
# @app.post('/post')
# def post(zap: Timestamp):
#     result = post_db.append(zap)
#     return result


# @app.post('/post')
# def post(id: int):
#     Timestamp.timestamp = datetime.datetime.now().hour
#     Timestamp.id = id
#     post_db.append(Timestamp)
#     return post_db

# @app.post('/post')
# def post(item: Timestamp):
#     # item.timestamp = datetime.datetime.now().hour
#     # item.id = len(post_db)
#     # post_db.append(item)
#     return post_db






# test
