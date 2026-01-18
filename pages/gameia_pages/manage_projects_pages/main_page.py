from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_text_in_search_bar_of_projects(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-investment-dashboard[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[1]/div[1]/div[1]"
        ).send_keys(text)

    def click_add_new_project(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='flex items-center justify-end gap-4']//button[@class='flex items-center justify-start px-6 py-3 rounded-lg cursor-pointer bg-metallic_seaweed']"
        ).click()

    def click_export_projects(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='flex items-center justify-start px-6 py-3 rounded-lg cursor-pointer border-2 border-metallic_seaweed text-metallic_seaweed bg-transparent hover:bg-metallic_seaweed hover:text-white']"
        ).click()

    def enter_text_in_search_bar_of_employee(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ابحث عن موظف']"
        ).send_keys(text)

    def click_add_new_employee(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-investment-dashboard[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='w-full flex flex-col items-start gap-6 p-6 rounded-xl bg-white']/div[@class='w-full flex items-center justify-between']/button[1]"
        ).click()

    def enter_text_in_search_bar_of_exported_projects(self,text):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//body/app-root/div[@class='relative w-full h-[100vh]']/haqeq-investment-dashboard[@class='ng-star-inserted']/app-side-nav/div[@class='flex h-screen']/div[@class='flex-1 -translate-x-[10px]']/div[@class='max-content-width min-h-[90vh] bg-bright_gray']/div[@class='w-full p-8 min-h-[89vh] flex flex-col gap-8 border-t-2 border-light_gray_border bg-white']/div[@class='w-full flex flex-col items-start gap-6 p-6 rounded-xl bg-white']/div[@class='w-full flex flex-col items-start gap-6 p-6 rounded-xl bg-white']/div[@class='w-full flex items-center justify-between']/div[1]"
        ).send_keys(text)

    