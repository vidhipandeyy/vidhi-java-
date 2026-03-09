import tkinter as tk

quiz = [
    {
        "question": "What does LED stand for?",
        "options": ["Light Emitting Diode", "Low Energy Device", "Linear Electric Device", "Light Energy Diode"],
        "answer": 0
    },
    {
        "question": "Unit of resistance?",
        "options": ["Volt", "Ampere", "Ohm", "Watt"],
        "answer": 2
    },
    {
        "question": "Which device amplifies signals?",
        "options": ["Resistor", "Capacitor", "Diode", "Transistor"],
        "answer": 3
    },
    {
        "question": "Binary number system uses how many digits?",
        "options": ["2", "8", "10", "16"],
        "answer": 0
    },
    {
        "question": "SI unit of current?",
        "options": ["Volt", "Ampere", "Watt", "Ohm"],
        "answer": 1
    }
]

q_index = 0
score = 0
time_left = 10

def start_timer():
    global time_left
    timer_label.config(text="Time left: " + str(time_left))

    if time_left > 0:
        time_left -= 1
        root.after(1000, start_timer)
    else:
        feedback_label.config(text="Time's up!", fg="orange")
        next_question()

def check_answer(selected):
    global score, time_left

    for btn in option_buttons:
        btn.config(state="disabled")

    if selected == quiz[q_index]["answer"]:
        feedback_label.config(text="Correct!", fg="green")
        score += 1
    else:
        correct = quiz[q_index]["answer"]
        feedback_label.config(text="Wrong! Correct: " + quiz[q_index]["options"][correct], fg="red")

    root.after(1500, next_question)

def next_question():
    global q_index, time_left

    q_index += 1

    if q_index < len(quiz):
        show_question()
    else:
        question_label.config(text="Quiz Finished! Score: " + str(score) + "/" + str(len(quiz)))
        timer_label.config(text="")
        feedback_label.config(text="")
        for btn in option_buttons:
            btn.pack_forget()

def show_question():
    global time_left
    time_left = 10

    question_label.config(text=quiz[q_index]["question"])
    feedback_label.config(text="")

    options = quiz[q_index]["options"]

    for i in range(4):
        option_buttons[i].config(text=options[i], state="normal")

    start_timer()

root = tk.Tk()
root.title("Electronics Quiz App")
root.geometry("420x350")

question_label = tk.Label(root, font=("Arial",14), wraplength=350)
question_label.pack(pady=20)

timer_label = tk.Label(root, font=("Arial",12), fg="blue")
timer_label.pack()

feedback_label = tk.Label(root, font=("Arial",12))
feedback_label.pack(pady=5)

option_buttons = []

for i in range(4):
    btn = tk.Button(root, font=("Arial",12), width=30,
                    command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

show_question()

root.mainloop()

