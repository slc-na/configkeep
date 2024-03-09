import logging

class LogService:
    _instance = None

    def __new__(cls, name="configkeep", level=logging.INFO):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(name, level)
        return cls._instance

    def _init(self, name, level):
        self.log_file = 'config.log'
        self.file_handler = logging.FileHandler(self.log_file) 
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
