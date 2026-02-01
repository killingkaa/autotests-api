from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Модель данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserRequestSchema(BaseModel):
    """
    схема данных для создания пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Схема данных ответа на запрос создания пользователя
    """
    user: UserSchema