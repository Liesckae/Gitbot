# 日志模块
import logging

def init_logger():
    '''初始化日志'''
    logging.basicConfig(
        filename="data/log/bot.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )