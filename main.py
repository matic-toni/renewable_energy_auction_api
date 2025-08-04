import logging
import threading

from fastapi import FastAPI, status, HTTPException
from models import BidRequestResponse
from auction import Auction, Bid

app: FastAPI = FastAPI()
auction: Auction = Auction()
lock: threading.Lock = threading.Lock()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.post("/add_bid", status_code=status.HTTP_201_CREATED)
def add_bid(bid_request: BidRequestResponse) -> None:
    logger.info(f"Received new bid: {bid_request}")

    bid: Bid = Bid(bid_request.producer, bid_request.price)
    try:
        with lock:
            auction.add_bid(bid)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to add bid: {str(e)}")


@app.get("/get_lowest_bid", response_model=BidRequestResponse)
def get_lowest_bid() -> BidRequestResponse:
    with lock:
        bid: Bid = auction.get_lowest_bid()

        if bid is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No bids available"
            )

        bid_response: BidRequestResponse = BidRequestResponse(producer=bid.producer, price=bid.price)
        return bid_response
