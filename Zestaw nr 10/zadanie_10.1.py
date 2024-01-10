from tkinter import *
import random 
  
window = Tk() 
window.configure(bg="darkgrey") 
window.geometry("300x200") 
window.title("Rzut Kostką") 
window.resizable(0, 0) 
  
def roll(): 
    dice = ['1', '2', '3', '4', '5', '6'] 
    label.configure(text=f'{random.choice(dice)}') 
    label.pack() 
   
roll_button = Button(window, text="Rzuć kostką", width=8, height=2, font=10, bg="paleturquoise", bd=2, command=roll) 
roll_button.pack(padx=10, pady=15)   

label = Label(window, font=("times", 40), bg="darkgrey", fg="black") 
  
window.mainloop() 