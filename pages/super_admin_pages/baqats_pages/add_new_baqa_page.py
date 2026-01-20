from selenium.webdriver.common.by import By

from base.basis import Base


class AddNewBaqaPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_name_of_baqa(self,name_of_baqa):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم الباقة']"
        ).send_keys(name_of_baqa)

    def enter_symbol_of_baqa(self,symbol_of_baqa):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='رمز الباقة (Code) ادخل']"
        ).send_keys(symbol_of_baqa)

    def enter_timeframe_of_trial(self,timeframe_of_trial):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل فترة التجربة بالايام']"
        ).send_keys(timeframe_of_trial)

    def select_time_of_subscription(self,time_of_subscription):
        if time_of_subscription == "Monthly":
            self.wait_until_element_be_visible(
                By.XPATH,
                "//input[@value='monthly']"
            ).click()
        elif time_of_subscription == "Yearly":
            self.wait_until_element_be_visible(
                By.XPATH,
                "//input[@value='yearly']"
            ).click()
        elif time_of_subscription == "Trial":
            self.wait_until_element_be_visible(
                By.XPATH,
                "//input[@value='trial']"
            ).click()

    def enter_number_of_wallets(self,number_of_wallets):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='عدد المحافظ']"
        ).send_keys(number_of_wallets)

    def enter_number_of_programs(self,number_of_programs):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='عدد البرامج']"
        ).send_keys(number_of_programs)

    def enter_number_of_projects(self,number_of_projects):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='عدد المشاريع']"
        ).send_keys(number_of_projects)

    def click_add_new_advantage(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[contains(text(),'اضافة ميزه جديدة')]"
        ).click()

    def enter_name_of_advantage(self,name_of_advantage):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل اسم الميزه']"
        ).send_keys(name_of_advantage)

    def click_add_new_disadvantage(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[contains(text(),'اضافة قيود جديدة')]"
        ).click()

    def enter_name_of_disadvantage(self,name_of_disadvantage):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل القيود']"
        ).send_keys(name_of_disadvantage)

    def click_add_new_value(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[contains(text(),'اضافة قيمة جديدة')]"
        ).click()

    def enter_name_of_value(self,name_of_value):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='ادخل قيمة مضافة']"
        ).send_keys(name_of_value)

    def select_feature(self,feature):
        if feature == "AI Reports":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='تقارير AI']"
            ).click()

        elif feature == "Table Of Measure":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='لوحة قياس الأثر']"
            ).click()

        elif feature == "Manage Activities":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='إدارة الأنشطة']"
            ).click()

        elif feature == "Almokhtabr":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='المختبر']"
            ).click()

        elif feature == "Meal DPro":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='MEAL DPro']"
            ).click()

        elif feature == "All":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='الكل']"
            ).click()

    def enter_price(self,price):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='سعر الباقة']"
        ).send_keys(price)

    def select_type_of_discount(self,type_of_discount):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//span[@aria-label='نسبة مئوية']"
        ).click()
        if type_of_discount == "Percentage":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//ul[@role='listbox']//li[.//span[normalize-space()='نسبة مئوية']]"
            ).click()

        elif type_of_discount == "Static":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//ul[@role='listbox']//li[.//span[normalize-space()='قيمة ثابتة']]"
            ).click()

    def select_status_of_discount(self,status_of_discount):
        if status_of_discount == "Active":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//label[contains(text(),'نشط')]//input[@name='discountStatus']"
            ).click()

        elif status_of_discount == "Stopped":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//label[contains(text(),'موقوف')]//input[@name='discountStatus']"
            ).click()

        elif status_of_discount == "Ended":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//label[contains(text(),'منتهي')]//input[@name='discountStatus']"
            ).click()

    def enter_code_of_discount(self,code_of_discount):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@placeholder='مثال: WINTER40 رمز الخصم للمستخدم']"
        ).send_keys(code_of_discount)

    def click_add_new_copon(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[contains(text(),'إضافة كوبون')]"
        ).click()

    def select_status_of_baqa(self,status_of_baqa):
        if status_of_baqa == "Active":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='active']"
            ).click()

        elif status_of_baqa == "Inactive":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='inactive']"
            ).click()

        elif status_of_baqa == "Expired":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//input[@value='expired']"
            ).click()

    def click_publish(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='font-bold text-2xl px-12 py-3 rounded-lg text-white bg-metallic_seaweed']"
        ).click()

    def click_copy(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='font-bold text-2xl leading-7 tracking-wide px-12 py-3 rounded-lg bg-transparent border border-metallic_seaweed text-metallic_seaweed hover:text-white hover:bg-metallic_seaweed']"
        ).click()

    def click_inactive(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='font-bold text-2xl leading-7 tracking-wide px-12 py-3 rounded-lg text-raisin_black bg-platinum']"
        ).click()

    def add_new_baqa(
            self,name_of_new_baqa,symbol_of_baqa,timeframe_of_trial,time_of_subscription,
            number_of_wallets,number_of_programs,number_of_projects,name_of_advantage,
            name_of_disadvantage,name_of_value,feature,price,type_of_discount,status_of_discount,
            code_of_discount,status_of_baqa
                     ):
        self.enter_name_of_baqa(name_of_baqa=name_of_new_baqa)
        self.enter_symbol_of_baqa(symbol_of_baqa=symbol_of_baqa)
        self.enter_timeframe_of_trial(timeframe_of_trial=timeframe_of_trial)
        self.select_time_of_subscription(time_of_subscription=time_of_subscription)
        self.enter_number_of_wallets(number_of_wallets=number_of_wallets)
        self.enter_number_of_programs(number_of_programs=number_of_programs)
        self.enter_number_of_projects(number_of_projects=number_of_projects)
        self.enter_name_of_advantage(name_of_advantage=name_of_advantage)
        self.enter_name_of_disadvantage(name_of_disadvantage=name_of_disadvantage)
        self.enter_name_of_value(name_of_value=name_of_value)
        self.select_feature(feature=feature)
        self.enter_price(price=price)
        self.select_type_of_discount(type_of_discount=type_of_discount)
        self.select_status_of_discount(status_of_discount=status_of_discount)
        self.enter_code_of_discount(code_of_discount=code_of_discount)
        self.select_status_of_baqa(status_of_baqa=status_of_baqa)
        self.click_publish()
