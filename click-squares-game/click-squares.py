import tkinter
import random
import root

window = tkinter.Tk()
window.configure(bg = "white")
window.minsize(500, 500)
window.title("Click Squares Game")

btn2 = tkinter.Button(window, bg = "black")
btn2.place(height = 50, width = 50, relx = 0, rely = 1.0, anchor = "sw")

btn3 = tkinter.Button(window, bg = "black")
btn3.place(height = 50, width = 50, relx = 0, rely = 0, anchor = "nw")

btn4 = tkinter.Button(window, bg = "black")
btn4.place(height = 50, width = 50, rely = 1.0, relx = 1.0, anchor = "se")

btn5 = tkinter.Button(window, bg = "black")
btn5.place(height = 50, width = 50, relx = 1.0, rely = 0, anchor = "ne")

btn1 = tkinter.Button(window, bg = "red", command = s_change)
btn1.place(height = 50, width = 50, relx = 1.0, rely = 0, anchor = "ne")

s = 0
score = tkinter.Label(window, text = s, font = ("Helvetica", 40), bg = "white").place(rely= 0.5, relx = 0.5, anchor = "center")

start = tkinter.Button(window, bg = "red", text = "START", font = ("Helvetica", 20), command = button_trigger).place(rely = 0.7, relx = 0.5, anchor = "center")

def s_change():
	global s
	s = s + 1
	score = tkinter.Label(window, text = s, font = ("Helvetica", 40), bg = "white").place(rely = 0.5, relx = 0.5, anchor = "center")
	click_change()
	return
	# This adds 1 to the scoreboard once the player successfully clicked on the red square

def c_change1():
	btn1.place(height = 50, width = 50, relx = 0, rely = 1.0, anchor = "sw")

def c_change2():
	btn1.place(height = 50, width = 50, relx = 0, rely = 0, anchor = "nw")

def c_change3():
	btn1.place(height = 50, width = 50, rely= 1.0, relx = 1.0, anchor = "se")

def c_change4():
	btn1.place(height = 50, width = 50, relx = 1.0, rely = 0, anchor = "ne")

	# These 4 functions place the red square in the 4 possible locations 

change_list = [c_change1, c_change2, c_change3, c_change4]

def button_trigger():
	time_change()
	start.destroy()

def click_change():
	random.choice(change_list)()
	return
	# This function triggers the position change of the red square to one of the four locations at random upon successful click by player

def time_change():
	btn1.after(random.randint(500, 2000), click_change)
	btn1.after(500, time_change)
	return
	# This changes the position of the red square after a random generated amount of time between 500 and 2000 ms and repeats the function

window.mainloop()
