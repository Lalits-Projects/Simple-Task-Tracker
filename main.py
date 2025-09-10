import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk
from tkinter import font

dict = {}
window = tk.Tk()
window.title("To-Do List Creator")
window.resizable(width=False, height=False)

strikethrough_font = font.Font(family="Arial", size=10, overstrike=1)
regular_font = font.Font(family="Arial", size=10)




def storeDict():
    task_val = task_entry.get()
    time_val = time_entry.get()
    dict[time_val] = task_val
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def killWindow():
    window.destroy()



task_frame = tk.Frame(master=window)
task_entry = tk.Entry(master=task_frame, width=50)
task_lable = tk.Label(master=task_frame, text="Task")

time_frame = tk.Frame(master=window)
time_entry = tk.Entry(master=time_frame, width=50)
time_lable = tk.Label(master=time_frame, text="Time")

task_entry.grid(row=0, column=1)
task_lable.grid(row=0, column=0)

time_entry.grid(row=1, column=1)
time_lable.grid(row=1, column=0)

btn_addTask = tk.Button(
    master=window,
    text="Add Task",
    command = storeDict
)

btn_createTable = tk.Button(
    master=window,
    text="Finish Task",
    command = killWindow
)

task_frame.grid(row=0, column=0, pady=5)
time_frame.grid(row=1, column=0, pady=5)
btn_addTask.grid(row=2, column=0, pady=2)
btn_createTable.grid(row=3, column=0, pady=2)

window.mainloop()

# Start The New Window

root = tk.Tk()
root.title("Things To Do:")
treeview = ttk.Treeview(columns= ("time"))
treeview.heading("#0", text="Tasks")
treeview.heading("time", text="Times")

for keys in dict:
    time_key = keys
    task_val = dict[keys]
    treeview.insert(
        "",
        tk.END,
        text = task_val,
        values = (time_key)
    )

treeview.pack()
root.mainloop()



