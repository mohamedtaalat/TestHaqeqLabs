from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewMobadraPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_title_of_mobadra(self,title_of_mobadra):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='title']"
        ).send_keys(title_of_mobadra)

    def select_status_of_mobadra(self,status_of_mobadra):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@aria-label='حدد حالة المبادرة']"
        ).click()
        if status_of_mobadra == "Now":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//div[contains(@class,'p-select-list-container')]//li[.//span[normalize-space()='حالية']]"
            )
        elif status_of_mobadra == "Past":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//div[contains(@class,'p-select-list-container')]//li[.//span[normalize-space()='سابقة']]"
            ).click()

    def select_type(self,type_of_mobadra):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@aria-label='حدد التصنيف']"
        ).click()
        if type_of_mobadra == "Educational":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[1]"
            ).click()

        elif type_of_mobadra == "Health":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[2]"
            ).click()

        elif type_of_mobadra == "Environmental":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[3]"
            ).click()

        elif type_of_mobadra == "Developmental":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[4]"
            ).click()

        elif type_of_mobadra == "Pastoral":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[5]"
            ).click()

    def enter_date_of_start(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@class='p-datepicker p-component p-inputwrapper p-focus']//calendaricon[@class='p-component p-iconwrapper p-datepicker-input-icon']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose Year']"
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

    def enter_date_of_end(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-datepicker[@class='w-full ng-untouched ng-pristine ng-valid ng-tns-c2825477640-18']//calendaricon[@class='p-component p-iconwrapper p-datepicker-input-icon']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose Year']"
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

    def enter_file(self,file):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-fileupload[@accept='application/pdf']//span[@class='p-button-label'][normalize-space()='Choose']"
        ).send_keys(file)

    def enter_poster(self,poster):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-fileupload[@accept='image/*']//p-button[@data-pc-section='choosebutton']//button[@type='button']"
        ).send_keys(poster)

    def enter_description(self,description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل وصف المبادرة']"
        ).send_keys(description)

    def enter_result(self,result):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل نتيجة المبادرة']"
        ).send_keys(result)

    def enter_topics(self,topics):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='ql-editor ql-blank']"
        ).send_keys(topics)

    def click_create(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

