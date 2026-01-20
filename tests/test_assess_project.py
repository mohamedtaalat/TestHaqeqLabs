import json
import time
import pytest
from pages.gameia_pages.assess_project_pages.main_page import MainPage
from pages.gameia_pages.side_bar import SideBar
from pages.sign_in_pages.gameia.second_sign_in_form_page import SecondSignInFormPage
from utilites.utility import Utility


@pytest.mark.usefixtures("driver")
class TestAssessProject:
    with open("data/gameia/assess_project/happy_scenarios.json.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    @pytest.mark.assess_project
    @pytest.mark.smoke
    def test_assess_project_happy_scenarios(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro","12345678")


        sb = SideBar(driver)
        sb.click_open_side_bar()
        sb.click_asses_project()
        time.sleep(3)
        mp = MainPage(driver)
        mp.assess_project(
            data["project_name"],
            data["project_description"],
            data["name_of_team"],
            data["email"],
            data["phone_number"],
            data["problem"],
            data["solution"],
            data["why_this_solution_is_better"],
            data["target_audience"],
            data["exam_explanation"],
            data["result"],
            data["athar"],
            data["value"],
            data["stretching"],
            data["source_of_income"],
            data["ability_of_continue"],
            data["main_expectations"],
            data["danger"]
        )
        time.sleep(20)
        driver.execute_script("document.body.style.zoom='40%'")
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\assess_project\\happy_scenarios.json\\{data['screenshot']}.png")


    with open("data/gameia/assess_project/negative_scenarios.json.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    @pytest.mark.assess_project
    def test_assess_project_negative_scenarios(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro","12345678")


        sb = SideBar(driver)
        sb.click_open_side_bar()
        sb.click_asses_project()
        time.sleep(3)
        mp = MainPage(driver)
        mp.assess_project(
            data["project_name"],
            data["project_description"],
            data["name_of_team"],
            data["email"],
            data["phone_number"],
            data["problem"],
            data["solution"],
            data["why_this_solution_is_better"],
            data["target_audience"],
            data["exam_explanation"],
            data["result"],
            data["athar"],
            data["value"],
            data["stretching"],
            data["source_of_income"],
            data["ability_of_continue"],
            data["main_expectations"],
            data["danger"]
        )
        time.sleep(2)
        driver.execute_script("document.body.style.zoom='40%'")
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\assess_project\\negative_scenarios.json\\{data['screenshot']}.png")
        utl = Utility()
        utl.test_element_is_disabled(mp.catch_button_status())