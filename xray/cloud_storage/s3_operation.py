import subprocess
import sys
import os
from xray.excep.exception import xrayexception
import logging

class s3operation:
    def sync_folder_to_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        try:
            command = [
                "aws",
                "s3",
                "sync",
                folder,
                f"s3://{bucket_name}/{bucket_folder_name}"
            ]
            subprocess.run(command, check=True)
            logging.info(f"Synced local folder '{folder}' to S3://{bucket_name}/{bucket_folder_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error syncing folder to S3: {e}")
            raise xrayexception(e, sys)

    def sync_folder_from_s3(self, folder: str, bucket_name: str, bucket_folder_name: str) -> None:
        try:
            command = [
                "aws",
                "s3",
                "sync",
                f"s3://{bucket_name}/{bucket_folder_name}/{folder}",
                folder
            ]
            subprocess.run(command, check=True)
            logging.info(f"Synced S3://{bucket_name}/{bucket_folder_name}/{folder} to local folder '{folder}'")
            
            # Add logging to list the contents of the local folder after syncing
            local_folder_contents = os.listdir(folder)
            logging.info(f"Local folder contents after syncing: {local_folder_contents}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error syncing folder from S3: {e}")
            raise xrayexception(e, sys)


