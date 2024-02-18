def cipher(text, sdvig, operation):
    alphabet_list = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]
    new_text = ""

    if operation == 1:
        sdvig *= -1
    
    for c in text:
        alphabet = ""
        
        for item in alphabet_list:
            if c in item:
                alphabet = item

        if alphabet != "":
            index = alphabet.find(c)
            new_index = (index + sdvig) % len(alphabet)
            new_text += alphabet[new_index]
        else:
            new_text += c
    
    return new_text



ui = {
    "ru": [
        "Введите ваш текст: ",
        "Введите сдвиг: ",
        "1 - Расшифровать, 2 - Зашифровать \nЧто сделать: ",
        "Нужно ввести 1 или 2!",
        "Ошибка! Нужно ввести число!",
        "1 - Повторить, 2 - Выход \nЧто сделать: "
    ],
    "en": [
        "Enter your text: ",
        "Enter shift: ",
        "1 - Decrypt, 2 - Encrypt \nWhat to do: ",
        "You have to enter 1 or 2!",
        "Error! You must enter a number!",
        "1 - Repeat, 2 - Exit \nWhat to do: "
    ]
}

while True:
    lang = input("RU/EN: ").lower()
    print()
    if lang in ui:
        break

while True:
    text = input(ui[lang][0])
    print()

    while True:
        try:
            sdvig = int(input(ui[lang][1]))
            print()
            break
        except ValueError:
            print(ui[lang][4])
            print()

    while True:
        try:
            operation = int(input(ui[lang][2]))
            if not 1 <= operation <= 2:
                raise Exception(ui[lang][3])
            print()
            break
        except ValueError:
            print(ui[lang][4])
            print()
        except Exception as e:
            print(e)
            print()

    print(cipher(text, sdvig, operation))
    print()

    while True:
        try:
            choise = int(input(ui[lang][5]))
            if not 1 <= choise <= 2:
                raise Exception(ui[lang][3])
            print()
            break
        except ValueError:
            print(ui[lang][4])
            print()
        except Exception as e:
            print(e)
            print()
    
    if choise == 2:
        break