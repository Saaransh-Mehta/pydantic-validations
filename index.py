from pydantic import BaseModel

class User(BaseModel):
    id:str
    name:str
    isActive : bool


input_data = {
    'id':"23",
    'name':"John",
    'isActive':True
}

user = User(**input_data)
print(user)



class Car(BaseModel):
    id:int
    name:str
    isElectric:bool
    price:float


fortuner = {'id':1,'name':"Fortuner",'isElectric':False,'price':30000000.00}

newCar = Car(**fortuner)
print(newCar)