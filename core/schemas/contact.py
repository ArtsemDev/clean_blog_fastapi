from pydantic import BaseModel, EmailStr, Field, ValidationError
from fastapi import Form

from .types import PhoneNumber


class ContactSchema(BaseModel):
    name: str = Field(min_length=2, max_length=64)
    email: EmailStr
    phone: PhoneNumber
    message: str

    @classmethod
    def as_form(
            cls,
            name: str = Form(),
            email: str = Form(),
            phone: str = Form(),
            message: str = Form()
    ):
        try:
            return cls(name=name, email=email, phone=phone, message=message)
        except ValidationError as e:
            return '\n'.join(i['msg'] for i in e.errors())
