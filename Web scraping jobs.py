import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as psd

#Establecer diccionario de trabajos
job_titles = []
job_description = []

#Establecer WebDriver
driver = webdriver.Firefox()

country = "MX"
next_page_exists = True
count = 0
captcha_active = False
page = 1

#Definir URL de inicio
start_url = "https://mx.indeed.com/jobs?q=python&l=remoto".format((page-1)*10)

#Visitar página
driver.get()

while next_page_exists:
    # Antes de pasar a cualquier página se deben cerrar los pop ups
    soup = BeautifulSoup(driver.page_source, "html.parser")
    time.sleep(5)
    pop_check = soup.find("div", {"id":"popover-foreground"})
    if pop_check is not None:
        print("Pop up found.")
        driver.back()
        driver.forward()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")



