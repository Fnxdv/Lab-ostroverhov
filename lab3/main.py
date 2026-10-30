import random
from words_data import HELP_TEXT, TIPS

random.seed(46)

def show_help():
    print(HELP_TEXT)
def count_words(text):
    return len(text.split())
def count_chars(text, with_spaces=True):
    if with_spaces:
        return len(text)
    return len(text.replace(" ", ""))
def random_tip():
    print(random.choice(TIPS))

def process_command(command, words, chars):
    running = True

    if command == "":
        print("Введите Команду: <команда>")

    elif command.startswith("add"):
        text = command[4:].strip()

        words += count_words(text)
        chars += count_chars(text, False)

        print(f"Слова: {words}, Буквы: {chars}")

    elif command == "report":
        print(f"Слова: {words}, Буквы: {chars}")

    elif command == "help":
        show_help()

    elif command == "tip":
        random_tip()

    elif command == "exit":
        running = False

    else:
        print("Неизвестная команда")

    return words, chars, running

words = 0
chars = 0
running = True

while running:
    command = input("Введите Команду: ").strip()
    words, chars, running = process_command(command, words, chars)