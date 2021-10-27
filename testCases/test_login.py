import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import get_project_root
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    username = ReadConfig.getApplicationCredential("username")
    password = ReadConfig.getApplicationCredential("password")
    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******************Test_001_Login******************")
        self.logger.info("******************Verifying Home Page Title******************")
        self.driver = setup
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************Home page title test is passed******************")
        else:
            self.driver.save_screenshot(get_project_root() + "\\Screenshots\\test_homepageTitle.png")
            self.driver.close()
            self.logger.error("******************Home page title test is failed******************")
            assert False

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************Verifying Login Title******************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        try:
            self.driver.switch_to.alert.dismiss()
        except:
            pass

        act_title = self.driver.title
        try:
            assert act_title == "Dashboard / nopCommerce administration", "Different value!!"
            self.driver.close()
            self.logger.info("******************Login test is passed******************")
        except:
            self.logger.error("******************Login test is failed******************")
            self.driver.close()
            assert False


