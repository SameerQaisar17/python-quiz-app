print("===== PYTHON QUIZ =====")
print("Answer the following questions!\n")

questions = [
    {
        "question": "Which language are we using?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for multiplication in Python?",
        "options": ["A. *", "B. x", "C. /", "D. +"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": ["A. loop", "B. function", "C. define", "D. def"],
        "answer": "D"
    },
    {
        "question": "Which function displays text on the screen?",
        "options": ["A. input()", "B. print()", "C. type()", "D. int()"],
        "answer": "B"
    }
]

score = 0

for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            break

        print("Invalid option! Please enter A, B, C, or D.")

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_letter = question["answer"]

        for option in question["options"]:
            if option.startswith(correct_letter + "."):
                correct_text = option[3:].strip()
                break

        print(
            f"Wrong! The correct answer is "
            f"{correct_letter}. {correct_text}"
        )

total = len(questions)
percentage = score / total * 100

print("\n===== QUIZ RESULTS =====")
print(f"Your score: {score}/{total}")
print(f"Percentage: {percentage:.0f}%")

if score == total:
    print("Perfect score! Amazing work!")
elif score >= total * 0.6:
    print("Good job! Keep practising!")
else:
    print("Keep learning! You will improve!")