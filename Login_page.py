import conftest
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.loginbutton = (By.ID, "login-button")
        self.login_error_message = (By.XPATH, "//*[@data-test='error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.loginbutton)

    def verificar_mensagem_erro_existe(self):
        self.verificar_elemento_existe(self.login_error_message)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.get_texto_elemento(self.login_error_message)
        assert texto_encontrado == texto_esperado, f"o texto encontrado '{texto_encontrado}' não é igual ao texto esperado '{texto_esperado}'."
