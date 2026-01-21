from selenium.webdriver.common.by import By

from base.basis import Base


class AddDepartmentPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_name_of_department(self,name_of_department):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@role='dialog']//div[1]//input[1]"
        ).send_keys(name_of_department)

    def enter_precent_of_department(self,precent_of_department):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[2]//input[1]"
        ).send_keys(precent_of_department)

    def enter_type_of_department(self,type_of_department):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='ng-tns-c2196985156-84 p-dialog-content ng-star-inserted']//div[3]//input[1]"
        ).send_keys(type_of_department)

    def click_save(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'احفظ')]"
        ).click()

    def click_close(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-ripple p-button p-component p-button-secondary']"
        ).click()
