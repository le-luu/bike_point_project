import logging
import os
from datetime import datetime

def logging_function(prefix, timestamp):
    '''
    Docstring for logging_function
    
    :param prefix: For the folder of the logs
    :param timestamp: For the name of the logs
    '''
    
    dir = f'{prefix}_logs'
    os.makedirs(dir,exist_ok=True)
    filename = timestamp

    log_filename = f"{dir}/{filename}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        filename=log_filename
    )
    logger = logging.getLogger()

    return logger

