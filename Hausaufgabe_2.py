from pydantic import BaseModel, EmailStr, model_validator
import json

""" Создать классы моделей данных с помощью Pydantic для пользователя и его адреса. """

class Address(BaseModel):
    city: str
    street: str
    house_number: int


class User(BaseModel):
    id: int | None = None
    name: str
    age: int
    email: EmailStr
    is_employed: bool
    address: Address

    @model_validator(mode='after')
    def check_age_and_employment(self):
        if self.is_employed and not (18 <= self.age <= 65):
             raise ValueError("Age must be between 18 and 65 for employed users")
        return self


# json_input = """{
#     "name": "John Doe",
#     "age": 70,
#     "email": "john.doe@example.com",
#     "is_employed": true,
#     "address": {
#         "city": "New York",
#         "street": "5th Avenue",
#         "house_number": 123
#     }
# }"""


json_input = """{
    "name": "John Doe",
    "age": 65,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}"""


# json_input = """{
#     "name": "John Doe",
#     "age": 64,
#     "email": "john.doe@example.com",
#     "is_employed": false,
#     "address": {
#         "city": "New York",
#         "street": "5th Avenue",
#         "house_number": 123
#     }
# }"""


data = json.loads(json_input)

if __name__ == '__main__':
    user = User(**data)
    print(user)