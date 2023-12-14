from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pytest


class Chamados:
    def __init__(self, driver):
        self.driver = driver

    def botao_criar_chamados(self):
        # Espera até que o modal obscuring desapareça (substitua 'seletor_do_modal' pelo seletor apropriado)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, 'seletor_do_modal'))
            )
        except TimeoutException:
            pytest.fail("Modal ainda visível após o tempo limite estendido.")

        # Agora você pode clicar no botão de chamados
        elemento_chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/main/div/div[1]/div[1]/a'))
        )
        self.driver.execute_script("arguments[0].click();", elemento_chamados)  # Use JavaScript para clicar no botão
        time.sleep(4)

    def preencher_organizacao(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[1]/div/div/div"))
        ).click()

        combo_box_option = self.driver.find_element(By.ID, "combo-box-option-0")
        combo_box_option.click()

    def preencher_categoria(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[3]/div/div/div"))
        ).click()

        combo_box_option2 = self.driver.find_element(By.ID, "combo-box-option-1")
        combo_box_option2.click()

    def preencher_localizacao(self):
        time.sleep(4)
        combo_boxloc = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[2]/div/div/div"))
        ).click()

        time.sleep(3)

        combo_boxloc2 = self.driver.find_element(By.ID, "combo-box-option-1")
        combo_boxloc2.click()
        time.sleep(3)

    def preencher_tipo(self):
        time.sleep(3)

        combo_boxtipo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div/form/div/div[4]/div/div/div"))
        )
        combo_boxtipo.click()

        combo_boxloc2 = self.driver.find_element(By.ID, "combo-box-option-1")
        combo_boxloc2.click()

    def preencher_titulo(self):
        elemento_titulo = self.driver.find_element(By.ID, 'title')
        elemento_titulo.send_keys("PAROU DE FUNCIONAR")
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento_titulo)

    def preencher_descricao(self):
        self.driver.find_element(By.CLASS_NAME,'ql-editor').send_keys("monitor Não liga 3 - aut")

    def botao_enviar(self):
        # Esperar até que o botão de envio esteja visível e clicável
        elemento_enviar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.MuiButton-contained'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento_enviar)
        elemento_enviar.click()

    def retornar_menu_chamadas(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/button[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/nav/a[1]/div[2]/span').click()

    def verificar_texto_chamado_criado(self):
        mensagem_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/main/div[2]/div/div[2]/span"))
        )
        mensagem_texto = mensagem_elemento.text
        assert "Cadastrado com sucesso!" in mensagem_texto, "A mensagem esperada não foi encontrada"
        print("Mensagem exibida com sucesso!")

    def verificar_link_criacao_chamado(self):

        link_esperado = "https://cmtech.2do.homologa.mexx.ai/pt/called-registration-client"  # Substitua pelo link que você espera
        link_atual = self.driver.current_url
        assert link_esperado in link_atual, f"O link atual não corresponde ao esperado. Esperado: {link_esperado}, Atual: {link_atual}"

