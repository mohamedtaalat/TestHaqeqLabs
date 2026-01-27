import json
import time

import pytest

from pages.gameia_pages.side_bar import SideBar
from pages.gameia_pages.wallets_pages.add_wallet_page import AddWalletPage
from pages.gameia_pages.wallets_pages.main_page import MainPage
from pages.sign_in_pages.gameia.second_sign_in_form_page import SecondSignInFormPage


@pytest.mark.usefixtures("driver")
class TestCreateWallet:
    with open("data/gameia/wallets/add_wallet/happy_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.create_wallet
    def test_create_wallet_happy_scenarios(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")

        sb = SideBar(driver)
        sb.click_open_side_bar()
        sb.click_wallets()
        time.sleep(3)
        mp = MainPage(driver)
        mp.click_create_new_wallet_button()
        time.sleep(3)
        cp = AddWalletPage(driver)
        cp.enter_wallet_name(data["wallet_name"])
        cp.enter_the_owner_gaha(data["owner_gaha"])
        cp.enter_start_date(data["path_of_year_start"],data["path_of_month_start"],data["path_of_day_start"])
        time.sleep(3)
        cp.enter_end_date(data["path_of_year_end"],data["path_of_month_end"],data["path_of_day_end"])
        cp.enter_wallet_description(data["wallet_description"])
        cp.click_create()
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\wallets\\{data['screenshot']}.png")
        time.sleep(3)

    with open("data/gameia/wallets/add_wallet/negative_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    @pytest.mark.create_wallet
    def test_create_wallet_negative_scenarios(self,driver,data):
        sign = SecondSignInFormPage(driver)
        sign.sign_in("045ec35053@webxio.pro", "12345678")

        sb = SideBar(driver)
        sb.click_open_side_bar()
        sb.click_wallets()
        time.sleep(3)
        mp = MainPage(driver)
        mp.click_create_new_wallet_button()
        time.sleep(3)
        cp = AddWalletPage(driver)
        cp.enter_wallet_name(data["wallet_name"])
        cp.enter_the_owner_gaha(data["owner_gaha"])
        cp.enter_start_date(data["path_of_year_start"],data["path_of_month_start"],data["path_of_day_start"])
        time.sleep(3)
        cp.enter_end_date(data["path_of_year_end"],data["path_of_month_end"],data["path_of_day_end"])
        cp.enter_wallet_description(data["wallet_description"])
        cp.click_create()
        driver.save_screenshot(f"C:\\Users\\admin\\PycharmProjects\\TestHaqeqLabs\\screenshots\\gameia\\wallets\\{data['screenshot']}n.png")
        time.sleep(3)