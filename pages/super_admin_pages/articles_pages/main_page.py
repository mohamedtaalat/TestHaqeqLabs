from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_send(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@label='ارسال']//button[@type='button']"
        ).click()

    def click_export(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@class='ms-6']//button[@type='button']"
        ).click()

    def click_add_article(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//p-button[@class='min-w-max']//button[@type='button']"
        ).click()

    def click_delete_all(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-button-outlined mb-2 p-button p-component']"
        ).click()

    def enter_name_in_search_bar(self,name):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ابحث بالاسم']"
        ).send_keys(name)

    def click_edit_article(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()

    def click_delete_article(self,path):
        self.wait_until_element_be_clickable(
            By.XPATH,
            path
        ).click()
