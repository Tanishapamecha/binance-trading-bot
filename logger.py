import logging

def setup_logger():
    logger = logging.getLogger("BinanceTradingBot")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    fh = logging.FileHandler('logs/bot.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
