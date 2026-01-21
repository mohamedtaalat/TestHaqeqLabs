from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def click_activate(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()

    def click_deactivate(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()
