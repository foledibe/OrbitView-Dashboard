"""
OrbitView Dashboard
A terminal dashboard showing NASA's photo of the day and the ISS's live location.
"""

import os
import requests
from dotenv import load_dotenv
from colorama import init, Fore, Style

init(autoreset=True)

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")


def get_apod():
    """Get NASA's Astronomy Picture of the Day."""
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_iss_location():
    """Get the International Space Station's current latitude/longitude."""
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    lat = float(data["iss_position"]["latitude"])
    lon = float(data["iss_position"]["longitude"])
    return lat, lon


def get_astronauts():
    """Get the number of people currently in space."""
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["number"]


def space_vibe_check(lat, num_astronauts):
    """Turn the ISS's position into a fun one-line status message."""
    if abs(lat) < 10:
        location_vibe = "cruising right along the equator"
    elif lat > 50:
        location_vibe = "way up near the northern edge of its orbit"
    elif lat < -50:
        location_vibe = "swinging down toward the southern edge of its orbit"
    elif lat > 0:
        location_vibe = "somewhere over the Northern Hemisphere"
    else:
        location_vibe = "somewhere over the Southern Hemisphere"

    return f"🛰️  The ISS is {location_vibe}, carrying {num_astronauts} astronauts right now."


def display_apod(data):
    """Print today's astronomy picture info in color."""
    print(Style.BRIGHT + Fore.CYAN + "\n=== OrbitView: Astronomy Picture of the Day ===")
    print(Fore.YELLOW + f"Title: {data['title']}")
    print(Fore.WHITE + f"Date:  {data['date']}")
    print(Fore.WHITE + f"Image: {data.get('url', 'N/A')}")

    explanation = data.get("explanation", "")
    short_explanation = explanation[:200] + "..." if len(explanation) > 200 else explanation
    print(Fore.WHITE + f"\n{short_explanation}\n")


def display_iss(lat, lon, num_astronauts):
    """Print the ISS's current position in color."""
    print(Style.BRIGHT + Fore.CYAN + "=== ISS Live Location ===")
    print(Fore.YELLOW + f"Latitude:  {lat:.2f}")
    print(Fore.YELLOW + f"Longitude: {lon:.2f}")
    print(Fore.MAGENTA + f"Status: {space_vibe_check(lat, num_astronauts)}\n")


def main():
    if not NASA_API_KEY:
        print(Fore.RED + "No API key found! Add NASA_API_KEY to your .env file.")
        return

    try:
        apod_data = get_apod()
        lat, lon = get_iss_location()
        num_astronauts = get_astronauts()
    except requests.exceptions.RequestException:
        print(Fore.RED + "Something went wrong reaching the APIs. Check your connection or API key.")
        return

    display_apod(apod_data)
    display_iss(lat, lon, num_astronauts)


if __name__ == "__main__":
    main()