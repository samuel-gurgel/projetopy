from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


# basicamente faz uma forma de nao mandar a senha


class UserDB(UserSchema):
    id: int


# fica com todos os campos do UserSchema e mas o id: int


class UserList(BaseModel):
    users: list[UserPublic]
