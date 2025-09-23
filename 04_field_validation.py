from pydantic import BaseModel, field_validator, Field , model_validator
from typing import List, Optional, Dict

class User(BaseModel):
    username:str
    age:int

    @field_validator('username')
    def username_len(cls,v):
        if len(v) < 3 or len(v) > 50:
            raise ValueError("Username must not exceed the limit of 3 to 50 characters")
        return v
    @model_validator(mode='after')
    def model_verify(cls,values):
        age = values.age
        if age < 18:
            raise ValueError("Age must be greater than or equal to 18")
        return values

