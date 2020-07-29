# standard libs
import random

# third party libs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# just stuff
style_list =['fed_', 'bbold_','big_']

# functions bruh
def processor(input_title, input_artist):
    # init the browser
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://nickstyler.de/')

    # wait until the form loads
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.ID, "nickstyler"))
    )

    # decide our styles
    title_style = random.choice(style_list)
    artist_style = random.choice(style_list)
    print(title_style + ' ' + artist_style)

    # find our input
    input_field = browser.find_element_by_name('textin')
    input_field.click()

    # msn-ify the title
    input_field.send_keys(input_title)
    output_field = browser.find_element_by_id(title_style)
    output_title = output_field.get_attribute('value')

    # clear it
    input_field.clear()

    # msn-ify the artist
    input_field.send_keys(input_artist)
    output_field = browser.find_element_by_id(artist_style)
    output_artist = output_field.get_attribute('value')

    # we audi
    browser.close()

    # return it
    return output_title, output_artist