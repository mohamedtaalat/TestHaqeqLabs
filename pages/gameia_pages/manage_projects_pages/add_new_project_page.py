from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.basis import Base


class AddNewProjectPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_name_of_project(self,name_of_project):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم المشروع']"
        ).send_keys(name_of_project)

    def select_status_of_project(self,status_of_project):
        i = 0
        if status_of_project == "Completed":
            i = 1
        elif status_of_project == "In Progress":
            i = 2
        elif status_of_project == "Delayed":
            i = 3

        Select(
                self.wait_until_element_be_visible(
                  By.XPATH,
                 "//body//app-root//div[@dir='rtl']//div//div//div//div//div//div[2]//div[1]//select[1]"
                 )
        ).select_by_index(i)

    def select_status_of_donates(self,status_of_donates):
        i = 0
        if status_of_donates == "Completed":
            i = 4
        elif status_of_donates == "Waiting":
            i = 2
        elif status_of_donates == "Not":
            i = 1
        elif status_of_donates == "Part":
            i = 3
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//body//app-root//div[@dir='rtl']//div//div//div[3]//div[1]//select[1]"
            )
        ).select_by_index(i)



