from pydantic import BaseModel,Field
from typing import List, Optional,Dict
import re


class Cart(BaseModel):
    id:int
    items:List[str]
    quantities:Optional[Dict[str,int]] = None
    total_price:float

cart_1 = Cart(id=2,items=["apple","banana"],quantities={'hello':1},total_price=250.09)
print(cart_1)

class Employee(BaseModel):
    id:str = Field(
        ...,
    )

    name:str = Field(
        ...,
        min_length=2,
        max_length=50,
        title="Name of the Employee",
        description="This field is required and must be between 2 and 50 characters",
        examples="Saaransh Mehta"
    )
    designation:str
    salary:float = Field(
        ...,
        ge=10000,

    )

    department:Optional[str] = "HR"
    skills:Optional[List[str]] = "Communication"

class User(BaseModel):
    username:str = Field(
        ...,
        min_length=3,
        max_length=50,
        regex=r'^[a-zA-Z0-9_]+$',
        description="Username must be alphanumeric and can include underscores",
        examples="user_123"
    )
    email:str = Field(
        ...,
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        description="Must be a valid email address",
        examples="example@gmail.com"
    )
    phone:str = Field(
        ...,
        description="Phone number must be in the format +91 9999999",
        min_lenght=10,
        max_length=10
    )


