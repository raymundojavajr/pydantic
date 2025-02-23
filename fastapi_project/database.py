from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./test.db"  # Using SQLite (Replace with PostgreSQL/MySQL for production)

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Database Models
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    orders = relationship("OrderDB", back_populates="user")

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserDB", back_populates="orders")

# Create tables in the database
Base.metadata.create_all(bind=engine)
