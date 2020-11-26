from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import time
import random

def main(email, pwd, cvv):
  # open browser and login
  options = Options()
  options.page_load_strategy = 'eager'
  driver = webdriver.Chrome(options=options)
  wait = WebDriverWait(driver, 300)
  driver.get("https://www.walmart.com/account/login")
  driver.find_element_by_id("email").send_keys(email)
  driver.find_element_by_id("password").send_keys(pwd)
  driver.find_element_by_xpath("//*[@id='sign-in-form']/button[1]").click()

  time.sleep(5)
  actual_start = time.time()
  
  driver.get("https://www.walmart.com/ip/Sony-PlayStation-4-500GB-Slim-System-Black/406966077")

  start = time.time()
  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button")))
  time.sleep(random.uniform(0, 0.1))
  driver.find_element_by_css_selector("#add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button").click()
  
  # click checkout
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cart-root-container-content-skip > div:nth-child(1) > div > div.Cart-PACModal.standard-pac.pac-added.pac-new-ny.no-price-fulfillment.pac-vanilla-hf > div > div > div > div > div.Cart-PACModal-Body-right-rail.Grid-col.u-size-1.u-size-1-2-m.u-size-1-2-l > div > div > div.Grid-col.u-size-1-2.pos-actions-container > div.cart-pos-main-actions.s-margin-top > div.new-ny-styling.cart-pos-proceed-to-checkout > div > button.button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary")))
  time.sleep(random.uniform(0, 0.1))
  driver.find_element_by_css_selector("#cart-root-container-content-skip > div:nth-child(1) > div > div.Cart-PACModal.standard-pac.pac-added.pac-new-ny.no-price-fulfillment.pac-vanilla-hf > div > div > div > div > div.Cart-PACModal-Body-right-rail.Grid-col.u-size-1.u-size-1-2-m.u-size-1-2-l > div > div > div.Grid-col.u-size-1-2.pos-actions-container > div.cart-pos-main-actions.s-margin-top > div.new-ny-styling.cart-pos-proceed-to-checkout > div > button.button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary").click()

  # continue after checkout
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(1) > div > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div.CXO_fulfillment_continue > button")))
  time.sleep(random.uniform(0, 0.1))
  driver.find_element_by_css_selector("body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(1) > div > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div.CXO_fulfillment_continue > button").click()

  # delivery address
  # wait.until(EC.presence_of_element_located((By.ID, "firstName")))
  # driver.find_element_by_id("firstName").send_keys(str("Long"))
  # time.sleep(0.1)
  # driver.find_element_by_id("lastName").send_keys(str("Nguyen"))
  # time.sleep(0.1)
  # driver.find_element_by_id("phone").send_keys(str("6176503291"))
  # time.sleep(0.1)
  # driver.find_element_by_id("addressLineOne").send_keys(str("624 Yale Avenue North"))
  # time.sleep(0.1)
  # driver.find_element_by_id("addressLineTwo").send_keys(str("718"))
  # time.sleep(0.1)
  # driver.find_element_by_css_selector("body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div > form > div.arrange > div.arrange-fill.u-size-1-12-m > button").click()
  # time.sleep(0.1)

  # continue after checkout
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.arrange > div.arrange-fill.u-size-1-12-m > button")))
  time.sleep(random.uniform(0, 0.1))
  driver.find_element_by_css_selector("body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.arrange > div.arrange-fill.u-size-1-12-m > button").click()

  # input CVV
  wait.until(EC.presence_of_element_located((By.ID, "cvv-confirm")))
  time.sleep(random.uniform(0, 0.1))
  driver.find_element_by_id("cvv-confirm").send_keys(cvv)
  driver.find_element_by_css_selector("body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(3) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div:nth-child(2) > div > button").click()

  print(time.time() - start)
  print("Total time: " + str(time.time() - actual_start))

  while True:
    time.sleep(5)

if __name__ == "__main__":
  email, pwd, cvv = sys.argv[1], sys.argv[2], sys.argv[3]
  main(email, pwd, cvv)
