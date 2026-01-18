from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.basis import Base
from pages.land_pages.home_page import HomePage


class SignInFormPage(Base):

    def __init__(self, driver):
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
        "// input[ @ placeholder = 'ادخل كلمة المرور']"
        ).send_keys(password)

    def select_sign_in_type(self,path):
        self.wait_until_element_be_presence(
            By.XPATH,
            path
        ).click()

    def click_sign_in_button(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def sign_in(self,email,password):
        hp = HomePage(self.driver)
        hp.click_accept()
        hp.click_sign_in()
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_button()

    def click_sign_up_button(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@class='text-login_btn_bg font-medium text-sm leading-6 tracking-normal no-underline pb-1 border-b-2 border-login_btn_bg cursor-pointer']"
        )
        self.scroll_to_element(element)
        element.click()

    def catch_error_message(self):
        try:
           return self.wait_until_element_be_presence(
                By.XPATH,
                "//h2[@id='swal2-title']"
            )
        except TimeoutException:
            return None

