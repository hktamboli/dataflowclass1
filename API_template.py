#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: api_request_script.py
Description: Makes a GET request to an API and processes the response.
Author: Harish Tamboli
Date: YYYY-MM-DD
"""

import requests
import logging
import json
from typing import Optional

# 🛠️ Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 🌐 API Configuration
API_URL = "https://api.example.com/data"
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Accept": "application/json"
}

# 📡 Function to make API call
def fetch_data_from_api(url: str, headers: dict) -> Optional[dict]:
    """Fetch data from the given API endpoint."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    return None

# 🧠 Function to process API response
def process_data(data: dict) -> dict:
    """Process the API response data."""
    # Example: Extract specific fields
    return {item["id"]: item["name"] for item in data.get("results", [])}

# 🚀 Main function
def main():
    logging.info("Starting API request script...")
    
    data = fetch_data_from_api(API_URL, HEADERS)
    if data:
        processed = process_data(data)
        logging.info(f"Processed {len(processed)} items.")
        print(json.dumps(processed, indent=4))
    else:
        logging.warning("No data received from API.")

    logging.info("Script finished.")

# 🧪 Entry point
if __name__ == "__main__":
    main()
