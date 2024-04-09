import tkinter as tk
from tkinter import ttk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
        entry.icursor(tk.END)  # Set cursor position to the end

def key_press(event):
    entry.insert(tk.END, event.char)
    entry.icursor(tk.END)  # Set cursor position to the end

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("Calculator")
    guiWindow.geometry("300x400+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#5F374B")

    calculator_frame = tk.Frame(guiWindow, bg="#5F374B")
    calculator_frame.pack(expand=True, fill="both")

    entry = tk.Entry(
        calculator_frame,
        font=("Consolas", 20),
        background="#FFFFFF",
        foreground="#000000",
        justify="right"
    )
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
    entry.bind("<Key>", key_press)

    button_list = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
    ]

    for (text, row, col) in button_list:
        button = ttk.Button(
            calculator_frame,
            text=text,
            width=5,
            command=lambda t=text: entry.insert(tk.END, t)
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        if text in {"C", "="}:
            button.bind("<Button-1>", button_click)

    guiWindow.mainloop()