import sys

args = sys.argv[1:]
user_text = str(args[0])
words = user_text.split()

if len(words) > 8:
    first_line = " ".join(words[:len(words)//2 + 1])
    second_line = " ".join(words[len(words)//2 + 1:])
    line = (len(first_line)+4) * "-"
    padding = (len(first_line) - len(second_line)) * " "
    text = "| " + first_line + " |\n| " + second_line + padding + " |"
else:
    line = (len(user_text)+4) * "-"
    text = "| "+user_text+" |"

cow = ["          \\ | ^__^", "           \\| (oo)\\______ ", "              (__)\\      )\\/\\", "                   ||--W |", "                   ||   ||", "                ````````````"]

container = [line, text, line]

for item in container:
    print(item)

for item in cow:
    print(item)