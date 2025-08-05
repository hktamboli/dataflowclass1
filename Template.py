#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script Name: example_script.py
Description: Brief description of what the script does.
Author: Harish Tamboli
Date: YYYY-MM-DD
"""

# 📦 Import necessary libraries
import os
import sys
import json
import logging
from datetime import datetime

# 🛠️ Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 📁 Constants and configuration
DATA_PATH = "data/input.json"
OUTPUT_PATH = "data/output.json"

# 🧠 Utility functions
def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load JSON: {e}")
        return {}

def save_json(data, file_path):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Failed to save JSON: {e}")

# 🔁 Main logic
def process_data(data):
    """Process the input data and return results."""
    # Example transformation
    return {k: v.upper() if isinstance(v, str) else v for k, v in data.items()}

# 🚀 Main entry point
def main():
    logging.info("Script started.")
    
    data = load_json(DATA_PATH)
    if not data:
        logging.warning("No data to process.")
        return
    result = process_data(data)
    save_json(result, OUTPUT_PATH)

    logging.info("Script finished.")

# 🧪 Run script
if __name__ == "__main__":
    main()
