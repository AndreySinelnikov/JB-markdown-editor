def get_text():
    return input("Text:")

def plain():
    return get_text()

def header():
    level = input("- Level:")
    if level in "123456":
        return f"{'#' * int(level)} {get_text()}\n"  # \n так как "should switch to a new line automatically"
    else:
        print("The level should be within the range of 1 to 6")

def bold():
    return f"**{get_text()}**"

def italic():
    return f"*{get_text()}*"

def inline_code():
    return f"`{get_text()}`"

def link():
    label = input("Label:")
    url = input("URL:")

    return f"[{label}]({url})"

def new_line():
    return "\n"

def create_list(ordered=False):
    rows = 0
    text = ""

    while rows < 1:
        rows = int(input("Number of rows: "))
        if rows < 1:
            print("The number of rows should be greater than zero")

        for i in range(1, rows + 1):
            row = input(f"Row #{i}: ")

            if ordered:
                text += f"{i}. {row}\n"
            else:
                text += f"* {row}\n"

    return text

def ordered_list():
    return create_list(ordered=True)

def main():
    result = ""

    formatters = {"plain": plain, "header": header, "bold": bold,
                  "italic": italic, "inline-code": inline_code, "link": link,
                  "line-break": new_line, "ordered-list": ordered_list,
                  "unordered-list": create_list}

    commands = ("!help", "!done")

    while True:
        user_choice = input("- Choose a formatter:")
        if user_choice in formatters:
            result += formatters[user_choice]()
            print(result)
        elif user_choice == "!help":
            print("Available formatters:", ' '.join(formatters))
            print("Available commands: ", ' '.join(commands))
        elif user_choice == "!done":
            break
        elif user_choice not in formatters:
            print("Unknown formatter or command. Please try again.")

if __name__ == "__main__":
    main()

