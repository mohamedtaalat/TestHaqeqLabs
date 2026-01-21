from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewNewsPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_title(self,title):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='title']"
        ).send_keys(title)

    def enter_poster(self,poster):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//span[normalize-space()='Choose']"
        ).send_keys(poster)

    def enter_description(self,description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل وصف الخبر']"
        ).send_keys(description)

    def enter_conclusion(self,conclusion):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل نتيجة الخبر']"
        ).send_keys(conclusion)

    def enter_topics(self,topics):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//div[@class='ql-editor ql-blank']"
        ).send_keys(topics)

    def click_add(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def add_new_news(self,title,poster,description,conclusion,topics):
        self.enter_title(title)
        self.enter_poster (poster)
        self.enter_description (description)
        self.enter_conclusion (conclusion)
        self.enter_topics (topics)
        self.click_add()