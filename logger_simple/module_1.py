from logger_simple.logging_module import logger
from module_2 import Module2


def hello_logger():
    logger.info("Hello info")
    logger.critical("Hello critical")
    logger.warning("Hello warning")
    logger.debug("Hello debug")


if __name__ == "__main__":
    Module2()
    hello_logger()
    # while True:
    #     hello_logger()
    #     time.sleep(0.001)
