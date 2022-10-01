def make_phrase(text):
    words = text.split()

    if len(words) > 8:
        first_line = " ".join(words[:len(words)//2 + 1])
        second_line = " ".join(words[len(words)//2 + 1:])
        line = (len(first_line)+4) * "-"
        padding = (len(first_line) - len(second_line)) * " "
        text = "| " + first_line + " |\n| " + second_line + padding + " |"
    else:
        line = (len(text)+4) * "-"
        text = "| "+text+" |"

    return [line, text, line]