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

# post_db.append(Timestamp(id=10, timestamp=datetime.datetime.now().hour))
# print(post_db)


@app.get('/')
def root():
    # ваш код здесь
    return {"message": "Hello World"}


# ваш код здесь
# @app.post('/post')
# def post(zap: Timestamp):
#     result = post_db.append(zap)
#     return result


@app.post('/post')
def post(id: int, zap: Timestamp):
    zap.timestamp = datetime.datetime.now().hour
    zap.id = id
    post_db.append(zap)
    return post_db
   
# test
