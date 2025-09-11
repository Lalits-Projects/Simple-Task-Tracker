import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk
from tkinter import font



dict_val = {}
window = tk.Tk()
window.title("To-Do List Creator")
window.resizable(width=False, height=False)
window.configure(background="black")



def storeDict():
    task_val = task_entry.get()
    time_val = time_entry.get()
    dict_val[time_val] = task_val
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def killWindow():
    window.destroy()

def strikeOut(event):
    completed = treeview.selection()
    for vals in completed:
        current_tags = treeview.item(vals, "tags")
        if "completed" in current_tags:
            treeview.item(vals, tags="matrix")
        else:
            treeview.item(vals, tags="completed")
    treeview.selection_set(())
    

def unselect(event):
    region = treeview.identify_region(event.x, event.y)
    if(region == "separator"):
        return "break"
    treeview.selection_set(())
    

def stopColResize(event):
    region = treeview.identify_region(event.x, event.y)
    if(region == "separator"):
        return "break"


task_frame = tk.Frame(master=window)
task_entry = tk.Entry(master=task_frame, width=50, foreground="lime",  background="black")
task_lable = tk.Label(master=task_frame, text="Task", foreground="white",  background="black")

time_frame = tk.Frame(master=window)
time_entry = tk.Entry(master=time_frame, width=50, foreground="lime",  background="black")
time_lable = tk.Label(master=time_frame, text="Time", foreground="white",  background="black")

task_entry.grid(row=1, column=1)
task_lable.grid(row=1, column=0)

time_entry.grid(row=0, column=1)
time_lable.grid(row=0, column=0)

btn_addTask = tk.Button(
    master=window,
    text="Add Task",
    command = storeDict,
    bg="black",
    fg="white"
)

btn_createTable = tk.Button(
    master=window,
    text="Finish Task",
    command = killWindow,
    bg="black",
    fg="white"
)

task_frame.grid(row=1, column=0, pady=5)
time_frame.grid(row=0, column=0, pady=5)
btn_addTask.grid(row=2, column=0, pady=2)
btn_createTable.grid(row=3, column=0, pady=2)

window.mainloop()

# Start The New Window

root = tk.Tk()
root.title("Things To Do:")
root.resizable(width=False, height=False)
root.configure(background="black")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Custom.Treeview",foreground="lime", background="black",fieldbackground="black")
style.configure("Treeview.Heading", background="black", foreground="white")



# Adjust These Values To Adjust Created To-Do Lis
task_width = 400
time_width = 100

total_width = task_width + time_width
hieght_val = len(dict_val) * 20 + 30

root.geometry(str(total_width)+"x"+str(hieght_val))
treeview = ttk.Treeview(columns=("time"), style="Custom.Treeview")



# Configure the style for Treeview headings


treeview.heading("#0", text="Tasks")
treeview.heading("time", text="Times" )
treeview.column("#0", width=task_width, minwidth=task_width, stretch=False)
treeview.column("time", width=time_width, minwidth=time_width, stretch=False)

strikethrough_font = font.Font(size=9, overstrike=1)



for keys in dict_val:
    time_key = keys
    task_val = dict_val[keys]
    treeview.insert(
        "",
        tk.END,
        text = task_val,
        values = (time_key),
        tags = "matrix"
    )

treeview.bind("<Double-1>", strikeOut)
treeview.bind("<Button-1>", unselect)
treeview.bind("<B1-Motion>", stopColResize) 
treeview.tag_configure("completed", font=strikethrough_font)
treeview.pack()
root.mainloop()





