#!/usr/bin/env python3

from tkinter import *
from class_objects import *

master = Tk()


for c in range(40):
	for r in range(30):
		Label(bg='green', text='', relief=RIDGE,width=3, height=2).grid(row=r,column=c)
		master.columnconfigure(c, weight=1)
		master.rowconfigure(r, weight=1)

x = 10
y = 5
v = 2

for c in range(x+2*v):
	for r in range(y+2*v):
		Label(bg='yellow', text='V', relief=RIDGE,width=3, height=2).grid(row=y+r-v,column=x+c-v)
		#master.columnconfigure(c, weight=1)
		#master.rowconfigure(r, weight=1)

for c in range(x):
	for r in range(y):
		Label(bg='purple', text='E', relief=RIDGE,width=3, height=2).grid(row=y+r,column=x+c)
		#master.columnconfigure(c, weight=1)
		#master.rowconfigure(r, weight=1)

mainloop()
