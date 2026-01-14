import logging
import os
from datetime import datetime

def logging_function(filepath, timestamp):
    '''
    Docstring for logging_function
    
    :param prefix: For the folder of the logs
    :param timestamp: For the name of the logs
    '''
    
    # dir = f'{prefix}_logs'
    # os.makedirs(dir,exist_ok=True)
    filename = timestamp
    # file_path = os.path.join(os.getcwd(),prefix)
    log_filename = f"{filepath}/{filename}.log"
    
    print(log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        filename=log_filename
    )
    logger = logging.getLogger()

    return logger

def main():
    print("Current Dir:",os.getcwd())
    print(os.path.join(os.getcwd(),"extract_logs"))

if __name__=="__main__":
    main()