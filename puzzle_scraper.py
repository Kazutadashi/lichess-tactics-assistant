import urllib.request
import json

id = '1MbZR'
with urllib.request.urlopen("https://lichess.org/api/puzzle/" + id) as puzzle_url:
    puzzle_data = json.loads(puzzle_url.read().decode())

print(puzzle_data['puzzle']['themes'])