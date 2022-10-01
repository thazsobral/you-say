import sys

from characters import choose_character
from phrase import make_phrase

args = sys.argv[1:]
user_text = str(args[0])

character = choose_character(str(args[1]))

container = make_phrase(user_text)

for item in container:
    print(item)

for item in character:
    print(item)