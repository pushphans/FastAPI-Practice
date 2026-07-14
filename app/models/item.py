from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    owner_id = Column(String, nullable=False)  # Store Supabase user ID (UUID as string)