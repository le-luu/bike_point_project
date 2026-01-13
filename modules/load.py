import boto3
import os
from datetime import datetime
from modules.logging import logging_function

def load_function(data_dir, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, logger):

    s3_client = boto3.client('s3', 
                         aws_access_key_id=AWS_ACCESS_KEY, 
                         aws_secret_access_key=AWS_SECRET_KEY
    )
    for (root,_,files) in os.walk(data_dir,topdown=True):
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

def main():
    Current_file_path = os.getcwd()
    data_path = os.path.join(Current_file_path, 'data')

    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME") 

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    load_logger = logging_function("load", timestamp)
    load_function(data_path,AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_BUCKET_NAME, load_logger)

if __name__ == "__main__":
    main()
