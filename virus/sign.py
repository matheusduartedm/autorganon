import hashlib
import logging
import sys
from datetime import datetime
from typing import Tuple
import requests

SERVER_URL = "http://hannover.local.psrservices.net:5000"


formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

logger = logging.getLogger('general')
logger.setLevel(logging.DEBUG)

# Create a stream handler to log to standard output
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def _calculate_md5(file_path: str) -> str:
    with open(file_path, 'rb') as file_hdr:
        md5_hash = hashlib.md5()
        chunk = file_hdr.read(4096)
        while chunk:
            md5_hash.update(chunk)
            chunk = file_hdr.read(4096)
    return md5_hash.hexdigest()


def sign_file(filename: str) -> bool:
    """Sends the file to the server to be signed. If the file is already signed, it is downloaded from the server."""
    cached, cached_filename = check_file(filename)
    available = False
    if not cached:
        available, cached_filename = upload_file(filename)
    else:
        available = True

    if available:
        download_file(filename, cached_filename)
        return True
    return False


def check_file(filename: str) -> Tuple[bool, str]:
    """Returns True if the file is cached on the server and the cached file name, False otherwise. """
    logger.info(f'Checking for cached signed file: {filename}.')
    file_hash = _calculate_md5(filename)
    url = f"{SERVER_URL}/check/{file_hash}"
    response = requests.get(url)
    if response.status_code == 200:
        response_obj = response.json()
        if response_obj.get('filename') is not None:
            cached_filename = response_obj['filename']
            logger.info(f'File is cached as: {cached_filename}.')
            return True, cached_filename
    return False, ""


def upload_file(filename: str) -> Tuple[bool, str]:
    """Uploads the file to the server and returns True if the upload was successful and the cached file name, False otherwise."""
    upload_start_time = datetime.now()
    url = f'{SERVER_URL}/upload'
    logger.info(f'File upload started: {filename}.')
    with open(filename, 'rb') as file:
        response = requests.post(url, files={'file': file})

    if response.status_code == 200:
        upload_elapsed_time = calculate_elapsed_time(upload_start_time)
        logger.info(f'File uploaded successfully: {filename}. Elapsed time: {upload_elapsed_time}')
        return True, response.json()['filename']
    else:
        logger.info('File upload failed. Response:')
        logger.info(response.status_code)
        logger.info(response.content)
        return False, ""


def download_file(original_file_path: str, server_filename: str) -> Tuple[bool, str]:
    """Downloads the file from the server and returns True if the download was successful and the signed local file name, False otherwise."""
    download_start_time = datetime.now()
    url = f'{SERVER_URL}/download/{server_filename}'
    logger.info(f'File download started: {url}')
    response = requests.get(url)

    if response.status_code == 200:
        with open(f'{original_file_path}', 'wb') as file:
            file.write(response.content)
        download_elapsed_time = calculate_elapsed_time(download_start_time)
        logger.info(f'File downloaded successfully: {original_file_path}. Elapsed time: {download_elapsed_time}')
        return True, original_file_path
    else:
        logger.info(f'File download failed ({original_file_path}). Response:')
        logger.info(response.status_code)
        logger.info(response.content)
        return False, ""


def calculate_elapsed_time(start_time: datetime) -> str:
    """Calculate the elapsed time of a process given its start time, and format to string XXhXXmXXs"""
    finish_time = datetime.now()
    elapsed = finish_time - start_time
    hours, seconds = divmod(elapsed.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f'{hours}h{minutes}m{seconds}s'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide the file path as an argument.')
        sys.exit(1)
    
    file_path = sys.argv[1]
    sign_file(file_path)
