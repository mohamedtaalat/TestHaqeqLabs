from selenium.webdriver.common.by import By

from base.basis import Base


class SideBar(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_open_side_bar(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//div[@class='text-login_btn_bg bg-transparent rounded-md lg:hidden cursor-pointer']//*[name()='svg']"
        ).click()

    def click_asses_project(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'تقييم المشروع')]"
        ).click()

    def click_partners(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'الشركات')]"
        ).click()

    def click_partner_order(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'طلبات الشراكة')]"
        ).click()

    def click_wallets(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'المحافظ')]"
        ).click()

    def click_programs(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'البرامج')]"
        ).click()

    def click_manage_projects(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'ادارة المشاريع')]"
        ).click()

    def click_activities(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'الانشطة')]"
        ).click()

    def click_plan_manage_performance(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'خطة إدارة الأداء')]"
        ).click()

    def click_performance_of_moshar(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'تتبع اداء الموشرات')]"
        ).click()

    def click_the_continue(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'المتابعة')]"
        ).click()

    def click_the_assessment(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'التقييم')]"
        ).click()

    def click_almosala(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'المسألة')]"
        ).click()

    def click_the_education(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[@href='/learning']//span[contains(text(),'التعلم')]"
        ).click()

    def click_simple_education(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'نموذج التعلم')]"
        ).click()

    def click_results_of_mokhtaber(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'نتائج المختبر')]"
        ).click()

    def click_manage_tamoel(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'ادارة التمويل')]"
        ).click()

    def click_astshareens(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'الأستشاريين')]"
        ).click()

    def click_orders_of_astsharh(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'طلبات الأستشارة')]"
        ).click()

    def click_the_exercise(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'التدريب')]"
        ).click()

    def click_the_bacqats(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//span[contains(text(),'الباقات')]"
        ).click()