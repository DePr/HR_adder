import time
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path=r'path\to\geckodriver.exe')
driver.get("https://www.linkedin.com")



if driver.title == 'LinkedIn: Log In or Sign Up':
    username = driver.find_element_by_id("login-email")
    password = driver.find_element_by_id("login-password")

    username.send_keys("usermame")
    password.send_keys("password")

    driver.find_element_by_id("login-submit").click()

driver.find_element_by_id("mynetwork-tab-icon").click()
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("pymk-card__occupation"))

def scrolldown():
    count = 0
    scroll_pause_time = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while count < 50:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        count += 1


def click_button():
    for ele in driver.find_elements_by_xpath("//div[@class='pymk-card ember-view']"):
        css_id = ele.get_attribute("id")
        element = driver.find_element_by_xpath(
            "//div[@id='" + css_id + "']/div/a/span[@class='pymk-card__occupation pymk-card__occupation--card-layout "
                                     "block m0 Sans-13px-black-55%']")
        pattern = re.compile("(?i)(HR|IT Recruiter|IT Recruitment|IT Headhunter|Recruitment)")
        if pattern.match(element.text):
            try:
                driver.find_element_by_xpath("//div[@id='" + css_id + "']/div/button").click()
                print('click')
            except:
                pass
        else:
            continue


def work():
    scrolldown()
    time.sleep(3)
    click_button()
    work()


if __name__ == '__main__':
    work()
