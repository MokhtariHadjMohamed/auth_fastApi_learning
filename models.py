from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///mydatabase.db", echo=True)

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, fullname={self.fullname!r}, username={self.username!r})"


SessionLocal = sessionmaker(bind=engine)
