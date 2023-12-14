import pytest
import time
from test_01 import realizar_login
from paginas.chamados import Chamados  # Certifique-se de importar a classe Chamados

def test_preencher_inf_novo_chamado(driver, login_info):

    # ========================== FLUXO DE CRIAÇÃO DE CHAMADO - CLIENTE ======================
    
    realizar_login(driver, login_info)  # Realiza o login uma vez
    Chamados(driver).botao_criar_chamados()  # Chama a função botao_criar_chamados na página de Chamados)
    Chamados(driver).verificar_link_criacao_chamado()
    Chamados(driver).preencher_organizacao()
    Chamados(driver).preencher_localizacao()
    Chamados(driver).preencher_categoria()
    Chamados(driver).preencher_tipo()
    Chamados(driver).preencher_titulo()
    Chamados(driver).preencher_descricao()
    Chamados(driver).botao_enviar()
    Chamados(driver).verificar_texto_chamado_criado()
    Chamados(driver).retornar_menu_chamadas()
