from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

numero_oab = 24045

driver = webdriver.Chrome()
driver.get('https://pje-consulta-publica.tjmg.jus.br/')
sleep(5)

campo_oab = driver.find_element(By.XPATH, '//*[@id="fPP:Decoration:numeroOAB"]')
campo_oab.send_keys(numero_oab)

dropdown_estados = driver.find_element(By.XPATH, '//*[@id="fPP:Decoration:estadoComboOAB"]')
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SC')

botao_pesquisar = driver.find_element(By.XPATH, '//*[@id="fPP:searchProcessos"]')
botao_pesquisar.click()
sleep(5)

processos = driver.find_elements(By.XPATH, '//*[@id="fPP:processosTable:1532818:j_id245"]/a/b')
for i in processos:
    i.click()
    sleep(5)
    janelas = driver.window_handles
    driver.switch_to.window(janelas[-1])
    driver.set_window_size(1920, 1080)
    numero_processo = driver.find_elements(By.XPATH, '//*[@id="j_id132:processoTrfViewView:j_id138"]/div/div[2]/div')
    numero_processo = numero_processo[0]
    numero_processo = numero_processo.text

    data_distribuição = driver.find_elements(By.XPATH, '//*[@id="j_id132:processoTrfViewView:j_id150"]/div/div[2]')
    data_distribuição = data_distribuição[0]
    data_distribuição = data_distribuição.text

    movimentacoes = driver.find_elements(By.XPATH, '//*[@id="j_id132:processoEventoPanel_body"]//tr[contains(@class,"rich-table-row")]//td//div//div//span')
    lista_movimentacoes = []
    for i in movimentacoes:
        lista_movimentacoes.append(i.text)