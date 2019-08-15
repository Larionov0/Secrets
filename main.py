data = {
    "login": {
        "password": "PSWRD",
        "question": 2,
        "answer": "lol",
        "secrets": {
            "secret1": "text1"
        }
    },
}

questions_list = [
    "What was color of your first car in past life?",
    "Who will be your next wife in future life?",
    "Best friend-animal?"
]


while True:
    ans = input("1 - sign up\n2 - sign in\n3 - exit\n")
    if ans == "1":
        """Sign up"""
        # Input login
        word = "login"
        correct_input = False
        while True:
            login = input(f"{' ' * 10}{'-'*20}\n{' ' * (9 - len(word))}Login |")
            if login == "stop":
                break
            if login in data:
                print("Try again!")
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        # Input password
        word = "password"
        correct_input = False
        while True:
            password = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Password |")
            if password == "stop":
                break
            if len(password) < 6:
                print("Try again!")
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        # Choosing num of question
        word = "question"
        correct_input = False
        while True:
            print("Choose the number of question (stop):")
            i = 1
            for question in questions_list:
                print(f"{i}. {question}")
                i += 1

            num_of_question = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Question |")
            if num_of_question == "stop":
                break

            if not num_of_question.isdigit() or int(num_of_question) >= len(questions_list):
                print("Icorrect number. Try again")
                continue

            num_of_question = int(num_of_question)
            correct_input = True
            break
        if not correct_input:
            continue

        # Input answer
        word = "answer"
        correct_input = False
        while True:
            answer = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Answer |")
            if answer == "stop":
                break
            if answer == "":
                print("Try again")
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        print(login, password, num_of_question, answer)




    elif ans == "2":
        pass
    elif ans == "3":
        exit(0)
    else:
        pass
