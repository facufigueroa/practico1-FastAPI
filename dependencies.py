from fastapi import Query, HTTPException
from typing_extensions import Annotated

def verifyApiToken(token: Annotated[str, Query()]):
    if token != "nivel-intermedio-2026":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token