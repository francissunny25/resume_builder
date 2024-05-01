from src.logger import logging
from src.components.job_reader import JobReader

if __name__ == "__main__":
    job_title = 'Data Analyst'
    job_location = ''
    logging.info("Collecting data from the user")
    job_reader = JobReader(job_title)