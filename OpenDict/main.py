from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from init_driver import driver
from search_routine import split
from search_routine import search_routine

print("Thanks for using zyTranslate CN-EN!")

driver.get("https://www.linguee.com/chinese-english")
lang_dropdown = driver.find_element_by_class_name('ui-selectmenu-text')
lang_dropdown.click()
lang_option = driver.find_element_by_id('ui-id-3')
lang_option.click()

search_string_raw = input("Input the phrase to search.")

search_string = split(search_string_raw)

final_sentence = ""
for search_term in search_string:
    final_sentence += (search_routine(search_term, 0))
    final_sentence += " "

print(final_sentence)




