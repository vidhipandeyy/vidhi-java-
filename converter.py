import tkinter as tk

def convert():
    value = float(entry.get())
    option = var.get()

    if option == "KM to M":
        result = value * 1000
        result_label.config(text=str(result) + " meters")

    elif option == "KG to G":
        result = value * 1000
        result_label.config(text=str(result) + " grams")

    elif option == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        result_label.config(text=str(result) + " °F")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x250")

entry = tk.Entry(root)
entry.pack(pady=10)

var = tk.StringVar()
var.set("KM to M")

menu = tk.OptionMenu(root, var, "KM to M", "KG to G", "Celsius to Fahrenheit")
menu.pack(pady=10)

convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()