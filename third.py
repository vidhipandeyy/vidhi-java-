import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

entry = tk.Entry(root, font=("Arial",20))
entry.pack(pady=10)

buttons = [
["7","8","9","/"],
["4","5","6","*"],
["1","2","3","-"],
["0",".","=","+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    
    for btn in row:
        button = tk.Button(frame, text=btn, width=5, height=2)
        button.pack(side="left", padx=5, pady=5)

root.mainloop()
