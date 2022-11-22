from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

p_path = r"C:\Users\Connor\Coding\Python\Scripts\bamboo_auto\bamboop.txt"
e_path = r"C:\Users\Connor\Coding\Python\Scripts\bamboo_auto\bambooe.txt"
login_path = r"C:\Users\Connor\Coding\Python\Scripts\bamboo_auto\bamboologin.txt"

with open(p_path, 'r') as myfile:  
    password = myfile.read().replace('\n', '')
with open(e_path, 'r') as myfile:  
    email = myfile.read().replace('\n', '')
with open(login_path, 'r') as myfile:  
    login_url = myfile.read().replace('\n', '')
hours = 7.5

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)

driver.get(login_url)
driver.find_element("id", "lemail").send_keys(email)
driver.find_element("id","password").send_keys(password)
driver.find_element(By.CLASS_NAME,"login-actions").click()
driver.find_element(By.XPATH,"//span[.='Yes, Trust this Browser']").click()
driver.implicitly_wait(30) 
driver.find_element(By.XPATH,"//span[.='Enter Time Worked']").click()
driver.find_element("id","hoursWorked").send_keys(hours)
driver.find_element(By.CLASS_NAME,"fab-SelectToggle__toggleButton").click()
driver.find_element(By.XPATH,"//div[.='TSI Bench']").click()
driver.find_element(By.XPATH,"//span[.='Save']").click()
driver.close()
driver.quit() 
