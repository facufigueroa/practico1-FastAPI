from fastapi import FastAPI, Depends
from routers import products, users
from dependencies import verifyApiToken

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router, dependencies=[Depends(verifyApiToken)])

@app.get("/")
async def root():
    return {
        "message": "Welcome!",
        "status": 200
    }