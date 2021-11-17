from lib2to3.pytree import Base
from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

class Gig(BaseModel):
    address: str
    category: str
    start_time: str
    end_time: str
    notes: str
    rate_of_pay: float


class Company(BaseModel):
    name: str
    password: str
    rating: float
    username: str


class Pro(BaseModel):
    address: str
    bank_account_number: str
    birthday: str
    first_name: str
    last_name: str
    phone_number: str
    photo_url: str
