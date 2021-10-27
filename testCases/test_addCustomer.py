import time

import pytest

from pageObjects.AddcustoerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.BrowserUtils import takeScreenshot
from utilities.DataUtils import generate_random_email, printingLetters
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_addCustomer(self, setup):
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
        self.email = generate_random_email()
        self.addCustomer.setEmail(self.email)
        self.password = printingLetters()
        self.addCustomer.setPassword(self.password)
        self.addCustomer.setFirstName("Abc")
        self.addCustomer.setLastnanme("Def")
        self.addCustomer.setGender("Male")
        self.addCustomer.setDateOfBirth(11, 3, 1996)
        self.addCustomer.setCompanyName("Yulup alar")
        self.addCustomer.setIsTaxExempt(True)
        self.addCustomer.setNewsletter("Your store name")
        self.addCustomer.setCustomerRoles("Vendors")
        self.addCustomer.setManagerOfVendor("Vendor 1")
        self.addCustomer.setAdminComment("blah balh balh")
        self.addCustomer.clickOnSaveBtn()
        if self.addCustomer.successfulMsgIsDisplayed and 'The new customer has been added successfully.' in self.addCustomer.newCustomerAddedSuccessfulMsg():
            assert True
            self.logger.info("***************Added customer Test Passed***************")
            self.driver.quit()
        else:
            takeScreenshot(self.driver, "test_addCustomer")
            self.logger.info("***************Added customer Test Failed!!!***************")
            self.driver.quit()
            assert False





