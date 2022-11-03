import urllib.request
import json
import time

#id_list = ['cv0SQ', '1MbZR', '7XAG4']
id_list = ['1TmlJ']
id = '1MbZR'

def create_thematic_dict(id_list):
    theme_dict = {}
    for id in id_list:
        time.sleep(.2)
        with urllib.request.urlopen("https://lichess.org/api/puzzle/" + id) as puzzle_url:
            puzzle_data = json.loads(puzzle_url.read().decode())
        theme_dict[id] = puzzle_data['puzzle']['themes']
    return theme_dict
        
def add_puzzles(filename, puzzles):
    try:
        with open(filename) as f:
            list_obj = json.load(f)
            print("json loaded.")
    except:
        list_obj = {}
        print("json failed to load")
    
    list_obj.update(puzzles)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(list_obj, f, indent=4)

puzzles = create_thematic_dict(id_list)
print(puzzles)


add_puzzles('lichess-tactics-assistant\puzzles.json', puzzles)



