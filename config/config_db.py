import os

MONGO_URI = "mongodb+srv://lux:ZcIBx4ktzuGzBxrm@cluster0.idplqbh.mongodb.net/?appName=cluster0"
DB_NAME = "meteostation"
COLLECTION_NAME = "sensorData"
CONFIG_NAME = "config"
SECRET_KEY = b"BogdanNaziariiSimkoCharchok"

AUTHORIZED_TOKENS = {
    "MeteostationVereshchakToken": "station_01",
    "MeteostationToken_1": "station_02"
}

# Weather API configuration
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "8f247d140dbb80523456d52163dec69d")
WEATHER_LOCATION_LAT = float(os.getenv("WEATHER_LOCATION_LAT", "49.8815")) 
WEATHER_LOCATION_LON = float(os.getenv("WEATHER_LOCATION_LON", "24.0929"))