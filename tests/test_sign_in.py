import time

import pytest
import json
from pages.sign_in_pages.second_sign_in_form_page import SecondSignInFormPage
from pages.sign_in_pages.sign_in_form_page import SignInFormPage
from utilites.utility import Utility


@pytest.mark.usefixtures("driver")
class TestSignIn:
    with open("data/sign_in_data/happy_scenarios.json") as f :
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_sign_in_happy_scenarios(self, driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in(data["email"], data["password"])
        time.sleep(3)
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\sign_in\\happy_scenarios\\{data["screenshot"]}.png")


    with open("data/sign_in_data/negative_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_sign_in_negative_scenarios(self, driver,data):
        sign = SignInFormPage(driver)
        sign.sign_in(data["email"], data["password"])
        element = sign.catch_error_message()
        time.sleep(3)
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\sign_in\\negative_scenarios\\{data["screenshot"]}.png")
        utl = Utility()
        utl.test_element_is_present(element)