from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br")
navegador.find_element_by_name('q').send_keys("botafogo")
button = navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button.click()
