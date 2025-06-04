import os

MONGO_URI = "mongodb+srv://lux:ZcIBx4ktzuGzBxrm@cluster0.idplqbh.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"
DB_NAME = "meteostation"
COLLECTION_NAME = "sensorData"
CONFIG_NAME = "config"

# Weather API configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "8f247d140dbb80523456d52163dec69d")
WEATHER_LOCATION_LAT = float(os.getenv("WEATHER_LOCATION_LAT", "50.4501"))  # Kyiv coordinates
WEATHER_LOCATION_LON = float(os.getenv("WEATHER_LOCATION_LON", "30.5234"))