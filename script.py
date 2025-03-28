import requests
import json
from datetime import datetime

# get current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
print("Current date & time : ", current_datetime)

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = str_current_datetime + ".txt"

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=51.75&longitude=1.26&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

response.text

jsondata = response.json()

# Serializing json
json_object = json.dumps(jsondata, indent=4)

# Writing to sample.json
with open(file_name, "w") as outfile:
    outfile.write(json_object)
