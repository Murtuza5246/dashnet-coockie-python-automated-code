from selenium import webdriver
import datetime
import time

from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait

CHROME_LOCATION = "E:\\Chrome development\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_LOCATION)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
available = driver.find_elements_by_css_selector(".grayed")
print(available)

def available_money_check() -> int:
    try:
        money_to_return = int(driver.find_element_by_id("money").text.replace(",", ""))
    except:
        money_to_return = int(driver.find_element_by_id("money").text)
    return money_to_return


def object_passer(index, item):
    return {"value": int(item.find_element_by_tag_name("b").text.split("-")[1].replace(" ", "").replace(",", "")),
            "index": index}


value_click = [object_passer(index, item) for index, item in enumerate(available[:8])][::-1]


def checking_through_the_list(current_money):
    returnning_index = 0
    got_the_big = True
    for item in value_click:
        if item["value"] <= current_money and got_the_big:
            returnning_index = item["index"]
            got_the_big = False
    return returnning_index


def clicking_the_clickable_object(index):
    clickable_list = [driver.find_element_by_id("buyCursor"), driver.find_element_by_id("buyGrandma"),
                      driver.find_element_by_id("buyFactory"), driver.find_element_by_id("buyMine"),
                      driver.find_element_by_id("buyShipment"), driver.find_element_by_id("buyAlchemy lab"),
                      driver.find_element_by_id("buyPortal"), driver.find_element_by_id("buyTime machine")]
    try:
        clickable_list[index].click()
        print(index)
    except ElementClickInterceptedException:
        print(index)
        print("failed to click the element!!")
    except StaleElementReferenceException:
        print(index)
        print("Stale error occurred!!")
    return


def check_which_to_click():
    current_money = available_money_check()
    clicking_the_clickable_object(checking_through_the_list(current_money))
    return


def current_milli_time():
    return round(time.time() * 1000)


while True:
    cookie.click()
    time_ = datetime.datetime.now()
    checking = round(float(str(time_).split(" ")[1].split(":")[2]))
    if checking % 5 == 0:
        time.sleep(1)
        print("triggering the click function!")
        check_which_to_click()

