def input_checker(prompt):
    gamer_answer = input(prompt)

    if len(gamer_answer) > 1:
        print('Введите только одну букву')
        gamer_answer = input(prompt)

    while any(char.isdigit() for char in gamer_answer):
        print('Введите текст без цифр')
        gamer_answer = input(prompt)

    return gamer_answer
