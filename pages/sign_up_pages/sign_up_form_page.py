import time

from selenium.webdriver.common.by import By

from base.basis import Base
from conftest import driver
from pages.land_pages.home_page import HomePage
from pages.sign_up_pages.choose_your_palace_page import ChooseYourPalacePage


class SignUpFormPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_name_of_gameia(self,name_of_gameia):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='اكتب اسم الجمعية']"
        ).send_keys(name_of_gameia)

    def enter_email(self,email):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل البريد الالكترونى']"
        ).send_keys(email)

    def enter_phone_number(self,phone_number):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='رقم الهاتف']"
        ).send_keys(phone_number)

    def enter_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@formcontrolname='password']"
        ).send_keys(password)

    def enter_confirm_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@class='input ng-untouched ng-pristine ng-valid']"
        ).send_keys(password)

    def click_accept_terms_and_conditions(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@type='checkbox']"
        ).click()

    def click_sign_up_button(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        )
        self.scroll_to_element(element)
        element.click()

    def setup(self):
        home_page = HomePage(self.driver)
        home_page.click_accept()
        self.driver.get("https://www.haqqeq-lab.com/auth/sign-up")
        cp = ChooseYourPalacePage(self.driver)
        cp.choose_gameia()
        cp.click_continue()

    def sign_up(self,name_of_gameia,email,phone_number,password,confirm_password):
        self.setup()
        self.enter_name_of_gameia(name_of_gameia)
        self.enter_email(email)
        self.enter_phone_number(phone_number)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_accept_terms_and_conditions()
        self.click_sign_up_button()

    def click_already_have_email_button(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@class='text-green-700 font-bold cursor-pointer']"
        )

    def catch_error_message(self):
        return self.wait_until_element_be_presence(
            By.XPATH,
            "//h2[@id='swal2-title']"
        )

