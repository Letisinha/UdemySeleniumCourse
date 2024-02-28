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
from Pages.Carrinho_page import CarrinhoPage
from Pages.Checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup_teardown")
class Test_parte02:
    def test_02_udemy(self):
        browser = conftest.browser
        Login_page = LoginPage()
        Base_page = BasePage()
        Home_page = HomePage()
        Carrinho_page = CarrinhoPage()
        Checkout_page = CheckoutPage()

        Login_page.fazer_login("standard_user", "secret_sauce")
        Home_page.login_com_sucesso()

        Home_page.adicionar_item_carrinho("Sauce Labs Backpack")

        Home_page.acessar_carrinho()

        Checkout_page.clicar_botao_checkout()

        Checkout_page.dados_pessoais("nominho", "sobrenominho", "postalcode")

        Checkout_page.continue_finish()

        # # verificar se está na página Products
        # products = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "title"))
        # )
        # assert products.is_displayed

        # # adicionar item no carrinho
        # AddCart1 = browser.find_element(
        #     By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']")
        # AddCart1.click()

        # # abrir o carrinho
        # carrinho = browser.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
        # carrinho.click()

        # # fazer checkout
        # browser.find_element(By.ID, "checkout").click()

        # #preencher dados
        # nome = browser.find_element(By.ID, "first-name").send_keys("nominho")
        # sobrenome = browser.find_element(By.ID, "last-name").send_keys("sobrenominho")
        # postal = browser.find_element(By.ID, "postal-code").send_keys("código postal")

        # continuebtn = browser.find_element(By.ID, "continue").click()

        # finishbtn = browser.find_element(By.ID, "finish").click()

        # time.sleep(2)

        # browser.quit()
