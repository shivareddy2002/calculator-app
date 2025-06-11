import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
expression = ""
screen_var = tk.StringVar()

entry = tk.Entry(root, textvar=screen_var, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

btn_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in btn_texts:
    f = tk.Frame(root)
    f.pack()
    for txt in row:
        b = tk.Button(f, text=txt, font="Arial 18", padx=20, pady=10)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
