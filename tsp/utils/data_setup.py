import os
import kagglehub
from google.cloud import storage
from tsp.config.logger import get_logger
from tsp.config.config import Config
from google.api_core.exceptions import NotFound
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

logger = get_logger(__name__)



def download_data():
    path = kagglehub.dataset_download("heptapod/titanic")
    file_name = os.listdir(path)[0]
    file_path = os.path.join(path, file_name)
    logger.info(f"File downloaded to: {file_path}")
    return file_path


def upload_data(file_path):
    """
    Uploads the file to the configured bucket.
    This function should be implemented based on your cloud provider's SDK.
    """
    try:
        client = storage.Client()
        bucket = client.bucket(Config.BUCKET_NAME)
        file_name = "data.csv"
        blob = bucket.blob("raw/" + file_name)

        if blob.exists():
            logger.warning(f"Blob {file_name} already exists in bucket {Config.BUCKET_NAME}. Skipping upload.")
        else:
            logger.info(f"Blob {file_name} does not exist in bucket {Config.BUCKET_NAME}. Uploading new file.")
            blob.upload_from_filename(file_path)
            logger.info(f"File {file_path} uploaded to bucket {Config.BUCKET_NAME}.")
    except NotFound:
        logger.error(f"Bucket {Config.BUCKET_NAME} not found. Please check your configuration.")
    except Exception as e:
        logger.error(f"An error occurred while uploading the file: {e}")
        raise
