import logging

def get_logger(name, loglevel="INFO"):
    '''
    logger = log.load(__name__)

    logger.debug("HOGE")
    '''
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setLevel(getattr(logging, loglevel))
    logger.setLevel(getattr(logging, loglevel))
    logger.addHandler(handler)
    return logger
