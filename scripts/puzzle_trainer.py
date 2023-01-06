import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# with open('lichess-tactics-assistant\data\puzzle_links.txt') as file:
#     puzzle_links = [line.rstrip() for line in file]

puzzle_links = ["https://lichess.org/training/cxhfh",
                "https://lichess.org/training/I8tZV",
                "https://lichess.org/training/VQdq2",
                "https://lichess.org/training/0a4R8"]

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Kazutadashi\\Documents\\Programming\\repos\\lichess-tactics-assistant\\UserData")
options.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path='C:\\Users\\Kazutadashi\\Documents\\Programming\\webdrivers\\chromedriver.exe', options=options)



def try_puzzle(puzzle_link):
    driver.implicitly_wait(600)
    driver.get(puzzle_link)
    # checks to see if a completion message shows up, returns the first one it gets whether its a failure or a success.
    completion_status = driver.find_element_by_css_selector(".puzzle__feedback.fail, .complete")
    if completion_status.text == "Success!":
        print("Puzzle was passed.")
        return True
    else:
        print("Puzzle was failed.")
        return False

while len(puzzle_links) > 0:
    random_list_index = random.randint(0, len(puzzle_links)-1)
    current_puzzle = puzzle_links[random_list_index]
    try_puzzle(current_puzzle)
    input("Press enter to continue to next puzzle.")
    puzzle_links.pop(random_list_index)
