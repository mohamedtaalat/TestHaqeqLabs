import json
import time

import pytest

from pages.sign_in_pages.super_admin.sign_in_form_page import SignInFormPage
from pages.super_admin_pages.articles_pages.add_new_article_page import AddNewArticlePage
from pages.super_admin_pages.articles_pages.main_page import MainPage
from pages.super_admin_pages.side_bar_page import SideBarPage


@pytest.mark.usefixtures("driver")
class TestAddNewArticle:
    with open("data/super_admin/articles/happy_scenarios.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_article
    def test_add_new_article_happy_scenarios(self, driver, data):
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com","12345678")
        sd = SideBarPage(driver)
        sd.click_articles()
        mp = MainPage(driver)
        mp.click_add_article()
        ap = AddNewArticlePage(driver)
        ap.add_article(
            data["name_of_article"],
            data["name_of_author"],
            data["path_of_year"],
            data["path_of_month"],
            data["path_of_day"],
            data["poster"],
            data["description"],
            data["conclusion"],
            data["topics"]
        )
        time.sleep(2)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\articles\\happy_scenarios\\{data['screenshot']}.png")

    with open("data/super_admin/articles/negative_scenarios.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    @pytest.mark.add_article
    def test_add_new_article_negative_scenarios(self, driver, data):
        sign = SignInFormPage(driver)
        sign.sign_in("admin@haqeq.com", "12345678")
        sd = SideBarPage(driver)
        sd.click_articles()
        mp = MainPage(driver)
        mp.click_add_article()
        ap = AddNewArticlePage(driver)
        ap.add_article(
            data["name_of_article"],
            data["name_of_author"],
            data["path_of_year"],
            data["path_of_month"],
            data["path_of_day"],
            data["poster"],
            data["description"],
            data["conclusion"],
            data["topics"]
        )
        time.sleep(2)
        driver.save_screenshot(
            f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\super_admin\\articles\\negative_scenarios\\{data['screenshot']}.png")