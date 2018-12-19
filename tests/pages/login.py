from framework.webapp import webapp


class LoginPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()
        self.url = "tester-account/sign-in"
        self.email_input = "//input[@type='email']"
        self.password_input = "//input[@type='password']"
        self.submit = "//button[@type='submit']"
        self.login_err = "//div[@class='text-danger']"

    def type_email(self, txt):
        email = self.driver.find_element_by_xpath(self.email_input)
        email.send_keys(txt)

    def type_password(self, txt):
        pwd = self.driver.find_element_by_xpath(self.password_input)
        pwd.send_keys(txt)

    def click_login(self):
        submit = self.driver.find_element_by_xpath(self.submit)
        submit.click()

    def login_error_displayed(self):
        webapp.wait_for_element_to_appear(self.login_err)
        err = self.driver.find_element_by_xpath(self.login_err)
        assert err.is_displayed() is True
        webapp.wait_for_correct_current_url(self.url)


loginPage = LoginPage.get_instance()
