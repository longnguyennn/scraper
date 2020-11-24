from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

def main():
  # prompt email + password
  email = str(input("email: "))
  password = str(input("password: "))

  # open browser and login
  driver = webdriver.Chrome()
  driver.get("https://www.walmart.com/account/login")
  driver.find_element_by_id("email").send_keys(email)
  driver.find_element_by_id("password").send_keys(password)
  driver.find_element_by_xpath("//*[@id='sign-in-form']/button[1]").click()

  time.sleep(5)

  # keep refreshing the page until the buy button appear
  while True:
    driver.get("https://www.walmart.com/ip/Marvel-s-Spider-Man-Miles-Morales-Ultimate-Launch-Edition-Sony-PlayStation-5/795159051")
    try:
      buy_button = driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[2]/select")
      break
    except NoSuchElementException as ex:
      continue

  # buy 2 ps5
  Select(driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[2]/select")).select_by_visible_text('2')
  driver.find_element_by_xpath("//*[@id='add-on-atc-container']/div[1]/section/div[1]/div[3]/button/span").click()

  while True:
    time.sleep(5)



if __name__ == "__main__":
  main()
