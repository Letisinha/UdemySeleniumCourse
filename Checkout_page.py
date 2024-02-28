import conftest
from Pages.Base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.botao_checkout = (By. ID, "checkout")
        self.nome = (By.ID, "first-name")
        self.sobrenome = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continuebtn = (By.ID, "continue")
        self.finishbtn = (By.ID, "finish")

    def clicar_botao_checkout(self):
        self.clicar(self.botao_checkout)

    def dados_pessoais(self, nome, sobrenome, postal_code):
        self.escrever(self.nome, nome)
        self.escrever(self.sobrenome, sobrenome)
        self.escrever(self.postal_code, postal_code)

    def continue_finish(self):
        self.clicar(self.continuebtn)
        self.clicar(self.finishbtn)