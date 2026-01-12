import requests
import os
from datetime import datetime
import json
import time
import logging

# Documentation: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk/BikePoint'
filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
dir = "data"
logs_dir = "logs"

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)

log_filename = f"logs/logging_example_{filename}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=log_filename
)
logger = logging.getLogger()

number_of_retries = 3
count = 0

while count< number_of_retries:
    response = requests.get(url, timeout=10)
    response_code = response.status_code

    if response_code == 200:

        if not os.path.exists(dir):
            os.mkdir(dir)

        response_json = response.json()

        
        filepath = f"{dir}/{filename}.json"
        try:
            with open(filepath, 'w') as f:
                json.dump(response_json, f)
            print(f"Download successful at {filename}")
            logger.info(f"Download successful at {filename}")
        except Exception as e:
            print(f"Error writing file: {e}")
            logger.error(f"Error writing file: {e}")
       
        break

    elif response_code > 499 or response_code < 200:
        print(response.reason)
        logger.warning(response.reason)
        time.sleep(10)
        count += 1
    else:
        print(response.reason)
        logger.error(response.reason)
        break