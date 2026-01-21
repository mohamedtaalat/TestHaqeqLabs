from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_new_video(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-ripple p-button p-component p-button-secondary']"
        ).click()