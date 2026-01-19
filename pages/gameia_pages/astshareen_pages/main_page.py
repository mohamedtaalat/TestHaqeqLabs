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
            "//input[@class='bg-transparent outline-none w-full h-10 px-2 ng-untouched ng-pristine ng-valid']"
        ).send_keys(text)

    def select_number_of_experience_year(self,number_of_experience_year):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//select[@class='bg-transparent cursor-pointer min-w-100 border-none outline-none focus:outline-none focus:border-none']"
            )
        ).select_by_value(number_of_experience_year)

    def select_company(self,path_of_company):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_company
        ).click()