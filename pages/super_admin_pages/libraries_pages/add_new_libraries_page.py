from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewLibrariesPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_title(self, title):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='title']"
        ).send_keys(title)

    def enter_author(self,author):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='author']"
        ).send_keys(author)

    def enter_date_of_published_libraries(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@id='icondisplay']"
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

    def select_type(self,type_of_libraries):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@aria-label='حدد التصنيف']"
        ).click()
        if type_of_libraries == "Educational":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[1]"
            ).click()

        elif type_of_libraries == "Health":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[2]"
            ).click()

        elif type_of_libraries == "Environmental":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[3]"
            ).click()

        elif type_of_libraries == "Developmental":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[4]"
            ).click()

        elif type_of_libraries == "Pastoral":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[contains(@class,'p-select-list-container')]//li[@role='option'])[5]"
            ).click()

    def enter_file(self,file):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-fileupload[@accept='application/pdf']//div//p-button[@data-pc-section='choosebutton']//button[@type='button']"
        ).send_keys(file)

    def enter_poster(self,poster):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-fileupload[@accept='image/*']//span[@class='p-button-label ng-star-inserted'][normalize-space()='Choose']"
        ).send_keys(poster)

    def enter_description(self,description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل الوصف']"
        ).send_keys(description)

    def enter_usage(self,usage):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل الأستخدام']"
        ).send_keys(usage)

    def enter_stakeholders(self, stakeholders):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@data-placeholder='ادخل المستفيدون']"
        ).send_keys(stakeholders)

    def enter_topics(self,topics):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@data-placeholder='ادخل المحاور']"
        ).send_keys(topics)

    def enter_help_in(self,help_in):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@data-placeholder='يساعد في']"
        ).send_keys(help_in)

    def click_add(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()