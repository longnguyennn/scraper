from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def main():
  # prompt email + password
  email = raw_input("email: ")
  password = raw_input("password: ")

  # open browser and login
  driver = webdriver.Chrome()
  driver.get("https://www.walmart.com/account/login")
  driver.find_element_by_id("email").send_keys(email)
  driver.find_element_by_id("password").send_keys(password)
  driver.find_element_by_xpath("//*[@id='sign-in-form']/button[1]").click()

  # keep refreshing the page until the buy button appear
  while True:
    driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")
    try:
      buy_button = driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[2]/select")
      break
    except NoSuchElementException as ex:
      continue

  # buy 2 ps5
  driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[2]/select").selectByIndex(1)
  driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[2]/select").click()

  while True:
    time.sleep(5)



if __name__ == "__main__":
  main()