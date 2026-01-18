import time

from selenium.webdriver.common.by import By

from base.basis import Base
from pages.sign_in_pages.sign_in_form_page import SignInFormPage


class SecondSignInFormPage(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self,email):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@placeholder='ادخل اسم المستخدم']"
        ).send_keys(email)

    def enter_password(self,password):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@placeholder='ادخل كلمة المرور']"
        ).send_keys(password)

    def click_sign_as_employee(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@id='is_employee']"
        ).click()

    def click_sign_in(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def sign_in(self,email,password):
        sg = SignInFormPage(self.driver)
        sg.sign_in(email,password)
        time.sleep(1)
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in()

