""" Comptage Application (simulation of MV2) """
from tkinter import *

window = Tk()
canvas = Canvas(window,  width=500, height=100, bg='ivory')
canvas.pack()

current_result = 0
def count(button):
    global current_result
    if button == "+1":
        result = current_result + 1
        current_result = result
    elif button == "+10":
        result = current_result + 10
        current_result = result
    elif button == "+5":
        result = current_result + 5
        current_result = result
        
    canvas.delete("all")
    canvas_zone = canvas.create_text(250, 40 ,text= result, font='Arial 13 italic', fill = 'blue', width=300)
    
    print(result)
    return result

button_1 = Button(window, text ='+1', command = lambda: count("+1")).pack(side=LEFT, padx=5, pady=5)
button_10 = Button(window, text ='+10', command= lambda: count("+10")).pack(side=RIGHT, padx=5, pady=5)
button_5 = Button(window, text ='+5', command= lambda: count("+5")).pack(side=BOTTOM, padx=5, pady=5)

window.mainloop()
