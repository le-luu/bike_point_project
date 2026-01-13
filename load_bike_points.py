import boto3
from dotenv import load_dotenv
import os
import logging

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")  

logs_dir = "logs"

filepath = "data/2026-01-07_15-29-03.json"

log_filename = f"logs/logging_example_2026-01-07_15-29-03.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=log_filename
)
logger = logging.getLogger()

print(AWS_BUCKET_NAME)

s3_client = boto3.client('s3', 
                         aws_access_key_id=AWS_ACCESS_KEY, 
                         aws_secret_access_key=AWS_SECRET_KEY
)

# s3_filename = "2026-01-07_15-29-03.json"
# s3_client.upload_file(filepath, AWS_BUCKET_NAME, s3_filename)


Current_file_path = os.getcwd()
print("Current Directory:",os.getcwd())

data_path = os.path.join(Current_file_path, 'data')

for (root,dirs,files) in os.walk(data_path,topdown=True):
    print("Root:",root)
    for file in files:
        if len(files)>0 and file.endswith('.json'):
            try:
                s3_client.upload_file(os.path.join(root,file), AWS_BUCKET_NAME, file)
                os.remove(os.path.join(root,file))
                print(f"Uploaded {file} to S3 bucket {AWS_BUCKET_NAME} and Removed {file} in local successfully.")
                logger.info(f"Uploaded {file} to S3 bucket {AWS_BUCKET_NAME} and Removed {file} in local successfully.")
            except Exception as e:
                print(f"Failed to upload {file}. Error: {e}")
                logger.error(f"Failed to upload {file}. Error: {e}")
        else:
            print("There are no JSON files to upload.")
            logger.warning("There are no JSON files to upload.")
