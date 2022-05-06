import inspect
import pytest

import logging

class BaseLogClass:

    def LOGGINGdemo(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("logFile.log")

        form = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message))s :")

        fileHandler.setFormatter(form)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        # logger.debug("A debug statment")

        # logger.info("A info statement")

        # logger.warning("Something fishy")

        # logger.error("A error")

        # logger.critical("Something serious happedned")
        return logger
