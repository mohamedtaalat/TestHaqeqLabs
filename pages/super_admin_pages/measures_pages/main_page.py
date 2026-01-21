from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def click_add_department(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@label='أضافة قسم']//button[@type='button']"
        ).click()

    def click_add_question(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@label='إضافة سؤال']//button[@type='button']"
        ).click()