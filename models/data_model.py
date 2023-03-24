from pydantic import BaseModel

class Product(BaseModel):
    id: str
    title: str
    description: str
    images: list
    price: int
    url: str
    vendor: str

