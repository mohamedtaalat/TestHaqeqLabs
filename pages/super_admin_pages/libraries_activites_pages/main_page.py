from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_name_of_activity(self,name_of_activity):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='اضافة نشاط']"
        ).send_keys(name_of_activity)

    def click_add(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def click_delete(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()

    def click_edit(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()
