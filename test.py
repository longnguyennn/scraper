from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
  # prompt email + password
  email = raw_input("email: ")
  password = raw_input("password: ")

  # open browser and login
  driver = webdriver.Chrome()
  driver.get("https://www.walmart.com/account/login")
  driver.find_element_by_id("email").send_keys(email)
  driver.find_element_by_id("password").send_keys(password)
  login_button = driver.find_element_by_xpath("//*[@id='sign-in-form']/button[2]")
  print(login_button)
  login_button.click()



if __name__ == "__main__":
  main()