import urllib.request
import json
import time
def load_ids(filepath: str) -> list:
    """Loads a text file containing links to lichess puzzles and returns a list of puzzle IDs.

    Parameters
    ----------
    filepath : str
        The filepath for where the links are stored
    """
    ids = []
    
    with open(filepath) as f:
        for line in f:
            ids.append(line.rstrip('\n')[-5:])
    return ids


def create_thematic_dict(ids: list) -> dict:
    """Creates a dictionary with the ID as the key, and the themes as the values.

    Parameters
    ----------
    ids : list
        The list of Lichess puzzle IDs
    """
    theme_dict = {}
    
    for id in ids:
        print(f'Making API call for ID: {id}')
        # sleep added to prevent fast API calls
        time.sleep(.1)
        with urllib.request.urlopen("https://lichess.org/api/puzzle/" + id) as puzzle_url:
            puzzle_data = json.loads(puzzle_url.read().decode())

        theme_dict[id] = puzzle_data['puzzle']['themes']
        print(f'Added {id} successfully.')

    return theme_dict


def add_puzzles(filepath: str, new_puzzles: dict) -> None:
    """Adds the new puzzles to the existing JSON file for later analysis

    Parameters
    ----------
    filepath : str
        The path to the puzzle JSON file

    new_puzzles : dict
        The dictionary that contains the new puzzleid:[themes] combo.
    """
    
    try:
        with open(filepath) as f:
            existing_puzzles = json.load(f)
            print("[+] Loaded JSON successfully")
    except:
        print("[-] JSON failed to load")
    
    existing_puzzles.update(new_puzzles)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing_puzzles, f, indent=4)


def check_duplicates(new_id_list: list, filepath: str) -> list:
    """Checks for duplicate IDs so we do not make API calls with them
    """

    new_ids = []

    with open(filepath) as f:
        existing_puzzles = json.load(f)
    
    for id in new_id_list:
        if id in [existing_id for existing_id in existing_puzzles]:
            pass
        else:
            new_ids.append(id)
    
    # we return all except the last line because it is a new line
    if new_ids == ['']:
        print('[x] No new puzzles to add')
        return []

    print(f'New puzzles found: {new_ids}')
    return new_ids





if __name__ == "__main__":

    #load all the puzzles from the links saved in the text file
    id_list = load_ids('lichess-tactics-assistant\data\puzzle_links.txt')
    print(f'[+] Loaded IDs')

    # check for duplicates, and save the new ones
    print(f'[-] Checking duplicates')
    ids_to_be_added = check_duplicates(id_list, 'lichess-tactics-assistant\data\puzzles.json')
    
    # get themes for the ids
    puzzles = create_thematic_dict(ids_to_be_added)

    # make calls to the API and update the JSON file
    add_puzzles('lichess-tactics-assistant\data\puzzles.json', puzzles)

