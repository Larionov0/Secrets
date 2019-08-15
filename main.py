from os import system

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
    system("cls")
    ans = input("---=mAIN MENu=---\n1 - sign up\n2 - sign in\n3 - exit\n")
    if ans == "1":
        """Sign up"""
        # Input login
        word = "login"
        correct_input = False
        while True:
            system("cls")
            login = input(f"{' ' * 10}{'-'*20}\n{' ' * (9 - len(word))}Login |")
            if login == "stop":
                break
            if login in data:
                print("Try again!")
                input()
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        # Input password
        word = "password"
        correct_input = False
        while True:
            system("cls")
            print(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len('login'))}Login |{login}")
            password = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Password |")
            if password == "stop":
                break
            if len(password) < 6:
                print("Try again!")
                input()
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        # Choosing num of question
        word = "question"
        correct_input = False
        while True:
            system("cls")
            print("Choose the number of question (stop):")
            i = 1
            for question in questions_list:
                print(f"{i}. {question}")
                i += 1

            num_of_question = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Question |")
            if num_of_question == "stop":
                break

            if not num_of_question.isdigit() or int(num_of_question) - 1 >= len(questions_list):
                print("Icorrect number. Try again")
                input()
                continue

            num_of_question = int(num_of_question) - 1
            correct_input = True
            break
        if not correct_input:
            continue

        # Input answer
        word = "answer"
        correct_input = False
        while True:
            system("cls")
            print(questions_list[num_of_question])
            answer = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Answer |")
            if answer == "stop":
                break
            if answer == "":
                print("Try again")
                input()
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        data[login] = {
        "password": password,
        "question": num_of_question,
        "answer": answer,
        "secrets": {}
        }
        system('cls')
        print("Successful sign up!")
        input()

    elif ans == "2":
        """Sign in"""
        # Input login
        word = "login"
        correct_input = False
        while True:
            system("cls")
            login = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Login |")
            if login == "stop":
                break
            if login not in data:
                print("Try again!")
                input()
            else:
                correct_input = True
                break
        if not correct_input:
            continue

        # Input password
        word = "password"
        correct_input = False
        while True:
            system("cls")
            print(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len('login'))}Login |{login}")
            password = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Password |")
            if password == "stop":
                break
            if password == data[login]["password"]:
                correct_input = True
                break
            else:
                print("Try again! (Do you forget password?)")
                # Here must be code for password recovery
                input()
        if not correct_input:
            continue

        # Menu with secrets
        while True:
            system('cls')
            print("-" * 10 + "===" + login + "===" + "-" * 10)
            print("\nYour secrets:")
            i = 1
            for secret_name in data[login]["secrets"]:
                print(f"{i}. {secret_name}")
                i += 1
            print("-" * 30)
            ans = input("1 - new secret\n2 - edit secret\n3 - delete secret\n4 - delete account\n5 - leave account\n:")
            if ans == "1":
                # Input name of secret
                word = "name"
                correct_input = False
                while True:
                    system("cls")
                    secret_name = input(f"{' ' * 10}{'-' * 20}\n{' ' * (9 - len(word))}Name |")
                    if secret_name == "stop":
                        break
                    if secret_name == "":
                        print("Try again!")
                        input()
                    else:
                        correct_input = True
                if not correct_input:
                    continue

                text = input("Text:\n")
                data[login]["secrets"][secret_name] = text
                input("Secret added!\n")

            elif ans == "2":
                pass
            elif ans == "3":
                pass
            elif ans == "4":
                pass
            elif ans == "5":
                pass
            else:
                pass

    elif ans == "3":
        exit(0)
    else:
        pass
