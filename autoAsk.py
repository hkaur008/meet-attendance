from selenium import webdriver
from getpass import getpass 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

meetlink=input("enter in your meet link")

options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver =webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://meet.google.com/")

link_textbox =driver.find_element(By.XPATH, '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/input')

link_textbox.send_keys(meetlink)
join_button=driver.find_element(By.XPATH, '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/a/button')

join_button.click()


