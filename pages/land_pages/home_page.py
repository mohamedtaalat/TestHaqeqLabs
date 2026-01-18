import time

from selenium.webdriver.common.by import By

from base.basis import Base


class HomePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_sign_in(self):

        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='bg-login_btn_bg text-white flex items-center rounded-lg px-4 py-2 font-normal']"
        ).click()

    def click_accept(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            " //hakek-cookie-banner//button[normalize-space()='موافق']"
        ).click()

