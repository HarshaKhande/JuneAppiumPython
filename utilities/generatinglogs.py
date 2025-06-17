import logging

def log():
    logging.basicConfig(filename="..\\Logs\\logfile.log",
                        format='%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger()
    logger.info("This is our first log")
    return logger


logger = log()
logger.info("This is the new log")
logger.error("This is a error message")