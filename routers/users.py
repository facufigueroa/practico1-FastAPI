from fastapi import APIRouter, HTTPException, Body, Path, Query
from typing_extensions import Annotated
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["users"])

dbUsers = []

class User(BaseModel):
    username: str = Field(min_length=5)
    age: int = Field(ge=18)

@router.post("/")
async def createUser(userData: Annotated[User, Body()]):
    for existingUser in dbUsers:
        if existingUser["username"] == userData.username:
            raise HTTPException(status_code=400, detail=f'Username "{userData.username}" already exist!')
    
    newUser = userData.model_dump()
    newUser["id"] = len(dbUsers) + 1
    dbUsers.append(newUser)

    return {
        "message": "User successfully created!",
        "user": newUser
    }

@router.get("/{userId}")
async def getUserById(userId: Annotated[int, Path(gt=0)], category: Annotated[str, Query(min_length=3)] = "general"):
    for existingUser in dbUsers:
        if existingUser["id"] == userId:
            return {
                "user": existingUser,
                "category": category
            }
    
    raise HTTPException(status_code=404, detail="User not found")