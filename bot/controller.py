# 主控制模块
import logging
from logger import init_logger
import commands


class BotColtroller:
    def __init__(self):
        init_logger()
        logging.info("Controller start instantiating")
        self.commands = {
            "status":self.run("status")
        }
        logging.info("Controller is instantiated")
    def run(self,command):
        pass