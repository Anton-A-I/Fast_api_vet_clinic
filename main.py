from enum import Enum
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
import datetime
from typing import Annotated, List

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

# dogs_db[7] = Dog(name='test', pk=7, kind=DogType.terrier)
# print(dogs_db.get(2))
@app.get('/')
def root():
    # ваш код здесь
    return {"message": "Hello World"}

@app.post('/post', summary='Get Post')
def post(item: Timestamp):
    item.id = len(post_db)
    item.timestamp = datetime.datetime.now().hour
    return {"id": item.id, "timestamp": item.timestamp}

@app.get('/dog', summary='Get Dogs')
def dog(kind: Annotated[DogType, Query(...)]):
    filtered_dogs = [dog for dog in dogs_db.values() if dog.kind == kind]
    return filtered_dogs

@app.post('/dog', response_model=Dog, summary='Create Dog')
def create_dog(dog: Dog):
    new_key = int(list(dogs_db.keys())[-1]+1)
    dogs_db[new_key] = Dog(name='test'+str(new_key), pk=new_key, kind=DogType.terrier)
    return dog

@app.get('/dog/{pk}', summary='Get Dog By Pk')
def dog(pk: Annotated[int, Path(..., title='Pk')]) -> Dog:
    dog = dogs_db.get(pk)
    if dog:
        return dog
    else:
        return {"message": "Dog not found"}


# @app.get('/dog/{pk}', summary='Get Dog By Pk')
# def dog(pk: Annotated[int, Path(...)]):
#     filtered_dogs_pk = [dog for dog in dogs_db.values() if dog.pk == pk]
#     return {"dogs": filtered_dogs_pk}

# @app.get('/dog')
# def dog(kind: DogType = Query(...)):
#     filtered_dogs = [dog for dog in dogs_db.values() if dog.kind == kind]
#     return {"dogs": filtered_dogs}

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
