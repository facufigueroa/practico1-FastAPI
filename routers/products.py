from fastapi import APIRouter, HTTPException, Body, Depends
from typing_extensions import Annotated
from pydantic import BaseModel, Field

router = APIRouter(prefix="/products", tags=["products"])

dbProducts = []

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)

@router.post("/")
async def createProduct(productData: Annotated[Product, Body()]):
    for existingProduct in dbProducts:
        if existingProduct["name"] == productData.name:
            raise HTTPException(status_code=400, detail=f'Product "{productData.name}" already exist!')
    
    newProduct = productData.model_dump()
    newProduct["id"] = len(dbProducts) + 1
    dbProducts.append(newProduct)

    return {
        "message": "Product successfully created!",
        "user": newProduct
    }

@router.get("/")
async def getProducts():
    return {
        "products": dbProducts
    }