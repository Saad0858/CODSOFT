import tkinter as tk
from tkinter import messagebox
import random
import tkinter.font as font

# Sample quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Venus", "Jupiter", "Mars", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "iphone was created by which company?",
        "choices": ["Samsung", "Apple", "Oppo", "OnePlus"],
        "answer": "Apple"
    },
    {
        "question": "Who is CEO of Tesla",
        "choices": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "answer": "Elon Musk"
    }
]

# Global variables
current_question_index = 0
score = 0

def check_answer():
    global score
    selected_index = answer_var.get()
    selected_answer = quiz_questions[current_question_index]["choices"][selected_index]
    correct_answer = quiz_questions[current_question_index]["answer"]

    if selected_answer == correct_answer:
        score += 1

    # Display feedback
    feedback_label.config(text=f"Your answer is {'correct' if selected_answer == correct_answer else 'incorrect'}.")
    show_correct_answer()
    submit_button.config(state=tk.DISABLED)
    next_button.config(state=tk.NORMAL)

def show_correct_answer():
    correct_answer = quiz_questions[current_question_index]["answer"]
    correct_label.config(text=f"The correct answer is: {correct_answer}")


def next_question():
    global current_question_index
    submit_button.config(state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)
    feedback_label.config(text="")
    correct_label.config(text="")

    if current_question_index < len(quiz_questions) - 1:
        current_question_index += 1
        question_label.config(text=quiz_questions[current_question_index]["question"])

        # Clear the selection
        answer_var.set(None)

        # Display the choices (if any)
        choices = quiz_questions[current_question_index].get("choices", [])
        for i, choice in enumerate(choices):
            answer_buttons[i].config(text=choice)

    else:
        display_final_results()

def display_final_results():
    result = f"You scored {score} out of {len(quiz_questions)}."
    user_choice = messagebox.askyesno("Quiz Complete", result + "\n\nDo you want to play again?")

    if user_choice:
        play_again()
    else:
        quit_game()

def play_again():
    global current_question_index, score
    current_question_index = 0
    score = 0

    # Shuffle the quiz questions before starting again
    random.shuffle(quiz_questions)

    # Start the quiz with the first question
    question_label.config(text=quiz_questions[current_question_index]["question"])
    choices = quiz_questions[current_question_index].get("choices", [])
    for i, choice in enumerate(choices):
        answer_buttons[i].config(text=choice)

    submit_button.config(state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)

def quit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x500+500+150")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Create widgets

label = tk.Label(frame1, text="Quiz Game", fg='blue')
label_font = font.Font(size=30, family='comic sans ms')
label['font'] = label_font
label.grid(pady=(10,10), row=1, column=1, columnspan=2)

question_label = tk.Label(frame1, text=quiz_questions[current_question_index]["question"],fg='red')
label_font = font.Font(size=14, family='comic sans ms')
question_label['font'] = label_font
question_label.grid(row=2, pady=(20, 10), column=2, padx=(20, 5))

answer_var = tk.IntVar()  # Use IntVar to store the index of the selected choice
answer_buttons = []
choices = quiz_questions[current_question_index].get("choices", [])
for i, choice in enumerate(choices):
    answer_buttons.append(tk.Radiobutton(frame1, text=choice, variable=answer_var, value=i))
    answer_font = font.Font(size=14, family='comic sans ms')
    answer_buttons[i]['font'] = answer_font
    answer_buttons[i].grid(row=i+3, pady=(1,1), column=2, padx=(5,5))
frame1.pack()

btn_font = font.Font(size=14)
submit_button = tk.Button(frame2, text="Submit", command=check_answer)
submit_button['font'] = btn_font
submit_button.grid(row=1, pady=(20, 10), column=1, padx=(20, 5))

next_button = tk.Button(frame2, text="Next", command=next_question, state=tk.DISABLED)
next_button['font'] = btn_font
next_button.grid(row=1, pady=(20, 10), column=2, padx=(20, 5))

feedback_label = tk.Label(frame2, text="", fg='red')
feedback_font = font.Font(size=14, family='comic sans ms')
feedback_label['font'] = feedback_font
feedback_label.grid(row=2, pady=(5,5), column=1, padx=(20, 5), columnspan=2)

correct_label = tk.Label(frame2, text="",fg='red')
correct_label_font = font.Font(size=14, family='comic sans ms')
correct_label['font'] = correct_label_font
correct_label.grid(row=3, pady=(5,5), column=1, padx=(20, 5), columnspan=2)

frame2.pack()

# Start the quiz with the first question
question_label.config(text=quiz_questions[current_question_index]["question"])
choices = quiz_questions[current_question_index].get("choices", [])
for i, choice in enumerate(choices):
    answer_buttons[i].config(text=choice)

# Run the application
root.mainloop()

