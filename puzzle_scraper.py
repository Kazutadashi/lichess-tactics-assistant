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
            ids.append(line[-6:-1])
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
        # sleep added to prevent fast API calls
        time.sleep(.1)
        with urllib.request.urlopen("https://lichess.org/api/puzzle/" + id) as puzzle_url:
            puzzle_data = json.loads(puzzle_url.read().decode())

        theme_dict[id] = puzzle_data['puzzle']['themes']

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
            print("[+] JSON loaded successfully.")
    except:
        print("[-] JSON failed to load.")
    
    existing_puzzles.update(new_puzzles)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing_puzzles, f, indent=4)


if __name__ == "__main__":

    id_list = load_ids('lichess-tactics-assistant\puzzle_links.txt')
    puzzles = create_thematic_dict(id_list)

    add_puzzles('lichess-tactics-assistant\puzzles.json', puzzles)

