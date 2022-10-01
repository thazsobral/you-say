import sys
from xml.dom.minidom import CharacterData

args = sys.argv[1:]
user_text = str(args[0])

try:
    match str(args[1]):
        case "penguim":
            character = [
                "    \\    __",
                "     \\-=(o '.",
                "        '.-.\\",
                "        /|  \\",
                "        '|  ||",
                "         _\_):,_"
            ]
        case "pikachu":
            character = [
                "      \\  \:.             .:/",
                "       \\  \``._________.''/ ",
                "        \\  \             / ",
                " .--.--, \\ / .':.   .':. \\",
                "/__:  /   \\| '::' . '::' |",
                "     / /   |`.   ._.   .'|",
                "    / /    |.'         '.|",
                "   /___-_-,|.\  \   /  /.|",
                "        // |''\.;   ;,/ '|",
                "        `==|:=         =:|",
                "           `.  _______  .'",
                "            `''       `''"
            ]
        case "bird":
            character = [
                "    \\  ,_,",
                "     \\(O,O)",
                "      (   )",
                "      -\"-\"------"
            ]
        case "dog":
            character = [
                " \\   /^ ^\\",
                "  \\ / 0 0 \\",
                "    V\ Y /V",
                "     / - \\",
                "    /    |",
                "   V__) ||",
            ]
        case "skull":
            character = [
                "\\     ___ (~ )( ~)",
                " \\   /   \_\ \/ /",
                "  \\ |   D_ ]\ \/",
                "   \\|   D _]/\ \\",
                "     \___/ / /\ \\",
                "          (_ )( _)"
            ]
        case "bug":
            character = [
                " \\     !__!",
                "  \\___(@)(-)",
                "     \.'||'./",
                "    -:  ::  :-",
                "    /'..''..'\\"
            ]
        case "hacker":
            character = [
"             \\  |       ",
"              \\ |     _/M\/MM\M/M\Mm,",
"               \\|    _YMMMMMMMMMMMM/",
"                    `MMMMMM/       \  ",
"                     MMM|   __    __/  ",
"                     YMM/ _/# \__/# \  ",
"                      (.   \__/  \__/  ",
"                       )       _,  |  ",
"                  _____/\     _   /   ",
"                      \  `._____,'",
"                       `..___(__",
"                                ``-.",
"                                    \\",
            ]
        case "man":
            character = [
                "  \\     ,.__",
                "   \\   ((_\)),",
                "    \\  | . . {",
                "     \\ (  _) )",
                "        \ _ /",
                "      __,\_/,__",
                "     / \ \^/_,_\\",
                "    |  | |&|   |\\",
                "    |  | |&|_o_| \\",
                "     \  \`&/   |"
            ]
        case "woman":
            character = [
" \\       ___.   ",
"  \\    /(()-/)  ",
"   \\  / /. . |\ ",
"    \\ ||  ]  )| ",
"      /|  -  || ",
"      /_\___/|, ",
"     |   \-/_,_\\",
"     |  :| |   |"
            ]
        case _:
            character = [
                "          \\   ^__^",
                "           \\  (oo)\\_______ ",
                "              (__)\\       )\\/\\",
                "                   ||--W |",
                "                   ||   ||",
                "                ````````````"
                ]
except IndexError:
    character = "cow"

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

container = [line, text, line]

for item in container:
    print(item)

for item in character:
    print(item)