from modules.logging import logging_function
from modules.extract import extract_function
from modules.load import load_function
from datetime import datetime
from dotenv import load_dotenv
import boto3
import os

def main():
    load_dotenv()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    url = 'https://api.tfl.gov.uk/BikePoint'

    # extract_logs=os.makedirs("extract_logs",exist_ok=True)
    # extract_logs_dir = os.path.join(os.getcwd(),extract_logs)
    extract_logger = logging_function("extract", timestamp)

    extract_function(url, 3, extract_logger, timestamp)

    Current_file_path = os.getcwd()
    data_path = os.path.join(Current_file_path, 'data')

    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME") 

    # print("Current dir: ",os.getcwd())
    # load_logs=os.makedirs("load_logs",exist_ok=True)
    # load_logs_dir = os.path.join(os.getcwd(),load_logs)
    load_logger = logging_function("load", timestamp)
    load_function(data_path,AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_BUCKET_NAME, load_logger)

if __name__=="__main__":
    main()