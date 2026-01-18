from selenium.webdriver.common.by import By

from base.basis import Base


class SettingsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_vision(self, vision):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-setting[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='flex gap-6']/div[@class='flex-1 bg-white rounded-xl']/div[2]/div[1]"
        ).send_keys(vision)

    def enter_message(self, message):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-setting[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='flex gap-6']/div[@class='flex-1 bg-white rounded-xl']/div[3]/div[1]"
        ).send_keys(message)

    def click_edit_hokma(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-setting[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='flex gap-6']/div[@class='flex-1 bg-white rounded-xl']/div[@class='w-full flex items-start justify-start gap-15']/div[1]/div[1]/div[1]/button[1]/*[1]//*[name()='svg']"
        ).click()

    def enter_hokma(self, hokma):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='w-full p-3 border border-gray-300 rounded-lg text-base leading-8 text-dark_grey ng-untouched ng-valid ng-star-inserted ng-dirty']"
        ).send_keys(hokma)

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
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-setting[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='flex gap-6']/div[@class='flex-1 bg-white rounded-xl']/div[@class='w-full flex items-start justify-start gap-15']/div[@class='w-fit flex flex-col gap-4 p-8']/div[@class='p-3 rounded-lg border border-metallic_seaweed']/div[@class='w-full flex items-center justify-end mt-4 ng-star-inserted']/button/*[1]//*[name()='svg']"
        ).click()

    def enter_satisfaction(self, satisfaction):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@class='w-full p-3 border border-gray-300 rounded-lg text-base leading-8 text-dark_grey ng-untouched ng-pristine ng-valid ng-star-inserted']"
        ).send_keys(satisfaction)

    def click_save_satisfaction(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='w-full flex items-start justify-start gap-15']//div[2]//div[1]//div[1]//button[1]"
        ).click()

    def edit_satisfaction(self, satisfaction):
        self.click_edit_satisfaction()
        self.enter_satisfaction(satisfaction)
        self.click_save_satisfaction()

