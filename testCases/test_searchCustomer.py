import pytest

from pageObjects.AddcustoerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_004_SearchCustomer:
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomer(self, setup):
        self.driver = setup
        self.logger.info("******************Test_003_AddCustomer******************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.login()
        self.logger.info("******************Login successful******************")
        self.logger.info("******************Start Add Customer Test******************")
        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomersMenu()
        self.addCustomer.clickOnCustomersMenuItem()
        self.addCustomer.clickOnAddNew()
        self.logger.info("******************Providing customer info******************")
        self.addCustomer.fillUpUser()
        self.searchCustomer = SearchCustomer(self.driver)
        self.searchCustomer.setEmail(self.addCustomer.email)
        self.searchCustomer.clickOnSearch()
        if self.searchCustomer.getResult("Email") == self.addCustomer.email:
            assert True
        else:
            assert False
        self.driver.close()

