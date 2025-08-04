from fastapi import FastAPI, Response, status, HTTPException
from models import BidRequestResponse
from auction import Auction, Bid

app = FastAPI()
auction = Auction()


@app.post("/add_bid", status_code=status.HTTP_201_CREATED)
def add_bid(bid_model: BidRequestResponse, response: Response):
    print("Received new bid:", bid_model)

    bid = Bid(bid_model.producer, bid_model.price)
    try:
        auction.add_bid(bid)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to add bid: {str(e)}")



@app.get("/get_lowest_bid", response_model=BidRequestResponse)
def get_lowest_bid():
    bid = auction.get_lowest_bid()

    if bid is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    bid_model = BidRequestResponse(producer=bid.producer, price=bid.price)
    return bid_model
