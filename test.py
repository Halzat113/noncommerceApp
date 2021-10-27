from utilities.customLogger import LogGen


class Test_001_Login:
    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.logger.info("******************Test_001_Login******************")
        self.logger.info("******************Verifying Home Page Title******************")
