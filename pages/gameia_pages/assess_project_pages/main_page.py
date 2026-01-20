from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from base.basis import Base


class MainPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def enter_project_name(self,project_name):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='projectName']"
        ).send_keys(project_name)

    def enter_project_description(self,project_description):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='description']"
        ).send_keys(project_description)

    def enter_name_of_team(self,name_of_team):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='founderName']"
        ).send_keys(name_of_team)

    def enter_email(self,email):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='email']"
        ).send_keys(email)

    def enter_phone_number(self,phone_number):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//input[@id='phone']"
        ).send_keys(phone_number)

    def enter_problem(self,problem):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='problem']"
        ).send_keys(problem)

    def enter_solution(self,solution):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='solution']"
        ).send_keys(solution)

    def enter_why_this_solution_is_better(self,why_this_solution_is_better):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='whyBetter']"
        ).send_keys(why_this_solution_is_better)

    def enter_target_audience(self,target_audience):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='targetAudience']"
        ).send_keys(target_audience)

    def enter_exam_explanation(self,exam_explanation):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='isTested']"
        ).send_keys(exam_explanation)

    def choose_positive(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='إيجابية']"
        ).click()

    def choose_hybrid(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='مختلطة']"
        ).click()

    def choose_not_clear(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='غير واضحة']"
        ).click()

    def choose_firstly_results(self, result):
        if result == "Positive":
            self.choose_positive()
        elif result == "Hybrid":
            self.choose_hybrid()
        elif result == "NotClear":
            self.choose_not_clear()

    def choose_economic(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='اقتصادي']"
        ).click()

    def choose_social(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='اجتماعي']"
        ).click()

    def choose_environmental(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='بيئي']"
        ).click()

    def choose_educational(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='تعليمي']"
        ).click()

    def choose_healthy(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='صحي']"
        ).click()

    def choose_athar(self,athar):
        if athar == "Economic":
            self.choose_economic()
        elif athar == "Social":
            self.choose_social()
        elif athar == "Environmental":
            self.choose_environmental()
        elif athar == "Healthy":
            self.choose_healthy()
        elif athar == "Educational":
            self.choose_educational()

    def choose_big(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='كبير']"
        ).click()

    def choose_medium(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='متوسط']"
        ).click()

    def choose_limited(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='محدود']"
        ).click()

    def choose_the_value(self,value):
        if value == "Big":
            self.choose_big()
        elif value == "Medium":
            self.choose_medium()
        elif value == "Limited":
            self.choose_limited()

    def enter_stretching(self,stretching):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='scalability']"
        ).send_keys(stretching)

    def enter_source_of_income(self,source_of_income):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='revenueSource']"
        ).send_keys(source_of_income)

    def enter_ability_of_continue(self,ability_of_continue):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='sustainabilityPotential']"
        ).send_keys(ability_of_continue)

    def enter_main_expectations(self,main_expectations):
        self.wait_until_element_be_visible(
            By.XPATH,
            "//textarea[@id='assumptions']"
        ).send_keys(main_expectations)

    def choose_soqeh(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='سوقية']"
        ).click()

    def choose_technology(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='تقنية']"
        ).click()

    def choose_finance(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@value='مالية']"
        ).click()

    def choose_dangers(self,danger):
        if danger == "Soqeh":
            self.choose_soqeh()
        elif danger == "Technology":
            self.choose_technology()
        elif danger == "Finance":
            self.choose_finance()

    def click_start_assessment(self):
        try:
            self.wait_until_element_be_clickable(
                By.XPATH,
                "//button[@type='submit']"
            ).click()
        except NoSuchElementException,TimeoutException:
            pass

    def assess_project(
            self,project_name,project_description,name_of_team,email,phone_number,problem,
            solution,why_this_solution_is_better,target_audience,
            exam_explanation,result,athar,value,stretching,source_of_income,ability_of_continue,
            main_expectations,danger
    ):
        self.enter_project_name(project_name)
        self.enter_project_description(project_description)
        self.enter_name_of_team(name_of_team)
        self.enter_email(email)
        self.enter_phone_number(phone_number)
        self.enter_problem(problem)
        self.enter_solution(solution)
        self.enter_why_this_solution_is_better(why_this_solution_is_better)
        self.enter_target_audience(target_audience)
        self.enter_exam_explanation(exam_explanation)
        self.choose_firstly_results(result)
        self.choose_athar(athar)
        self.choose_the_value(value)
        self.enter_stretching(stretching)
        self.enter_source_of_income(source_of_income)
        self.enter_ability_of_continue(ability_of_continue)
        self.enter_main_expectations(main_expectations)
        self.choose_dangers(danger)
        self.click_start_assessment()

    def catch_button_status(self):
        return self.wait_until_element_be_visible(
            By.XPATH,
            "//button[@type='submit']"
        )