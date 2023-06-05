import tkinter as tk
from packages.utils import change_in_json

def onKeyPress(event):
    text.insert('end', f'You pressed {event.char}\n')
    print(dir(event))
    print(event.keycode)
    save_binding(2)

def save_binding(keybind):
    key = ["APP"]["binds"]["start"]
    print(key)
    change_in_json(file="config.json", key=key, new_value="xaxa")

root = tk.Tk()
root.geometry('800x600')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()