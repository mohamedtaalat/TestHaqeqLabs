from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_new_baqa(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='w-fit flex items-center justify-center gap-2 px-6 py-3 font-semibold text-xl leading-7 tracking-wide rounded-lg text-white bg-metallic_seaweed']"
        )
        self.scroll_to_element(element)
        element.click()

