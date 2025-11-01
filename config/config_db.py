import os, json
from dotenv import load_dotenv
load_dotenv("secrets.env")

MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = "meteostation"
COLLECTION_NAME = "sensorData"
CONFIG_NAME = "config"
SECRET_KEY = os.getenv("SECRET_KEY", "").encode()

AUTHORIZED_TOKENS = json.loads(os.getenv("AUTHORIZED_TOKENS", "{}"))

# Weather API configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
WEATHER_LOCATION_LAT = float(os.getenv("WEATHER_LOCATION_LAT", "49.8815")) 
WEATHER_LOCATION_LON = float(os.getenv("WEATHER_LOCATION_LON", "24.0929"))