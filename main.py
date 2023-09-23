# -*- coding: utf-8 -*-
#%% Import modules
from tkinter import Tk, Label
from time import strftime


#%% Function
def Time():
    clock = strftime('%H:%M:%S')
    sub_msg = strftime("%a | %d %b %Y")
    clock_label.config(text=clock)
    date_label.config(text=sub_msg)
    app.after(1000, Time)


#%% App
app = Tk()
app.geometry("275x110")
app.configure(bg="black")

clock_label = Label(app, font=("DS-Digital", 50, "bold"), background="black", foreground="white")
clock_label.place(x=0, y=0)

date_label = Label(app, font=("DS-Digital", 20, "bold"), background="black", foreground="white")
date_label.place(x=0, y=67)

Time()

app.overrideredirect(True)
app.wm_attributes("-transparentcolor", "black")
app.mainloop()
