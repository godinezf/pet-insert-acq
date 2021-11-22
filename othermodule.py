import time
import logging

logger = logging.getLogger(__name__)

def someProcess(self):
    logger.error("starting")
    for i in range(10):
        logger.error("line%d" % i)  # Every iteration, I want to display this line per line 
                                    # in the textbox on the main window
        time.sleep(2)    # in my own code, here comes a time consuming task 