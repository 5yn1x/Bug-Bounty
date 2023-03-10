from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# scrape = input("what page would you like to scrape?  ")

cdp =  "C:\developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=cdp)

driver.get("https://github.com/usernam121")
# driver.get(f"{scrape}")
repo = "https://github.com/usernam121"
# time.sleep(2)
res = driver.find_elements(By.CLASS_NAME, "repo")
# time.sleep(2)

links = []
final_link = []

def for_raw(second_page):
    driver.get(second_page)
    time.sleep(2)
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    # print(html)
    if "password" in html:
        print(f"found password {second_page}")


def loop(nex_page):
    global a
    driver.get(nex_page)
    time.sleep(1)
    res2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in res2:
        pass
        # print(a.text)
    if "py" in a.text:
        second_page = f"{nex_page}/blob/main/{a.text}"
        time.sleep(1)
        for_raw(second_page)

    if "js" in a.text:
        second_page = f"{nex_page}/blob/main/{a.text}"
        print(second_page)
    elif "php" in a.text:
        second_page = f"{nex_page}/blob/main/{a.text}"
        print(second_page)

    if "txt" in a.text:
        second_page = f"{nex_page}/blob/main/{a.text}"
        print(second_page)
    elif "php" in a.text:
        second_page = f"{nex_page}/blob/main/{a.text}"
        print(second_page)


for i in res:
    links.append(i.text)
# print(links)

for l in links:
    next_page = f"{repo}/{l}"
    final_link.append(next_page)
    loop(next_page)
# print(final_link)

driver.close()