import json
import time
import pytest
from pages.gameia_pages.assess_project_pages.main_page import MainPage
from pages.gameia_pages.side_bar import SideBar
from pages.sign_in_pages.second_sign_in_form_page import SecondSignInFormPage

@pytest.mark.usefixtures("driver")
class TestAssessProject:
    with open("data/assess_project/data.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    @pytest.mark.assess_project
    @pytest.mark.smoke
    def test_assess_project(self,driver,data):
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
        driver.execute_script("document.body.style.zoom='10%'")
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\assess_project\\{data['screenshot']}.png")
