import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from paginas.loginpage import LoginPage


@pytest.fixture(scope="module")
def driver():
    # Inicialize o driver (por exemplo, Firefox)
    driver = webdriver.Firefox()
    # Direcione para o site
    driver.get("https://cmtech.2do.homologa.mexx.ai/pt")
    driver.maximize_window()
    yield driver  # Passe o driver como uma fixture
    # Encerre o driver após os testes
    driver.quit()

@pytest.fixture
def login_info():
    # Forneça informações de login (email, senha, etc.)
    return {
        "email": "vmbm@cesar.school",
        "senha": "123456",
    }

@pytest.fixture
def botaoconfirmar_login(driver):
    return LoginPage(driver)