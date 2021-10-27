class SearchCustomer:
    txtInput_xpath = "//input[@id='{}']"
    btnSearch_xpath = "//button[@id='search-customers']"
    tblSearchFor_xpath = "(//tr[@role='row'])[1]/th"
    tblSearchResult_xpath = "//tr[@class='odd']/td[{}]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtInput_xpath.format("SearchEmail")).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtInput_xpath.format("SearchFirstName")).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtInput_xpath.format("SearchLastName")).send_keys(lastname)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def findIndex(self, search):
        lst = self.driver.find_elements_by_xpath(self.tblSearchFor_xpath)
        for i, d in enumerate(lst):
            if d.text == search:
                return i+1

    def getResult(self, search):
        i = self.findIndex(search)
        return self.driver.find_element_by_xpath(self.tblSearchResult_xpath.format(i)).text



