from pydantic import BaseModel, computed_field

class Cart(BaseModel):
    id:int
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


cart_1 = Cart(id=2,price=250,quantity=2)
print(cart_1.total_price)

print(cart_1.model_dump())