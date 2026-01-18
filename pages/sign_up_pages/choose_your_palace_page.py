from selenium.webdriver.common.by import By

from base.basis import Base


class ChooseYourPalacePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def choose_gameia(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='icons/svgs/gamaya.svg']//*[name()='svg']"
        ).click()

    def choose_astshare(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='icons/svgs/consultant.svg']//*[name()='svg']"
        ).click()

    def choose_gaha_manha(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//*[@src='icons/svgs/funding.svg']//*[name()='svg']"
        ).click()

    def click_continue(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[contains(text(),'متابعة')]"
        )
        self.scroll_to_element(element)
        element.click()

