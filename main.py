from fastapi import FastAPI, status, Depends, HTTPException
import models
from typing import Annotated
from sqlalchemy.orm import Session
import auth
from auth import get_current_user

app = FastAPI()
app.include_router(
    auth.router
)
models.Base.metadata.create_all(models.engine)


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        return HTTPException(status_code=401, detail="Authentication Fail")
    return {"User": user}
