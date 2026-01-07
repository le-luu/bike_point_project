import requests
import os
from datetime import datetime
import json

# Documentation: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'

response = requests.get(url, timeout=10)

dir = "data"

if not os.path.exists(dir):
    os.mkdir(dir)

response_json = response.json()


filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filepath = f"{dir}/{filename}.json"

with open(filepath, 'w') as f:
    json.dump(response_json, f)

print(f"Download successful at {filepath}")

