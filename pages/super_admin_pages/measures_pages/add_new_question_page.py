from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewQuestionPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_department_of_question(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()

    def enter_question_name(self,question_name):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='flex items-center gap-4 mb-8 ng-tns-c2196985156-85']//input[@id='email']"
        ).send_keys(question_name)

    def select_type_of_question(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@aria-label='حدد نوع السؤال']"
        ).click()

        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()

    def enter_answer(self,answer):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='flex items-start gap-4 mb-8 ng-tns-c2196985156-85']//input[1]"
        ).send_keys(answer)

    def enter_precent(self,precent):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//body//app-root//input[2]"
        ).send_keys(precent)

    def click_add(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'اضافة')]"
        ).click()

    def click_save(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-ripple p-button p-component']"
        ).click()
