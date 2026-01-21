import json
import time

import pytest

from pages.sign_in_pages.super_admin.sign_in_form_page import SignInFormPage
from pages.super_admin_pages.news_pages.add_new_news_page import AddNewNewsPage
from pages.super_admin_pages.side_bar_page import SideBarPage


@pytest.mark.usefixtures("driver")
class TestAddNewNews:
    with open("data/super_admin/news/happy_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_news
    def test_add_new_news_happy_scenarios(self, driver, data):
        driver.get("https://admin.haqqeq-lab.com/login")
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com", "12345678")
        sd = SideBarPage(driver)
        sd.click_news()
        ap = AddNewNewsPage(driver)
        ap.add_new_news(
            data["title"],
            data["poster"],
            data["description"],
            data["conclusion"],
            data["topics"]
        )
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\news\\happy_scenarios\\{data['screenshot']}.png")
        time.sleep(2)

    with open("data/super_admin/news/negative_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_news
    def test_add_new_news_negative_scenarios(self, driver, data):
        driver.get("https://admin.haqqeq-lab.com/login")
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com", "12345678")
        sd = SideBarPage(driver)
        sd.click_news()
        ap = AddNewNewsPage(driver)
        ap.add_new_news(
            data["title"],
            data["poster"],
            data["description"],
            data["conclusion"],
            data["topics"]
        )
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\news\\negative_scenarios\\{data['screenshot']}.png")
        time.sleep(2)