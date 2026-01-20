import json
import time

import pytest

from pages.sign_in_pages.super_admin.sign_in_form_page import SignInFormPage
from pages.super_admin_pages.baqats_pages.add_new_baqa_page import AddNewBaqaPage
from pages.super_admin_pages.baqats_pages.main_page import MainPage
from pages.super_admin_pages.side_bar_page import SideBarPage


@pytest.mark.usefixtures("driver")
class TestAddNewBaqa:
    with open("data/super_admin/baqa/happy_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_baqa
    def test_add_new_baqa_happy_scenarios(self,driver,data):
        driver.get("https://admin.haqqeq-lab.com/login")
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com","12345678")
        sb = SideBarPage(driver)
        # sb.click_open_side_bar()
        sb.click_baqats()
        mp = MainPage(driver)
        mp.click_add_new_baqa()
        ab = AddNewBaqaPage(driver)
        ab.add_new_baqa(
            data["name_of_new_baqa"],
            data["symbol_of_baqa"],
            data["timeframe_of_trial"],
            data["time_of_subscription"],
            data["number_of_wallets"],
            data["number_of_programs"],
            data["number_of_projects"],
            data["name_of_advantage"],
            data["name_of_disadvantage"],
            data["name_of_value"],
            data["feature"],
            data["price"],
            data["type_of_discount"],
            data["status_of_discount"],
            data["code_of_discount"],
            data["status_of_baqa"]
        )
        time.sleep(2)
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\baqa\\happy_scenarios\\{data['screenshot']}.png")


    with open("data/super_admin/baqa/negative_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_baqa
    def test_add_new_baqa_negative_scenarios(self,driver,data):
        driver.get("https://admin.haqqeq-lab.com/login")
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com", "12345678")
        sb = SideBarPage(driver)
        # sb.click_open_side_bar()
        sb.click_baqats()
        mp = MainPage(driver)
        mp.click_add_new_baqa()
        ab = AddNewBaqaPage(driver)
        ab.add_new_baqa(
            data["name_of_new_baqa"],
            data["symbol_of_baqa"],
            data["timeframe_of_trial"],
            data["time_of_subscription"],
            data["number_of_wallets"],
            data["number_of_programs"],
            data["number_of_projects"],
            data["name_of_advantage"],
            data["name_of_disadvantage"],
            data["name_of_value"],
            data["feature"],
            data["price"],
            data["type_of_discount"],
            data["status_of_discount"],
            data["code_of_discount"],
            data["status_of_baqa"]
        )
        time.sleep(2)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\baqa\\negative_scenarios\\{data['screenshot']}.png")
