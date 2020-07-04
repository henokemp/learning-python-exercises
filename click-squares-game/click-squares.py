import tkinter
import random
import time

s = 0
time = random.choice(1,5)

window = tkinter.Tk()
window.configure(bg = "white")
window.title("Click Squares Game")

location1 =

btn1 = tkinter.Button(window, bg = "red", command = s_change)
btn1.place(height = 50, width = 50, relx = 1.0, rely = 0, anchor="ne")

btn2 = tkinter.Button(window, bg = "black")
btn2.place(height = 50, width = 50, relx = 0, rely = 1.0, anchor="sw")

btn3 = tkinter.Button(window, bg = "black")
btn3.place(height = 50, width = 50, relx = 0, rely = 0, anchor="nw")

btn4 = tkinter.Button(window, bg = "black")
btn4.place(height = 50, width = 50, rely= 1.0, relx = 1.0, anchor="se")

score = tkinter.Label(window, text = s, font=("Helvetica", 40), bg = "white").place(rely= 0.5, relx = 0.5, anchor = "center")

def s_change():
	global s
	s = s + 1
	score = tkinter.Label(window, text = s, font=("Helvetica", 40), bg = "white").place(rely= 0.5, relx = 0.5, anchor = "center")
	# c_change()
	return

def c_change():
	time.sleep(time)

	if bg == "red":
		bg = "black"
	else:
		bg = "red"

window.mainloop()
