'''Q3. Quiz Game with Exception Handling

Problem:
Design a multiple-choice quiz game.

Store questions in a list of dictionaries, each containing:

question (string),

options (tuple of choices),

answer (correct option string).

Use a loop to display questions one by one.

User enters their choice:

If choice not in options, raise and handle a ValueError.

If input is not a string, handle TypeError.

Keep score of correct answers.

At the end:

Display total score.

Store answered questions in a dictionary {question: chosen_answer}.

Convert it into a set of correctly answered questions.'''


questions = [
    {
        "question": "What is the capital of India?",
        "options": ("A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
        "answer": "A"
    },
    {
        "question": "What is the national animal of India?",
        "options": ("A. Lion", "B. Elephant", "C. Tiger", "D. Peacock"),
        "answer": "C"
    },
    {
        "question": "What is 9 * 8?",
        "options": ("A. 64", "B. 72", "C. 81", "D. 98"),
        "answer": "B"
    }
]

score = 0
answered = {}

print("Welcome to the Quiz Game!\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    while True:
        try:
            choice = input("Enter your choice (A/B/C/D): ").strip().upper()

            if not choice.isalpha():
                raise TypeError("Input must be a letter (A-D).")

            if choice not in [opt[0] for opt in q["options"]]:
                raise ValueError("Choice must be one of A, B, C, or D.")

            answered[q["question"]] = choice

            if choice == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer was {q['answer']}.\n")
            break

        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception:
            print("Unexpected error occurred!")

correctly_answered = {
    q for q in answered
    if answered[q] == questions[[qq["question"] for qq in questions].index(q)]["answer"]
}

print("--- Quiz Summary ---")
print(f"Total Score: {score}/{len(questions)}")
print("Answered Questions:", answered)
print("Correctly Answered Questions (set):", correctly_answered)
