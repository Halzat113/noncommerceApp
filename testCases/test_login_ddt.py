import pytest

from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import get_project_root
from utilities.customLogger import LogGen


class Test_002_DDT_Login:
    path = get_project_root() + "\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************Test_002_DDT_Login******************")
        self.logger.info("******************Verifying Login DDT test******************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in the Excel = ", self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed **** ")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("**** Failed **** ")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("************Login DDT test passed*****************")
            assert True
        else:
            self.logger.info("***** Login DDT test failed")
            assert False

        self.driver.close()

        self.logger.info("*********** End of Login DDT Test **************")
        self.logger.info("*********** Completed TC_LoginDDT_002 **************")