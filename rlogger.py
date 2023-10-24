import logging
from logging.handlers import RotatingFileHandler
import threading


class RLogger:
    def __init__(self, filename="app.log", log_level=logging.INFO, log_format=None, max_log_size=5, backup_count=3, log_to_console=True, context=None) -> None:
        self.handlers = []
        self.lock = threading.RLock()

        if log_format is None:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
        
        self.add_file_handler(filename, log_level, log_format, max_log_size, backup_count)
        
        if log_to_console:
            self.add_stream_handler(log_level, log_format)
        
        
        self.context = threading.local()
        self.context.data = context if context else {}


    def _configure_logger(self, log_level, log_format):
        logger = logging.getLogger("RLOGGER")
        logger.setLevel(log_level)

        for handler in self.handlers:
            handler.setFormatter(logging.Formatter(log_format))
            logger.addHandler(handler)
        
        return logger


    def add_file_handler(self, filename, max_log_size, backup_count):
        file_handler = RotatingFileHandler(filename, maxBytes=max_log_size * 1024 * 1024, backupCount=backup_count)
        self.handlers.append(file_handler)

    
    def add_stream_handler(self):
        stream_handler = logging.StreamHandler()
        self.handlers.append(stream_handler) 
    
    
    def log(self, level, message, status="INFO", data=None):
        with self.lock:
            logger = self._configure_logger(level, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            if data is None:
                data = {}
            data.update(self.context.data)

            log_message = { "log": { "STATUS": status, "DATA": data } }
            logger.log(level, message + ' ' + str(log_message))

    
    def info(self, message, data=None):
        self.log(logging.INFO, message, status="INFO", data=data)
    
    
    def success(self, message, data=None):
        self.log(logging.INFO, message, status="SUCCESS", data=data)

    
    def error(self, message, data=None, exc_info=False):
        self.log(logging.ERROR, message, status="ERROR", data=data)

        if exc_info:
            self.log(logging.ERROR, message, str(exc_info), status="ERROR")
    
    
    def warning(self, message, data=None):
        self.log(logging.WARNING, message, status="WARNING", data=data)

    
    def debug(self, message, data=None):
        self.log(logging.DEBUG, message, status="DEBUG", data=data)

    
    def update_context(self, new_context):
        self.context.data.update(new_context)


    def clear_context(self):
        self.context.data.clear()