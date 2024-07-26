import logging

"""
Constant 	    Numeric Value 	String Value
logging.DEBUG 	    10  	    DEBUG
logging.INFO 	    20   	    NFO
logging.WARNING 	30 	        WARNING
logging.ERROR 	    40 	        ERROR
logging.CRITICAL 	50      	CRITICAL
"""


#configuration
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

#logging messages

logging.debug("This isa debug msg")
logging.info("this is info msg")
logging.warning("thsi is a warnnig msg")
logging.error("this is an eror msg")
logging.critical("this is critical msg")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("An exception occured",exc_info=True)
