from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_text_in_search_bar(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ابحث...']"
        ).send_keys(text)

