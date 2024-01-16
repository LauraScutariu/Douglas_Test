from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://www.douglas.ro/account/login')

# cu sleep putem pune pauza de cateva secunde
sleep(5)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')