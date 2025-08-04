# Renewable Energy Auction System

A FastAPI application that manages bids from renewable energy producers and efficiently retrieves the lowest-cost offer.

## Requirements
1. Python 3.7+
2. pip
3. Git

## Setup & Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/matic-toni/renewable_energy_auction_api.git
    ```

2. **Create and activate virtual environment**
    - Windows
       ```bash
       python -m venv venv
       ```
       ```bash
       .\venv\Scripts\activate
       ```
    
   - Linux/MacOS
       ```bash
       python -m venv venv
       ```
     ```bash
     source venv/bin/activate
     ```
  
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API's docs:** http://localhost:8000/docs

## API Endpoints

### POST `/add_bid`
Add a new bid to the auction system.

**Request:**
```json
{
  "producer": "SolarCo",
  "price": 50.5
}
```

**Response:** HTTP 201 Created

### GET `/get_lowest_bid`
Get the current lowest bid.

**Response:**
```json
{
  "producer": "WindWorks", 
  "price": 45.0
}
```

Returns HTTP 404 if no bids available.

## Example Usage

```bash
# Add bids
curl -X POST "http://localhost:8000/add_bid" \
     -H "Content-Type: application/json" \
     -d '{"producer": "SolarCo", "price": 50.0}'

# Get lowest bid
curl -X GET "http://localhost:8000/get_lowest_bid"
```

## Solution

Uses Python's `heapq` for efficient bid management:
- Add bid: O(log n)
- Get lowest: O(1)

Uses `threading.Lock()` to prevent race conditions during read/write access to the bid heap.
