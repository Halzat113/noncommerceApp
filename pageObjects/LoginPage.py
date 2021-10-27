from utilities.readProperties import ReadConfig


class LoginPage:
    username_id = "Email"
    password_id = "Password"
    button_login_xpath = "//button[.='Log in']"
    button_logout_xpath = "//a[.='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def login(self):
        username = ReadConfig.getApplicationCredential("username")
        password = ReadConfig.getApplicationCredential("password")
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()
