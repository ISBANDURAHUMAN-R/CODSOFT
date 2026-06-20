from tkinter import *
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Score  You: {user_score}  Computer: {computer_score}"
    )

def reset_score():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    score_label.config(
        text="Score  You: 0  Computer: 0"
    )

    result_label.config(text="")
    user_label.config(text="You:")
    computer_label.config(text="Computer:")

root = Tk()
root.title("Rock Paper Scissors - CODSOFT")
root.geometry("500x450")
root.resizable(False, False)

Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 18, "bold")
).pack(pady=15)

user_label = Label(root, text="You:", font=("Arial", 12))
user_label.pack()

computer_label = Label(root, text="Computer:", font=("Arial", 12))
computer_label.pack()

result_label = Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=15)

Button(
    root,
    text="Rock",
    width=15,
    command=lambda: play("Rock")
).pack(pady=5)

Button(
    root,
    text="Paper",
    width=15,
    command=lambda: play("Paper")
).pack(pady=5)

Button(
    root,
    text="Scissors",
    width=15,
    command=lambda: play("Scissors")
).pack(pady=5)

score_label = Label(
    root,
    text="Score  You: 0  Computer: 0",
    font=("Arial", 12)
)
score_label.pack(pady=20)

Button(
    root,
    text="Reset Score",
    command=reset_score
).pack()

Label(
    root,
    text="Created by RAHUMAN",
    font=("Arial", 10)
).pack(side=BOTTOM, pady=10)

root.mainloop()
