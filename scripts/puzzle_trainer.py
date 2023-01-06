import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Kazutadashi\\Documents\\Programming\\repos\\lichess-tactics-assistant\\UserData")
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path='C:\\Users\\Kazutadashi\\Documents\\Programming\\webdrivers\\chromedriver.exe', options=options)
driver.implicitly_wait(10)
driver.get("https://lichess.org/training/cxhfh")

# checks to see if a completion message shows up, returns the first one it gets whether its a failure or a success.
completion_status = driver.find_element_by_css_selector(".puzzle__feedback.fail, .complete")
if completion_status.text == "Success!":
    print("Puzzle was passed.")
else:
    print("Puzzle was failed.")