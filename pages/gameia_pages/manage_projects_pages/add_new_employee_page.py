from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewEmployeePage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_new_employee_name(self,new_employee_name):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم المشروع']"
        ).send_keys(new_employee_name)

    def select_employee_access(self,new_employee_access):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//button[@class='flex justify-between items-center w-full px-4 py-2 text-left border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-metallic_seaweed bg-bright_gray']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-add-employee/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='bg-bright_gray p-10']/div[@class='w-full p-8 rounded-xl bg-white']/div[@class='w-full flex flex-col items-start gap-10']/div[@class='flex items-stretch justify-start gap-5 w-full']/div[@class='w-[30.5rem] min-w-[30.5rem]']/haqeq-multi-select[@placeholder='اختر صلاحية الموظف']/div[@class='relative inline-block w-full']/div[@class='absolute z-10 w-full mt-1 bg-white border border-gray-300 rounded-md shadow-lg']/div[@class='py-1 overflow-auto max-h-60']/div[1]"
        ).click()

    def enter_the_department(self,the_department):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل قسم الخاص بالموظف']"
        ).send_keys(the_department)

    def enter_the_date(self,path_of_year,path_of_month,path_of_day):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//span[@class='font-semibold leading-none tracking-normal text-right text-gray-400']"
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

    def enter_email(self,email):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل البريد الألكتروني']"
        ).send_keys(email)

    def enter_password(self,password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[6]//input[1]"
        ).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[7]//input[1]"
        ).send_keys(confirm_password)

    def enter_phone_number(self,phone_number):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل رقم الجوال']"
        ).send_keys(phone_number)

    def click_create(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-10 py-3 rounded-xl w-max flex items-center justify-start gap-2 font-semibold text-xl leading-7 tracking-wider disabled:opacity-50 disabled:cursor-not-allowed text-white bg-metallic_seaweed']"
        ).click()