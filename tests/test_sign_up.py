import time

import pytest
import json

from pages.sign_up_pages.sign_up_form_page import SignUpFormPage
from utilites.utility import Utility


@pytest.mark.usefixtures("driver")
class TestSignUp:

    with open("data/sign_up_data/happy_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.signup
    def test_sign_up_happy_scenarios(self, driver,data):
        sg = SignUpFormPage(driver)
        sg.sign_up(
            data["name_of_gameia"],
            data["email"],
            data["phone_number"],
            data["password"],
            data["confirm_password"]
        )
        time.sleep(1)
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\sign_up\\happy_scenarios\\{data['screenshot']}.png")
        element = sg.catch_error_message()
        utl = Utility()
        utl.test_element_is_not_present(element)

    with open("data/sign_up_data/negative_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.signup
    def test_sign_up_negative_scenarios(self, driver,data):
        sg = SignUpFormPage(driver)
        sg.sign_up(
            data["name_of_gameia"],
            data["email"],
            data["phone_number"],
            data["password"],
            data["confirm_password"]
        )
        time.sleep(1)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\sign_up\\negative_scenarios\\{data['screenshot']}.png"
        )
        element = sg.catch_error_message()
        utl = Utility()
        utl.test_element_is_present(element)
