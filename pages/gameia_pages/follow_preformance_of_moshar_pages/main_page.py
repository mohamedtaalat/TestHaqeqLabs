from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def select_project(self,project):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//select[@class='cursor-pointer min-w-100 border-none outline-none focus:outline-none bg-transparent appearance-none pr-8 text-metallic_seaweed ng-pristine ng-valid ng-touched']"
            )
        ).select_by_value(project)