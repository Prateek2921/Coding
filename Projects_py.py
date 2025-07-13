import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.set(result)
        except:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
entry = tk.StringVar()
entry.set("")

entry_field = tk.Entry(root, textvar=entry, font="Arial 20")
entry_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", padx=20, pady=10)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
