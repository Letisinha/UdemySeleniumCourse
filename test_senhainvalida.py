import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest
from Pages.Login_page import LoginPage
from Pages.Base_page import BasePage
from Pages.Home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
class Test_parte04:
    def test_04_udemy(self):
        browser = conftest.browser
        Base_page = BasePage()
        Login_page = LoginPage()

        Login_page.fazer_login("standard_user", "senha_invalida")

        Login_page.verificar_mensagem_erro_existe()

        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        Login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)