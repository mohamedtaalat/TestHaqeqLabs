from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewArticlePage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_title_of_article(self,title):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='title']"
        ).send_keys(title)

    def enter_name_of_author(self,author):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='author']"
        ).send_keys(author)

    def enter_date_of_published_article(self,path_of_year,path_of_month,path_of_day):
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

    def enter_poster(self,poster):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='p-ripple p-button p-component p-fileupload-choose-button undefined']"
        ).send_keys(poster)

    def enter_description(self,description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='p-textarea p-component w-full h-60 font-medium leading-8 tracking-wide ng-pristine ng-valid ng-touched']"
        ).send_keys(description)

    def enter_conclusion(self,conclusion):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='p-textarea p-component w-full h-60 font-medium leading-8 tracking-wide ng-untouched ng-pristine ng-valid']"
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

    def add_article(self,name_of_article,name_of_author,path_of_year,path_of_month,path_of_day,poster,description,conclusion,topics):
        self.enter_title_of_article(name_of_article)
        self.enter_name_of_author(name_of_author)
        self.enter_date_of_published_article(path_of_year,path_of_month,path_of_day)
        self.enter_poster(poster)
        self.enter_description(description)
        self.enter_conclusion(conclusion)
        self.enter_topics(topics)
        self.click_add()
