from pydantic import BaseModel
from typing import Optional ,List, Union

class Address(BaseModel):
    street:str
    city:str
    pincode:str

class Companies(BaseModel):
    name:str
    address:Optional[Address] = None

class Employee(BaseModel):
    name:str
    company:Optional[Companies] = None



class TextContent(BaseModel):
    title:str
    description:str


class ImageContent:
    title:str = "Image"
    description: str = "This is a image"



class Article(BaseModel):
    id:int
    overall_content = Optional[List[Union[TextContent,ImageContent]]] = None