import heapq
from dataclasses import dataclass


@dataclass
class Bid:
    producer: str
    price: float

    def __lt__(self, other):
        return self.price < other.price


class Auction:
    def __init__(self):
        self.bid_list = []

    def add_bid(self, bid: Bid):
        heapq.heappush(self.bid_list, bid)

    def get_lowest_bid(self):
        if len(self.bid_list) > 0:
            return self.bid_list[0]
        else:
            return None
