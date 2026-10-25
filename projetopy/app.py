from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from projetopy.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    # user.model adiciona todos os campos de user para user_with_id
    # cria um dicionario
    # o parantese depois da classe significa que voce ta chamando a classe como
    # se fosse uma funcao, e ela devolve um objeto novo daquele tipo

    database.append(user_with_id)

    return user_with_id
    # basicamente ele pega a mensagem que voce manda em JSON
    # e converte para uma classe do python


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}
    # esse response_model=UserList faz que o FastApi olhe o schema UserList no
    # schemas e valide se esta igual ou nao


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='ERROR! User not found'
        )
        # raise faz com que esse erro "exploda" ou seja seja mostrado na tela
    database[user_id - 1] = user_with_id

    return user_with_id
    # esse user_id ele pede uma variavel int que identifique qual eh o termo
    # que vai ser mudado


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='ERROR! User not found'
        )
    return database.pop(user_id - 1)
