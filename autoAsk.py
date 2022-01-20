from datetime import datetime
import time


from selenium import webdriver
from getpass import getpass 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 2,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 2,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 2         # 1:allow, 2:block 
  })



driver =webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

driver.get("https://meet.google.com/")

def checker(s):
  if (len(driver.find_elements(By.XPATH, s)) != 0):
        return 0
  else:
        driver.implicitly_wait(10)
        checker(s)      


signin_btn=driver.find_element(By.XPATH, '/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a')
signin_btn.click()

enter_email =driver.find_element(By.XPATH, '//*[@id="identifierId"]')
#email=input("enter in your email  ")
enter_email.send_keys(email)

driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]').click()

checker('//*[@id="password"]/div[1]/div/div[1]/input')
enter_password =driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
#password=input("enter in your password  ")


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
enter_password.send_keys(password)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]')))
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]').click()

checker('//*[@id="i3"]')
meetlink=input("enter in your meet code ")
link_textbox =driver.find_element(By.XPATH, '//*[@id="i3"]')
link_textbox.send_keys(meetlink)


join_button=driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]')
join_button.click()

checker('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
driver.implicitly_wait(1000)
WebDriverWait(driver, 320).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')))
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()

checker('//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span')
driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span').click()

def print_list():
    checker("//div[@class='cS7aqe NkoVdd']")
    driver.implicitly_wait(20)
    all_spans = driver.find_elements_by_xpath("//div[@class='cS7aqe NkoVdd']")
    if(len(all_spans)>1):
        print("-----> list of participants as generated at time ")
        now = datetime.now()
        print("now time is ====", now)
        for span in all_spans:
            print(span.text)
    
        

def executeSomething():
    print_list()
    time.sleep(60*1)

while True:
    executeSomething()
    
#https://meet.google.com/$rpc/google.rtc.meetings.v1.MeetingSpaceService/SyncMeetingSpaceCollections
