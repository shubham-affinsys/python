import logging

"""
Constant 	    Numeric Value 	String Value
logging.DEBUG 	    10  	    DEBUG
logging.INFO 	    20   	    NFO
logging.WARNING 	30 	        WARNING
logging.ERROR 	    40 	        ERROR
logging.CRITICAL 	50      	CRITICAL
"""
"""

#configuration
# logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

#logging messages



#logginto a file
logging.basicConfig(
    level=logging.DEBUG,
    filename="app_logs.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
logging.debug("This isa debug msg")
logging.info("this is info msg")
logging.warning("thsi is a warnnig msg")
logging.error("this is an eror msg")
logging.critical("this is critical msg")

#display a variable data in log file
name="shubh"
logging.debug(f"{name=}")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("An exception occured",exc_info=True)
    #or
    logging.exception("An error occured in calculation")


"""

# instantiating own logger
"""
good practice to pass __name__ as paramter this way loggers name is always modules name in pyhton package namespace

cannot confgure instantiated logge using basicConfig() like root logger we need to use handlers
"""
logger = logging.getLogger(__name__)

logger.level
logger.parent
logger.setLevel(logging.DEBUG)


#handlers
console_handler  = logging.StreamHandler()
file_handler = logging.FileHandler("app_logs.log",mode="a",encoding="utf-8")

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

console_handler.setFormatter(formatter)
console_handler.setLevel("DEBUG")

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.handlers
logger.warning("This is my logger")
logger.error("there was an error")






##################
"""
Filtering Logs:
    There are three approaches to creating filters for logging. You can create a:

    Subclass of logging.Filter() and overwrite the .filter() method
    Class that contains a .filter() method
    Callable that resembles a .filter() method

"""

def show_only_debug(record):
    return record.levelname=="DEBUG"
console_handler.addFilter(show_only_debug)
