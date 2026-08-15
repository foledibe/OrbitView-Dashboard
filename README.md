# 🛰️ OrbitView Dashboard

A terminal dashboard that pulls NASA's Astronomy Picture of the Day and
tracks the International Space Station's live location - complete with a
"Space Vibe Check" status line and an ASCII orbit history chart.

## Features

- 🌌 NASA's Astronomy Picture of the Day, pulled live
- 🛰️ Real-time ISS latitude/longitude
- 👩‍🚀 Live count of astronauts currently in space
- 🔮 "Space Vibe Check" - a fun status line based on the ISS's position
- 📈 ASCII chart tracking the ISS's recent orbit path

## Tech stack

- Python
- [requests](https://pypi.org/project/requests/) for API calls
- [python-dotenv](https://pypi.org/project/python-dotenv/) for secure config
- [colorama](https://pypi.org/project/colorama/) for terminal color
- [NASA Open APIs](https://api.nasa.gov) - Astronomy Picture of the Day
- [Open Notify](http://open-notify.org/) - ISS location and astronaut data

## Setup

1. Clone this repo:

```
git clone https://github.com/YOUR-USERNAME/orbitview-dashboard.git
cd orbitview-dashboard
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Get a free API key from [api.nasa.gov](https://api.nasa.gov).

4. Create a .env file:

```
NASA_API_KEY=your_key_here
```

5. Run it:

```
python main.py
```

## Example

```
=== OrbitView: Astronomy Picture of the Day ===
Title: The Rho Ophiuchi Cloud Complex
Date:  2026-08-13
Image: https://apod.nasa.gov/apod/image/...

=== ISS Live Location ===
Latitude:  32.14
Longitude: -117.86
Status: 🛰️  The ISS is somewhere over the Northern Hemisphere, carrying 7 astronauts right now.

Recent Orbit Track (latitude):
2026-08-13  ############### 30.1°N
2026-08-13  ################ 32.1°N
```

## Possible future additions

- Map visualization of the ISS's path
- Notification when the ISS is visible overhead
- Archive of past APOD images
