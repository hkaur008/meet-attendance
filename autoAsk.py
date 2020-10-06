from datetime import datetime


from selenium import webdriver
from getpass import getpass 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




driver =webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://meet.google.com/")
driver.maximize_window()


signin_btn=driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a')
signin_btn.click()

enter_email =driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email=input("enter in your email  ")
enter_email.send_keys(email)

driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]').click()


wait = WebDriverWait(driver, 300) 
wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))

enter_password =driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password=input("enter in your password  ")
enter_password.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]').click()

wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="i3"]')))
meetlink=input("enter in your meet code ")
link_textbox =driver.find_element(By.XPATH, '//*[@id="i3"]')
link_textbox.send_keys(meetlink)


join_button=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]')
join_button.click()

wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')))
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')))
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()

wait = WebDriverWait(driver, 1000)
wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span')))
driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span').click()



all_spans = driver.find_elements_by_class_name('cS7aqe NkoVdd')
print("  --------------->list of participants as generated at time <-------------")


now = datetime.now()
print("now time is  =", now)

for span in all_spans:
    print("    "+span.text)


