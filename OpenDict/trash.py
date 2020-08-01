from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

search_term = input("Input a word to search.")

chromedriver = "C:\\Webdrivers\\Chrome\\Version81\\chromedriver.exe"

driver = webdriver.Chrome(chromedriver)

driver.get("https://www.linguee.com/chinese-english")

lang_dropdown = driver.find_element_by_class_name('ui-selectmenu-text')

lang_dropdown.click()

lang_option = driver.find_element_by_id('ui-id-3')

lang_option.click()

linguee_search = driver.find_elements_by_tag_name('input')[0]

linguee_search.send_keys(search_term)

linguee_search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

words_list = driver.find_elements_by_xpath("//*[@class='dictLink featured']")

target_list = []
for word in words_list:
    target_list.append(word.get_attribute('innerHTML'))

print(target_list)

###########################

search_term = input("Input next word to search.")

linguee_search = driver.find_elements_by_tag_name('input')[0]
linguee_search.send_keys(Keys.BACKSPACE)
linguee_search.send_keys(search_term)

linguee_search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

words_list = driver.find_elements_by_xpath("//*[@class='dictLink featured']")

target_list = []
for word in words_list:
    target_list.append(word.get_attribute('innerHTML'))

print(target_list)