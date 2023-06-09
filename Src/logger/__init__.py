import logging
from datetime import datetime
import os


LOG_Dir='Logger File'

CURRENT_TIMESTAMP=f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

LOG_FILE_NAME=f"log_{CURRENT_TIMESTAMP}.log"

os.makedirs(LOG_Dir,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_Dir,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s',
                    level=logging.INFO
                    # level=logging.DEBUG
                    ) 

if __name__=="__main__":
    logging.info("logging has been Started and tested successful")