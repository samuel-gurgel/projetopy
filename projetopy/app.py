from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from projetopy.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula02():
    return """
    <html>
      <head>
        <title>Nosso ola mundo!</title>
      </head>
      <body>
        <h1> Ola Mundo </h1>
      </body>
    </html>"""
