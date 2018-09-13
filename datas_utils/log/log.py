import logging

LOG_FORMAT = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'

def get_logger(name, loglevel="INFO", logformat=LOG_FORMAT):
    '''
    logger = log.load(__name__)

    logger.debug("HOGE")
    '''
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    logger.setLevel(getattr(logging, loglevel))
    handler.setLevel(getattr(logging, loglevel))
    formatter = logging.Formatter(logformat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
