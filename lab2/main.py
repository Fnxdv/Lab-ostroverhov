words = 0
chars = 0
flag = True
while flag:
    sentence = input("Введите Команду: ").strip()
    if sentence == "":
                print("Введите Команду: <команда>")
                continue
    if sentence.startswith("add"):
        sentence = sentence[3:].strip()
        if sentence == "":
            print(f"Слова: {words}, Буквы: {chars}")
            continue
        else:
            words += sentence.count(" ") + 1
            chars += len(sentence.replace(" ", ""))
            print(f"Слова: {words}, Буквы: {chars}")
    if sentence == "report":
        print(f"Слова: {words}, Буквы: {chars}")
    if sentence == "exit":
         flag = False

