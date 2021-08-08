from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {
            'name': 'Krzysiek'
        }
    }


@app.get('/about')
def about():
    return {
        'data': 'about page'
    }


@app.get('/blog/unpublished')
def unpublished_blogs():
    return {'data': 'all unpublished blogs'}


@app.get('/blogs')
def get_blogs(limit: int = 10, published: bool = True):
    if published:
        return {'data': 'return all published blogs'}

    return {'data': 'return all blogs'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'data': id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with {request.title}'}



