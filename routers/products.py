from fastapi import APIRouter
from get_all_products import get_products

router = APIRouter(prefix="/products")

@router.get("/{keywords}")
async def root(keywords: str):
    return get_products(keywords)