from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_new_news(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@class='min-w-max']//button[@type='button']"
        ).click()

    