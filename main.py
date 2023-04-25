import configparser
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Lendo as informações do arquivo de configuração
config = configparser.ConfigParser()
config.read('arquivo_novo.txt')

# Acessando o Centreon
driver = webdriver.Chrome()
driver.get('https://centreon-testes.sollobrasil.com.br/')
wait = WebDriverWait(driver, 10)
username_input1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Alias"]')))
password_input1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]')))

# Fazendo login
username_input1.send_keys('USER')
password_input1.send_keys('Password')
connect_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Connect"]')))
connect_button.click()
time.sleep(5)

# Navegando até a página de cadastro de hosts
driver.get('https://centreon-testes.sollobrasil.com.br/centreon/main.php?p=601&o=a')
time.sleep(5)

# Preenchendo os campos para cada host
for section in config.sections():
    host_name = config.get(section, 'host_name')
    alias = config.get(section, 'alias')
    address = config.get(section, 'address')
    # contact_groups = config.get(section, 'contact_groups')
    use = config.get(section, 'use')

    # Selecionando o template correto de acordo com o sistema operacional
    if 'Windows' in use:
        template = 'OS-Windows-SNMP-producao'
    elif 'Linux' in use:
        template = 'OS-Linux-SNMP-producao'
    else:
        template = 'Other_devices-producao'

    # a.Pressionando TAB 23 vezes
    for i in range(23):
        element = driver.switch_to.active_element
        element.send_keys(Keys.TAB)

    # b. Escrevendo a frase no campo onde o tab parar
    element = driver.switch_to.active_element
    element.send_keys(host_name)

    # Pressionando TAB e inserindo o valor de alias
    element = driver.switch_to.active_element
    element.send_keys(Keys.TAB)
    element.send_keys(alias)

    # Pressionando TAB e inserindo o valor de address
    element = driver.switch_to.active_element
    element.send_keys(Keys.TAB)
    element.send_keys(address)

    # Define a posição do mouse
    x, y = 700, 730
    x2, y2 = 700, 750

    # Move o mouse para a posição
    pyautogui.moveTo(x, y)

    # Clica na posição
    pyautogui.click(x, y)
    pyautogui.moveTo(x2, y2)
    pyautogui.click(x2, y2)

    # Escreve o template e aperta enter
    clktemplate = driver.switch_to.active_element
    clktemplate.send_keys(template)
    clktemplate.send_keys(Keys.ENTER)
    time.sleep(1)
    # Salvando o formulário
    x3, y3 = 1150, 320
    pyautogui.move(x3, y3)
    pyautogui.click(x3, y3)
    time.sleep(5)

    # Navegando até a página de cadastro de hosts
    driver.get('https://centreon-testes.sollobrasil.com.br/centreon/main.php?p=601&o=a')
    time.sleep(5)