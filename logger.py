import logging
from pathlib import Path


class Logger(object):
    def __init__(self, log_name: str):
        # Create a custom logger
        log_name_stem = Path(log_name).stem
        Path('logs').mkdir(exist_ok=True, parents=True)

        logger = logging.getLogger(log_name_stem)

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('logs/{}.log'.format(log_name_stem))
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.WARNING)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        logger.setLevel(logging.DEBUG)
        self.logger = logger

    def get(self):
        return self.logger