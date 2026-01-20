from selenium.webdriver.common.by import By

from base.basis import Base


class SideBarPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_open_side_bar(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='layout-menu-button layout-topbar-action']"
        ).click()

    def click_articles(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'المقالات')]]"
        ).click()

    def click_mobadrat(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'المبادرات')]]"

        ).click()

    def click_news(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'الاخبار')]]"
        ).click()

    def click_libraries(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'المكتبات')]]']"
        ).click()

    def click_videos(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'الفيديوهات')]]"
        ).click()

    def click_baqats(self):
         self.wait_until_element_be_clickable(
            By.XPATH,
            "//a[.//span[normalize-space()='الباقات']]"
        ).click()

    def click_gahat_donats(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'جهات التمويل')]]"
        ).click()

    def click_stakeholder_gahat(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'العملاء')]]"
        ).click()

    def click_gameiat(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'الجمعيات')]]"
        ).click()

    def click_stakeholder_gameia(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'العملاء')]]"
        ).click()

    def click_almokhtabr(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'المختبر')]]"
        ).click()

    def click_keasat(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'القياسات')]]"
        ).click()

    def click_settings(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'الاعدادات')]]"
        ).click()

    def click_activity_library(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "// a[. //span[contains(text(),'نشاط المكتبة')]]"
        ).click()

