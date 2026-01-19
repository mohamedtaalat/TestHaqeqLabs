from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.basis import Base


class ExportProjectPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_project(self, project_name):
       Select(
           self.wait_until_element_be_visible(
               By.XPATH,
               "//body//app-root//div[@dir='rtl']//div//div//div//div//div//div[1]//div[1]//select[1]"
           )
       ).select_by_value(project_name)

    def select_type_of_project(self, project_type):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//body//app-root//div[@dir='rtl']//div//div//div//div[2]//div[1]//select[1]"
            )
        ).select_by_value(project_type)

    def select_sample_project(self, project_sample):
        Select(
            self.wait_until_element_be_visible(
                By.XPATH,
                "//div[@class='w-full flex flex-col items-start justify-start gap-4 col-span-2 text-rich_black']//select[@class='cursor-pointer bg-transparent w-full border-none outline-none focus:outline-none focus:border-none has-[option:disabled:checked]:text-gray-400 ng-pristine ng-valid ng-touched']"
            )
        ).select_by_value(project_sample)

    def click_export_project(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-10 py-4 rounded-lg font-semibold leading-none tracking-normal bg-metallic_seaweed text-white']"
        ).click()