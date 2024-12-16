import logging

FORMAT = '%(asctime)s %(levelname)s [%(name)s] - %(message)s'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()  # Logger
logger_handler = logging.StreamHandler()
logger.addHandler(logger_handler)
logger_handler.setFormatter(logging.Formatter(FORMAT))