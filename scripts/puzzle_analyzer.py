import json

BASIC_MOTIFS = ['advancedPawn', 'attackingF2F7', 'capturingDefender', 'discoveredAttack', 'doubleCheck', 'exposedKing', 'fork', 'hangingPiece', 'kingsideAttack',
                'pin', 'queensideAttack', 'sacrifice', 'skewer', 'trappedPiece']

ADVANCED_MOTIFS = ['attraction', 'clearance', 'defensiveMove', 'deflection', 'interference', 'intermezzo', 'quietMove', 'xRayAttack', 'zugzwang']

def count_themes(filepath: str) -> dict:
    """Counts how many times a specific theme shows up in the entire list of puzzles. 

    This function is used to count how many themes show up in all of our failed or slowed puzzles to
    better show which themes the player needs to focus on more, since they are missing many puzzles with 
    this specific theme.

    Parameters
    ----------
    filepath : str
        The filepath to the JSON file that contains the puzzles and their corresponding themes
    """

    with open(filepath) as f:
        puzzles = json.load(f)

    all_themes = []
    for k in puzzles:
        all_themes += puzzles[k]
    
    # Counts how many times each theme shows up
    occurrences = {item: all_themes.count(item) for item in all_themes}

    # Sorts a dictionary to show the most to least occurrences of themes
    ranked_occurrences = {k: v for k,v in sorted(occurrences.items(), key=lambda item:item[1], reverse=True)}
    return ranked_occurrences 


def restrict_motifs(tactical_themes: dict) -> dict:
    """Removes all themes that are not basic tactical motifs
    """
    themes_to_delete = []
    for theme in tactical_themes:
        if theme not in BASIC_MOTIFS and theme not in ADVANCED_MOTIFS:
            #print(f'The theme: "{theme}" is not a basic or advanced motif. Deleting theme.')
            themes_to_delete.append(theme)
        else:
            pass
            #print(f'The theme: "{theme}" is a basic or advanced motif. Saving theme.')
        
    for theme in themes_to_delete:
        del tactical_themes[theme]
    #print(tactical_themes)
    return tactical_themes



if __name__ == "__main__":
    
    themes = count_themes('lichess-tactics-assistant\data\puzzles.json')
    
    restricted_themes = themes.copy()
    restricted_themes = restrict_motifs(restricted_themes)

    print(themes, '\n', restricted_themes)
