from logger import Logger

class B(object):

    def __init__(self):
        self.logger = Logger(__name__).get()

    def b_do_something(self):
        self.logger.info('b_do_something is executed')
