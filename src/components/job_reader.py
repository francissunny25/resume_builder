import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import html_to_json

import requests
from bs4 import BeautifulSoup
import json


class JobReaderConfig:
    job_path: str='artifacts/jobs/'

class JobReader:
    def __init__(self):
        self.job_config = JobReaderConfig

    # def read_linkedin_jobs(self, job_title, job_loc):
    def read_linkedin_jobs(self, job_title):
        try:
            logging.info(f'Reading jobs of title: {job_title} from Linkedin')
            url = f'https://www.linkedin.com/jobs/{job_title}-jobs?keywords=Qa%20Tester&location=United%20States&geoId=103644278&f_TPR=r604800&position=1&pageNum=0'
            response = requests.get(url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            json_content = json.dumps(html_to_json(soup), indent=4)
            return json_content
        except Exception as e:
            raise CustomException(e, sys)