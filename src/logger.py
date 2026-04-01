import logging
import os
from datetime import datetime
import sys

LOF_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

#path for log file
logs_path=os.path.join(os.path.dirname(__file__), '..', 'logs', LOF_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOF_FILE)

#overrite the logging functionality to log the message in log file
#this is used for logging the messages in log file, it will create a log file with the name of the current date and time and log the messages in that file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    #timestamp, name of the logger, level of the log message and the message
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    #this is for the log level, it will log all the messages which are above or equal to the log level
    level=logging.INFO
)


#creates log files in logs folder with asccensding time line name level and message 
if __name__=="__main__":
    logging.info('Logging has started')
  


