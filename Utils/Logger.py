import logging, os, time, pathlib
from datetime import datetime

def setUP_Logger():
    timestamp = datetime.now().strftime('%Y%m%d%H%S%f')
    log_dir = os.path.join(os.getcwd(),'Reports',f'{timestamp}')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir,'test.log')

    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    return logger