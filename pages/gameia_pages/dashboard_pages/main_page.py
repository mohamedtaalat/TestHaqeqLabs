from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_notifications(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='svg/notification.svg']//*[name()='svg']"
        ).click()

    def click_settings(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='svg/settings.svg']//*[name()='svg']"
        ).click()

    def click_sign_out(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='svg/logout.svg']//*[name()='svg']"
        ).click()