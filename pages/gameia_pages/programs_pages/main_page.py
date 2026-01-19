from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_test_in_search_bar(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ابحث عن برنامج']"
        ).send_keys(text)

    def click_create_new_program(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='bg-metallic_seaweed text-white font-semibold rounded-lg px-6 py-2 ms-4']"
        ).click()

    def enter_name_of_program(self,name_of_program):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم البرنامج']"
        ).send_keys(name_of_program)

    def select_wallet(self,wallet):
        Select(self.wait_until_element_be_clickable(
            By.XPATH,
            "//select[@class='bg-transparent min-w-100 outline-none border-none focus:border-none focus:outline-none has-[option:disabled:checked]:text-gray-400 w-full h-10 px-2 ng-pristine ng-valid ng-touched']"
        )).select_by_value(wallet)

    def enter_start_date(self,path_of_year,path_of_month,path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='cdk-overlay-backdrop mat-overlay-transparent-backdrop mat-datepicker-2-backdrop cdk-overlay-backdrop-showing']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_year
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_month
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_day
        ).click()

    def enter_end_date(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='cdk-overlay-backdrop mat-overlay-transparent-backdrop mat-datepicker-2-backdrop cdk-overlay-backdrop-showing']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_year
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_month
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_day
        ).click()

    def enter_program_description(self,description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل وصف البرنامج']"
        ).send_keys(description)

    def enter_general_goal(self,general_goal):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل الهدف العام']"
        ).send_keys(general_goal)

    def click_add_new_result(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-metallic_seaweed text-white']"
        ).click()

    def enter_specific_goal(self,specific_goal):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل الهدف التفصيلى']"
        ).send_keys(specific_goal)

    def enter_perhaps(self,perhaps):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='w-full flex items-center justify-between border rounded-lg px-4 py-2 border-windsor_tan']//input[@placeholder='ادخل الافتراض']"
        ).send_keys(perhaps)

    def click_add_secondary_result(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-3 py-2 rounded-lg bg-windsor_tan']"
        ).click()

    def enter_secondary_result(self,secondary_result):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل النتيجة المرحلية']"
        ).send_keys(secondary_result)

    def enter_assumption(self,assumption):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='w-full flex items-center justify-between border rounded-lg px-4 py-2 mt-4 border-windsor_tan']//input[@placeholder='ادخل الافتراض']"
        ).send_keys(assumption)

    def click_add_out_come(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-3 py-1 rounded-lg bg-windsor_tan']"
        ).click()

    def enter_the_outcome(self,outcome):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل المخرج']"
        ).send_keys(outcome)

    def click_create(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-10 py-3 rounded-xl w-max flex items-center justify-start gap-2 font-semibold text-xl leading-7 tracking-wider disabled:opacity-50 disabled:cursor-not-allowed text-white bg-metallic_seaweed ng-star-inserted']"
        ).click()

