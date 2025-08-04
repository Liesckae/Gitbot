# 主控制模块import 
import logging
from logger import init_logger


class BotColtroller:
    def __init__(self):
        init_logger()
        logging.info("Controller is instantiated")
    def run(self):
        pass