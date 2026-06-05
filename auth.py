from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from models import Users, SessionLocal
import bcrypt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

SECRET_KEY = "197b2C37C391b93fe80344Fe73b806947a65e36206e05a1a23c2fa12702Fe3"
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


class CreateUserRequest(BaseModel):
    fullname: str
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code=status. HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):

    password_bytes = create_user_request.password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)
    db_hashed_password = hashed_password_bytes.decode("utf-8")

    create_user_model = Users(fullname=create_user_request.fullname,
                              username=create_user_request.username,
                              hashed_password=db_hashed_password,)
    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
async def login_from_access_token(from_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(from_data.username, from_data.password, db)

    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')

    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()

    if not user:
        return False

    password_bytes = password.encode("utf-8")
    hashed_password_bytes = user.hashed_password.encode("utf-8")

    if not bcrypt.checkpw(password=password_bytes, hashed_password=hashed_password_bytes):
        return False

    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')

        if username is None or user_id is None:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
