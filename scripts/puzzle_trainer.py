import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time
import keyboard

def get_puzzle(puzzle_link):
    driver.implicitly_wait(600)
    driver.get(puzzle_link)
    # checks to see if a completion message shows up, returns the first one it gets whether its a failure or a success.
    completion_status = driver.find_element_by_css_selector(".puzzle__feedback.fail, .complete")
    if completion_status.text == "Success!":
        return True
    else:
        return False

def start_run(rush_mode=False):
    numberCorrect = 0
    numberFailed = 0
    puzzlesAttempted = 0
    numberOfPuzzles = len(puzzle_links)
    
    start_time = time.time()
    while len(puzzle_links) > 0:
        
        # pick a random puzzle
        random_list_index = random.randint(0, len(puzzle_links)-1)
        current_puzzle = puzzle_links[random_list_index]

        puzzle_result = get_puzzle(current_puzzle)
        
        if puzzle_result == True:
            numberCorrect+=1
        else:
            numberFailed+=1
        puzzlesAttempted += 1
        
        # wait until key is pressed to go to next puzzle
        if rush_mode == False:
            keyboard.wait("a")
            print("'A' key was pressed. Going to the next puzzle.")

        print(f"[{puzzlesAttempted}/{numberOfPuzzles}] - {numberCorrect} Correct | {numberFailed} Failed.")
        
        puzzle_links.pop(random_list_index)
        end_time = time.time()

    time_taken = end_time - start_time
    time_format = "%M:%S"
    print(time_taken)
    print(f"-----------------\nCycle finished.\n\nAccuracy: {round(numberCorrect/numberOfPuzzles*100, 2)}%, \
        Time: {round((time_taken))} seconds. ({time.strftime(time_format, time.gmtime(time_taken))} minutes)")
    print(f"Goal time is 180 seconds. {time_taken-180} off goal.")


with open('lichess-tactics-assistant\data\puzzle_links.txt') as file:
    puzzle_links = [line.rstrip() for line in file]

puzzle_links = ["https://lichess.org/training/cxhfh",
                "https://lichess.org/training/I8tZV",
                "https://lichess.org/training/VQdq2",
                "https://lichess.org/training/0a4R8"]

# enables caching
options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Kazutadashi\\Documents\\Programming\\repos\\lichess-tactics-assistant\\UserData")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(executable_path='C:\\Users\\Kazutadashi\\Documents\\Programming\\webdrivers\\chromedriver.exe', options=options)






start_run(rush_mode=True)
driver.close()