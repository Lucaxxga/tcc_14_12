import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from paginas.loginpage import LoginPage

def realizar_login(driver, login_info):
    email = login_info["email"]
    senha = login_info["senha"]

    # Espere até que o elemento com o ID "email" seja visível
    email_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_element.send_keys(email)

    # Localize o elemento da senha da mesma maneira
    senha_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    senha_element.send_keys(senha)

    # Clique no botão "Confirmar"
    botao_confirmar = LoginPage(driver)
    botao_confirmar.click_confirmar()


def test_login(driver, login_info):
    realizar_login(driver, login_info)