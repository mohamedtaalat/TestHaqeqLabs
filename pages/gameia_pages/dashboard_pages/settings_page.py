from selenium.webdriver.common.by import By

from base.basis import Base


class SettingsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_vision(self, vision):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[contains(@class,'justify-end')]//button"
        ).click()
        self.wait_until_element_be_visible(
            By.XPATH,
            ""
        ).send_keys(vision)

    def enter_message(self, message):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-setting/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='flex gap-6']/div[@class='flex-1 bg-white rounded-xl']/div[3]/div[1]/div[1]/button[1]/*[1]//*[name()='svg']"
        ).click()

        element = self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='w-full p-3 border border-gray-300 rounded-lg text-base leading-8 text-dark_grey ng-untouched ng-pristine ng-valid']"
        )
        element.clear()
        element.send_keys(message)
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='bg-metallic_seaweed text-white px-4 py-2 rounded-lg font-semibold']"
        ).click()

    def click_edit_hokma(self):
        element =  self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full flex items-start justify-start gap-15']//div[1]//div[1]//div[1]//button"
        )
        self.scroll_to_element(element)
        element.click()

    def enter_hokma(self, hokma):
        element = self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='w-full p-3 border border-gray-300 rounded-lg text-base leading-8 text-dark_grey ng-untouched ng-pristine ng-valid']"
        )
        element.clear()
        element.send_keys(hokma)

    def click_save_hokma(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='bg-metallic_seaweed text-white px-4 py-2 rounded-lg font-semibold']"
        ).click()

    def edit_hokma(self, hokma):
        self.click_edit_hokma()
        self.enter_hokma(hokma)
        self.click_save_hokma()

    def click_edit_satisfaction(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full flex items-start justify-start gap-15']//div[2]//button"
        )
        self.scroll_to_element(element)
        element.click()

    def enter_satisfaction(self, satisfaction):
        element = self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='w-full p-3 border border-gray-300 rounded-lg text-base leading-8 text-dark_grey ng-untouched ng-pristine ng-valid']"
        )
        print(element)
        element.clear()
        element.send_keys(satisfaction)

    def click_save_satisfaction(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full flex items-start justify-start gap-15']//div[2]//div[1]//div[1]//button[1]"
        ).click()

    def edit_satisfaction(self, satisfaction):
        self.click_edit_satisfaction()
        self.enter_satisfaction(satisfaction)
        self.click_save_satisfaction()

