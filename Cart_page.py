import conftest
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.carrinho = (By.XPATH, '//*[@class="shopping_cart_link"]')
        self.voltar = (By.ID, "continue-shopping")
        self.checkout = (By.ID, "checkout")
        self.nome = (By.ID, "first-name")
        self.sobrenome = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continuebtn = (By.ID, "continue")
        self.finishbtn = (By.ID, "finish")

    def adicionar_item_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1]).format(nome_item)
        self.clicar(item)
    
    def acessar_carrinho(self):
        self.clicar(self.carrinho)
    