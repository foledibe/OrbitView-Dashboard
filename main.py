"""
OrbitView Dashboard
A terminal dashboard showing NASA's photo of the day and the ISS's live location.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")


def get_apod():
    """Get NASA's Astronomy Picture of the Day."""
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def main():
    if not NASA_API_KEY:
        print("No API key found! Add NASA_API_KEY to your .env file.")
        return

    data = get_apod()
    print(data)  # raw print for now


if __name__ == "__main__":
    main()