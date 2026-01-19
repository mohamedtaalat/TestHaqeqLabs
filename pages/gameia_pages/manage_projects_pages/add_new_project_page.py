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
       Select(
                self.wait_until_element_be_visible(
                  By.XPATH,
                 "//body//app-root//div[@dir='rtl']//div//div//div//div//div//div[2]//div[1]//select[1]"
                 )
        ).select_by_value(status_of_project)

    def select_status_of_donates(self,status_of_donates):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//body//app-root//div[@dir='rtl']//div//div//div[3]//div[1]//select[1]"
            )
        ).select_by_value(status_of_donates)

    def select_wallet(self,wallet):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//div[4]//div[1]//select[1]"
            )
        ).select_by_value(wallet)

    def select_name_of_program(self,name_of_program):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//div[5]//div[1]//select[1]"
            )
        ).select_by_value(name_of_program)

    def enter_start_date(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'ادخل تاريخ بدء المشروع')]"
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
            "//span[contains(text(),'ادخل تاريخ انتهاء المشروع')]"
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

    def enter_maiznet_the_project(self,maiznet_of_project):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ميزانية المشروع']"
        ).send_keys(maiznet_of_project)

    def enter_the_name_owner_gaha(self,name_of_owner):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='أدخل اسم الجهة المالكة للمشروع']"
        ).send_keys(name_of_owner)

    def enter_the_name_of_the_gaha_donates(self,name_of_the_gaha_donates):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='أدخل اسم الجهة الممولة للمشروع']"
        ).send_keys(name_of_the_gaha_donates)

    def enter_the_name_of_the_gaha_will_make_the_project\
                    (self,name_of_the_gaha_will_make_the_project):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='أدخل اسم الجهة المنفذة للمشروع']"
        ).send_keys()

    def select_the_type_of_project(self,type_of_project):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//div[12]//div[1]//select[1]"
            )
        ).select_by_value(type_of_project)

    def select_the_location(self,location):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//select[@class='bg-transparent min-w-100 outline-none border-none focus:border-none focus:outline-none has-[option:disabled:checked]:text-gray-400 w-full h-10 px-2 ng-untouched ng-pristine ng-valid']"
            )
        ).select_by_value(location)

    def enter_the_number_of_stakeholders(self,number_of_stakeholders):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل عدد المستفيدين']"
        ).send_keys(number_of_stakeholders)

    def enter_target_feat(self,target_feat):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='ql-editor ql-blank']"
        ).send_keys(target_feat)

    def enter_the_project_description(self,project_description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل وصف المشروع']"
        ).send_keys(project_description)

    def click_create(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-10 py-3 rounded-xl w-max flex items-center justify-start gap-2 font-semibold text-xl leading-7 tracking-wider disabled:opacity-50 disabled:cursor-not-allowed text-white bg-metallic_seaweed']"
        ).click()


