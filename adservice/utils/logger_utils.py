import logging

log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])


# https://gist.github.com/huklee/cea20761dd05da7c39120084f52fcc7c
class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonLogger(object, metaclass=SingletonType):

    def __init__(self):
        print("Generating new Logger instance")
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        return self._logger


def get_logger():
    return SingletonLogger.__call__().get_logger()


if __name__ == '__main__':
    logger = get_logger()
    logger.info("Logger Initialised")