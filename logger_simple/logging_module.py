import logging
from logging.handlers import RotatingFileHandler

import sys

_log_file_path = 'logger_simple.log'
_max_mega_bytes = 10
_backup_count = 5

logger = logging.getLogger('main_logger')
logger.setLevel(logging.DEBUG)
fh = RotatingFileHandler(_log_file_path, maxBytes=_max_mega_bytes*1024*1024, backupCount=_backup_count)
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] [%(filename)s.%(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                              datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)
