from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    id: int
    items: List[str]
    total_price:float
    metadata: Optional[Dict[str, str]] = None

cart_1 = Cart(id=2,items=["apple","banana"],total_price=250.09)
print(cart_1)