import pytest
from selenium import webdriver

browser = webdriver.Remote

@pytest.fixture
def setup_teardown():
	#setup
	global browser
	#(inserir aqui o que deve ser repetido)
	browser = webdriver.Edge()
	browser.maximize_window()
	browser.get("https://www.saucedemo.com/")
	#run test (o teste vai ser executado quando chegar no yield. Vai rodar o def de que esse é o setup e quando chegar no yield, vai começar a rodar o teste de fato)
	yield

	#teardown pra finalizar todos os testes que o yield rodar
	browser.quit()