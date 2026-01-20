from selenium.webdriver.common.by import By

from base.basis import Base


class SignInFormPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def enter_email(self,email):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='email1']"
        ).send_keys(email)

    def enter_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='Password']"
        ).send_keys(password)

    def click_login(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-ripple p-button p-component w-full']"
        ).click()

    def sign_in(self,email,password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()