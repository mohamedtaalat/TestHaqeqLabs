from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_text_in_search_bar(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='w-1/3 border border-spanish_gray rounded-lg flex items-center justify-start']//input[@placeholder='ابحث...']"
        ).send_keys(text)

    def select_topic(self,topic):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//select[@class='cursor-pointer min-w-100 border-none outline-none focus:outline-none focus:border-none']"
            )
        ).select_by_value(
            topic
        )

    def select_book(self,path_of_book):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_book
        ).click()

    def select_video(self,path_of_video):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_video
        ).click()