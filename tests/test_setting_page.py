import json
import time

import pytest

from pages.gameia_pages.dashboard_pages.main_page import MainPage
from pages.gameia_pages.dashboard_pages.settings_page import SettingsPage
from pages.sign_in_pages.gameia.second_sign_in_form_page import SecondSignInFormPage


@pytest.mark.usefixtures("driver")
class TestSettingPage:
    with open("data/gameia/settings/vision.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.vision
    def test_vision(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")
        mp = MainPage(driver)
        mp.click_settings()
        sp = SettingsPage(driver)
        sp.enter_vision(data["vision"])
        time.sleep(3)
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\settings\\vision\\{data['screenshot']}.jpg")

    with open("data/gameia/settings/message.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.message
    def test_message(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")
        time.sleep(1)
        mp = MainPage(driver)
        mp.click_settings()
        sp = SettingsPage(driver)
        sp.enter_message(data["message"])
        time.sleep(3)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\settings\\message\\{data['screenshot']}.jpg")

    with open("data/gameia/settings/hokma.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.hokma
    def test_hokma(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")
        time.sleep(1)
        mp = MainPage(driver)
        mp.click_settings()
        sp = SettingsPage(driver)
        sp.edit_hokma(data["hokma"])
        time.sleep(3)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\settings\\hokma\\{data['screenshot']}.jpg")


    with open("data/gameia/settings/satisfaction.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.satisfaction
    def test_satisfaction(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")
        time.sleep(1)
        mp = MainPage(driver)
        mp.click_settings()
        sp = SettingsPage(driver)
        sp.edit_satisfaction(data["satisfaction"])
        time.sleep(3)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\settings\\satisfaction\\{data['screenshot']}.jpg")
