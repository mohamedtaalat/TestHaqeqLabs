import time

from selenium.webdriver.common.by import By

from base.basis import Base


class AddWalletPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def enter_wallet_name(self,wallet_name):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم المحفظة']"
        ).send_keys(wallet_name)

    def enter_the_owner_gaha(self,owner_gaha):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل الجهة المالكة للمحفظة']"
        ).send_keys(owner_gaha)

    def enter_start_date(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@class='font-semibold text-xl leading-none tracking-normal text-right text-gray-400 ng-star-inserted']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose month and year']"
        ).click()

        time.sleep(1)
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_year
        ).click()
        time.sleep(1)
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_month
        ).click()
        time.sleep(1)
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_day
        ).click()
        time.sleep(1)

    def enter_end_date(self, path_of_year, path_of_month, path_of_day):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[@class='font-semibold leading-none tracking-normal text-right text-gray-400 ng-star-inserted']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@aria-label='Choose month and year']"
        ).click()
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_year
        ).click()
        time.sleep(1)
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_month
        ).click()
        time.sleep(1)
        self.wait_until_element_be_clickable(
            By.XPATH,
            path_of_day
        ).click()
        time.sleep(1)

    def enter_wallet_description(self,wallet_description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@placeholder='ادخل وصف المحفظة']"
        ).send_keys(wallet_description)


    def click_create(self):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='px-10 py-3 rounded-xl w-max flex items-center justify-start gap-2 font-semibold text-xl leading-7 tracking-wider disabled:opacity-50 disabled:cursor-not-allowed text-white bg-metallic_seaweed']"
        )
        self.scroll_to_element(element)
        element.click()


