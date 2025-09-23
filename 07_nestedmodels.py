from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name:str
    email:str
    address:Address


address = Address(
    street="123 Main street",
    city="barwaa",
    state="haryana",
    zip_code="121001"
)

person_1 = User(
    name="Saaransh Mehta",
    email="saaransh@gmail.com",
    address=address

)

print(person_1.model_dump())