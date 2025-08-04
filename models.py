from pydantic import BaseModel


class BidRequestResponse(BaseModel):
    producer: str
    price: float
