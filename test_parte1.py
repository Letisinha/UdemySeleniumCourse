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


@pytest.mark.usefixtures("setup_teardown")
class Test_parte01:
    def test_01_udemy(self):
        browser = conftest.browser
        # Instanciando objetos e paginas
        Base_page = BasePage()
        Login_page = LoginPage()
        Home_page = HomePage()
        Carrinho_page = CarrinhoPage()

        # Comandos usando as pages
        Login_page.fazer_login("standard_user", "secret_sauce")
        Home_page.login_com_sucesso()
        Home_page.adicionar_item_carrinho("Sauce Labs Backpack")

        Home_page.acessar_carrinho()

        Carrinho_page.assert_item_carrinho("Sauce Labs Backpack")

        Carrinho_page.continuar_comprando()

        Home_page.adicionar_item_carrinho("Sauce Labs Bolt T-Shirt")

        Home_page.acessar_carrinho()

        Carrinho_page.assert_item_carrinho("Sauce Labs Backpack")
        Carrinho_page.assert_item_carrinho("Sauce Labs Bolt T-Shirt")


        # colocando o username
        # username = browser.find_element(By.ID, "user-name")
        # username.send_keys("standard_user")

        # # colocando a senha
        # password = browser.find_element(By.ID, "password")
        # password.send_keys("secret_sauce")

        # time.sleep(1)
        # # clicar botão login
        # btn = browser.find_element(By.ID, "login-button")
        # btn.click()

        # verificar se está na página Products
        # products = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "title"))
        # )
        # assert products.is_displayed

        # adicionar item no carrinho
        # AddCart1 = browser.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']")
        # AddCart1.click()

        # abrir o carrinho
        # carrinho = browser.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
        # carrinho.click()

        # time.sleep(1)
        # # verificar se o item correto foi adicionado
        # item1 = browser.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']")
        # assert item1.is_displayed

        # # voltar para a página inicial
        # ContShopbutton = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.ID, "continue-shopping"))
        # )

        # ContShop = browser.find_element(By.ID, "continue-shopping")
        # ContShop.click()

        # time.sleep(1)
        # # adicionar outro item no carrinho
        # AddCart2 = browser.find_element(
        #     By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        # AddCart2.click()

        # # abrir o carrinho novamente
        # carrinho = browser.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
        # carrinho.click()

        # # aguardar até mostrar os itens
        # seucarrinho = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@class='title']"))
        # )

        # time.sleep(1)
        # # Os itens estão no carrinho?
        # item2 = browser.find_element(
        #     By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']")
        # assert item2.is_displayed

        time.sleep(2)

        browser.quit()
