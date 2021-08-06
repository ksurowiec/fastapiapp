from fastapi import FastAPI
from typing import Optional

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
