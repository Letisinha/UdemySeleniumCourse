import conftest
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self):
        self.browser = conftest.browser

    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)

    def escrever(self, locator, texto):
        return self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        return self.encontrar_elemento(locator).click()

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(
        ), f"o elemento {locator} não foi encontrado na tela"

    def get_texto_elemento(self, locator):
        return self.encontrar_elemento(locator).text