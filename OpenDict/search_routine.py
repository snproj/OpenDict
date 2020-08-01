from init_driver import driver
from selenium.webdriver.common.keys import Keys

def split(search_string):
    return [search_term for search_term in search_string]

def search_routine(search_term, index):
    try:
        driver.implicitly_wait(2)
        linguee_search = driver.find_elements_by_tag_name('input')[0]
        linguee_search.send_keys(Keys.BACKSPACE)
        linguee_search.send_keys(search_term)
        linguee_search.send_keys(Keys.RETURN)

        words_list = driver.find_elements_by_xpath("//*[@class='dictLink featured']")

        target_list = []
        for word in words_list:
            target_list.append(word.get_attribute('innerHTML'))

        print(search_term + ": ")
        print(target_list)
        return target_list[index]
    except:
        print("Nothing found for " + search_term)
        return search_term
