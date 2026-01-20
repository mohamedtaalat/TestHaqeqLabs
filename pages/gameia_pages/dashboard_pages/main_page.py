from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_notifications(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full py-4 px-6 flex justify-between items-center']//button[1]"
        ).click()

    def click_settings(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full py-4 px-6 flex justify-between items-center']//button[2]"
        )
        self.scroll_to_element(element)
        element.click()

    def click_sign_out(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full py-4 px-6 flex justify-between items-center']//button[3]"
        ).click()