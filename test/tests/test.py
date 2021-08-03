import json
import pytest
from page_object.inputs import Inputs
from seleniumbase import BaseCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from page_object.login_page import (Login, LoginPage)

class TestBase(BaseCase):
    @pytest.fixture(autouse=True)
    def inputs(self, pytestconfig) -> Inputs:
        inputs_path = pytestconfig.getoption("inputs")
        with open(inputs_path, encoding="utf-8") as f:
            inputs = json.load(f)
            self.inputs = Inputs(**inputs)

class LoginUser(TestBase):
    def landing(self) -> WebElement:
        self.driver.get(
            f"http://13.115.251.76:8080/exam/login"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def click_submit_btn(self):
        submit_btn: WebElement = self.find_element(
            LoginPage.submit_btn
        )
        submit_btn.click()   

    def populate_login(
        self,
        username,
        password,
        ):
        uname: WebElement = self.find_element(LoginPage.username)
        uname.send_keys(username)

        pwd: WebElement = self.find_element(LoginPage.password)
        pwd.send_keys(password)

    def test1(self):
        self.landing()
        
        login_page: Login = self.inputs.user.login
        self.populate_login(
            str(login_page.username),
            str(login_page.password),
        )

        self.click_submit_btn()

        self.assert_text("ログイン完了")
        