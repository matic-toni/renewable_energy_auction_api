# Renewable Energy Auction System

A FastAPI application that manages bids from renewable energy producers and efficiently retrieves the lowest-cost offer using a min-heap data structure.

## Requirements
1. Python 3.7+
2. pip

## Setup & Installation

1. **Create and activate virtual environment**
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
  
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:** http://localhost:8000

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
- Interactive docs: http://localhost:8000/docs

Solution is:
- Thread-safe: Uses `threading.Lock()` to prevent race conditions during read/write access to the bid heap.
