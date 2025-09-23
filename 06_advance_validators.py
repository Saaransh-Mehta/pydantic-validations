from pydantic import BaseModel, Field , field_validator

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int
    email:str

    @field_validator('first_name','last_name')
    def name_starts_with_capital(cls,v):
        if not v[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return v


class User(BaseModel):
    email:str

    @field_validator('email')
    def normalize_wmail(cls,v):
        return v.lower.strip()
    



class Product(BaseModel):
    price:str


    @field_validator('price',mode='before')
    def parse_price(cls,v):
        if isinstance(v,str):
            return float(v.replace('$','').replace(',',''))
        return v