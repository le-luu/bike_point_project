import requests
import os
import json
import time

def extract_function(url, number_of_retries, logger, timestamp):
    '''
    Designed for extracting data from bike point API
    
    :param url: Description
    :param number_of_tries: Description
    :param logger: Description
    :param timestamp: Description
    '''
    count = 0

    while count< number_of_retries:
        response = requests.get(url, timeout=10)
        response_code = response.status_code

        dir = 'data'
        if response_code == 200:
            
            os.makedirs(dir,exist_ok=True)

            response_json = response.json()

            filepath = f"{dir}/{timestamp}.json"
            try:
                with open(filepath, 'w') as f:
                    json.dump(response_json, f)
                print(f"Download successful at {timestamp}")
                logger.info(f"Download successful at {timestamp}")
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
