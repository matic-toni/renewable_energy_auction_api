from pydantic import BaseModel, field_validator


class BidModel(BaseModel):
    producer: str
    price: float

    @field_validator('price')
    def check_price(cls, price):
        if price < 0:
            raise ValueError("Price has to be larger than 0")
        return price
