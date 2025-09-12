'''Q5. Quiz Game with File Storage

Problem:
Create a quiz game using file handling.

Questions are stored in a file (questions.txt) in format:
"question|option1,option2,option3|answer"

Program reads questions and asks user.

User’s answers are stored in answers.txt.

At the end, show:

Score.

Correctly answered questions (set).

Summary dictionary {question: chosen_answer}.

Handle exceptions:

Invalid file format.

File not found.

Invalid user input.'''


questions = []
options = []
answers = []


def get_questions():
    try:
        with open("Files\\questions.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    raise ValueError("Invalid file format in questions.txt")
                question, option, answer = parts
                questions.append(question)
                options.append(option)
                answers.append(answer)
    except FileNotFoundError:
        print("Questions file not found!")
    except ValueError as ve:
        print(ve)


def get_user_answers():
    open("Files\\answers.txt", "w").close()

    for i in range(len(questions)):
        while True:
            print(f"\nQ{i+1}. {questions[i]}")
            temp = options[i].strip().split(",")
            for opt in temp:
                print(f"- {opt}")
            try:
                user_answer = input(f"Answer for Q{i+1}: ").strip().lower()
                if user_answer in [opt.lower() for opt in temp]:
                    try:
                        with open("Files\\answers.txt", "a") as f:
                            f.write(user_answer + "\n")
                    except FileNotFoundError:
                        print("Answers file not found!")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Not a valid option!")


def summary():
    score = 0
    correct = []
    summary = {}
    user_answers = []
    try:
        with open("Files\\answers.txt") as f:
            for line in f:
                a = line.strip()
                user_answers.append(a)

        for i in range(len(questions)):
            if i < len(user_answers):
                if user_answers[i].lower() == answers[i].lower():
                    score += 1
                    correct.append(questions[i])
                summary[questions[i]] = user_answers[i]
            else:
                summary[questions[i]] = "No Answer"

        print(f"\n--- Result ---")
        print(f"Score: {score}/{len(answers)}")
        print(f"Correctly Answered Questions: {set(correct)}")
        print(f"Summary Dictionary: {summary}")

    except FileNotFoundError:
        print("Answers file not found!")


get_questions()
get_user_answers()
summary()
