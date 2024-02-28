import conftest
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage

class CarrinhoPage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_continue_shopping = (By.ID, "continue-shopping")

    def assert_item_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_elemento_existe(item)

    def continuar_comprando(self):
        self.clicar(self.botao_continue_shopping)