from logger import Logger

class A(object):

    def __init__(self):
        self.logger = Logger(__name__).get()

    def a_do_something(self):
        self.logger.info('a_do_something is executed')
