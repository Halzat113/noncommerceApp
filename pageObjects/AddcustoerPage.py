import random

from selenium.webdriver.support.ui import Select
import names

from utilities.DataUtils import generate_random_email, printingLetters, getGender, getDob, getNewsletter, \
    get_one_random_name, letters


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@class='nav-link' and @href='#']/p[contains(.,'Customers')]/.."
    linkCustomers_menuitem_xpath = "//ul[@class='nav nav-treeview' and contains(@style,'display')]//p[.=' Customers']"
    btnAddNew_xpath = "//a[@class='btn btn-primary' and contains(.,'Add new')]"
    inputs_xpath = "//*[@id='{}']"
    txtNewsletter = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/.."
    drdNewsletter = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[.='{}']"
    txtCustomersRole = "//ul[@id='SelectedCustomerRoleIds_taglist']/.."
    txtCustomerRolesSelected = "//li[@class='k-button']/span[.='{}']/following-sibling::span"
    drdCustomerRoles = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[.='{}']"
    drpVendor = "//select[@id='VendorId']"
    btnSave = "//button[@name='save']"
    msgAddNew = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver
        self.email = generate_random_email()

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("Email")).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("Password")).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("FirstName")).send_keys(firstname)

    def setLastnanme(self, lastname):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("LastName")).send_keys(lastname)

    def setGender(self, gender):
        if str(gender).upper() == 'MALE':
            self.driver.find_element_by_xpath(self.inputs_xpath.format("Gender_Male")).click()
        elif str(gender).upper() == "FEMALE":
            self.driver.find_element_by_xpath(self.inputs_xpath.format("Gender_Female")).click()
        else:
            raise AssertionError("Please select only male or female")

    '''
        if arguments are empty this function will set random DOB 
    '''

    def setDateOfBirth(self, month=None, day=None, year=None):
        if month is not None and day is not None and year is not None:
            dob = f'{month}/{day},{year}'
            self.driver.find_element_by_xpath(self.inputs_xpath.format("DateOfBirth")).send_keys(dob)
        elif month is None or day is None or year is None:
            self.driver.find_element_by_xpath(self.inputs_xpath.format("DateOfBirth")).send_keys(getDob())

    def setCompanyName(self, companyName):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("Company")).send_keys(companyName)

    def setIsTaxExempt(self, isTaxExept):
        if isTaxExept:
            self.driver.find_element_by_xpath(self.inputs_xpath.format("IsTaxExempt")).click()

    def setNewsletter(self, txt):
        self.driver.find_element_by_xpath(self.txtNewsletter).click()
        element = self.driver.find_element_by_xpath(self.drdNewsletter.format(txt))
        self.driver.execute_script("arguments[0].click();", element)

    def setCustomerRoles(self, role):
        if role == "Guests":
            self.driver.find_element_by_xpath(self.txtCustomerRolesSelected.format("Registered")).click()
            self.driver.find_element_by_xpath(self.txtCustomersRole).click()
            element = self.driver.find_element_by_xpath(self.drdCustomerRoles.format(role))
            self.driver.execute_script("arguments[0].click();", element)
        else:
            self.driver.find_element_by_xpath(self.txtCustomersRole).click()
            element = self.driver.find_element_by_xpath(self.drdCustomerRoles.format(role))

        self.driver.execute_script("arguments[0].click();", element)

    def setManagerOfVendor(self, txt):
        vendor = Select(self.driver.find_element_by_xpath(self.drpVendor))
        vendor.select_by_visible_text(txt)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.inputs_xpath.format("AdminComment")).send_keys(comment)

    def clickOnSaveBtn(self):
        self.driver.find_element_by_xpath(self.btnSave).click()

    def newCustomerAddedSuccessfulMsg(self):
        return self.driver.find_element_by_xpath(self.msgAddNew).text

    def successfulMsgIsDisplayed(self):
        return self.driver.find_element_by_xpath(self.msgAddNew).is_displayed()

    def fillUpUser(self):
        self.setEmail(self.email)
        password = printingLetters()
        self.setPassword(password)
        self.setFirstName(names.get_first_name())
        self.setLastnanme(names.get_last_name())
        self.setGender(getGender())
        self.setDateOfBirth()
        self.setCompanyName(printingLetters())
        self.setIsTaxExempt(bool(random.getrandbits(1)))
        self.setNewsletter(getNewsletter())
        self.setManagerOfVendor("Vendor 1")
        self.setAdminComment(get_one_random_name(letters))
        self.clickOnSaveBtn()

