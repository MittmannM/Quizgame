def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        print("---------------")
        for i in options[question_num-1]:
            print(i)
        print("\n")
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1


    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0



def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Score: " + str(score)+"%")


def play_again():
    response = input("Play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False



questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
                ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
                ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
                ["A. True", "B. False", "C. sometimes", "D. Whats Earth?"]]

new_game()

while play_again():
    new_game()

print("GuNa")
