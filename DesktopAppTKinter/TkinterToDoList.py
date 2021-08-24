from tkinter import *
from tkinter import scrolledtext
def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()

def render_create_view():
    clear_view()
    task_name = Entry(tk)
    task_name.grid(column=1, row=0, padx=20, pady=20)
    Label(tk,text="Enter description").grid(column=1,row=1,padx=20,pady=20)
    description = scrolledtext.ScrolledText(tk, width=20, height=10)
    description.grid(column=2,row=1,padx=20,pady=20)
    task_priority = IntVar
    Label(tk,text="What is the task priority?").grid(column=1,row=2,padx=20,pady=20)
    radio_button1 = Radiobutton(tk,text="Low",value=1, variable=task_priority)
    radio_button1.grid(column=2,row=2,padx=20,pady=20)
    radio_button2 = Radiobutton(tk, text="Medium",value=2, variable=task_priority)
    radio_button2.grid(column=3, row=2, padx=20, pady=20)
    radio_button3 = Radiobutton(tk, text="High", value=3, variable=task_priority)
    radio_button3.grid(column=4, row=2, padx=20, pady=20)
    task_completed = BooleanVar
    check_box = Checkbutton(tk,text="Is it completed?", variable=task_completed)
    check_box.grid(column=1, row=3, padx=20, pady=20)
tk = Tk()
tk.geometry("700x700")
button = Button(tk, text="List all tasks",bg="green")
button.grid(column=0,row=0,padx=20, pady=20)
Button(tk,text="Create task",bg = "blue",command=render_create_view).grid(column=1,row=0,padx=160,pady=20)
tk.mainloop()


