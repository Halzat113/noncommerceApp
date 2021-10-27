import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\halza\\PycharmProjects\\noncommerceApp\\Log\\test.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            force=True
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# logger = LogGen.loggen()
# logger.info("This is info")