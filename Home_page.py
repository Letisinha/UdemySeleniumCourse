import conftest
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina = (By.CLASS_NAME, "title")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.adicionar_ao_carrinho = (By.XPATH, "//*[text()= 'Add to cart']")
        self.carrinho = (By.XPATH, '//*[@class="shopping_cart_link"]')

    def login_com_sucesso(self):
        self.verificar_elemento_existe(self.titulo_pagina)

    def adicionar_item_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.adicionar_ao_carrinho)
    
    def acessar_carrinho(self):
        self.clicar(self.carrinho)
