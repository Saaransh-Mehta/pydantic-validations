from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street:str
    city:str
    code:str

class User(BaseModel):
    id:str
    name:str
    email:str
    is_active:bool = True
    created_at:datetime = datetime.now()
    address:Address
    tags:List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v:v.strftime('%d-%m-%Y %H:%M:%S')}

    )


user = User(
    id="123",
    name="John Doe",
    email="johndoe@gmail.com",
    created_at=datetime(2025,1,1,12,0,0),
    is_active=False,
    address=Address(
        street="123 Main St",
        city="New York",
        code="10001"
    ),
    tags=["admin","user"]
)

print(user.model_dump())


json_string = user.model_dump_json()
print(json_string)