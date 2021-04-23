import tkinter as tk

window = tk.Tk()
window.title('scale window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty') # width-Character width
l.pack()

def print_selection(v): # v- the default variable
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, # lable-name; from&to-range ; orient-orientation;
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection) # length-px; showvalue-if or not show content on the buoy)
# tickinterval-the interval width of 'label'; resolution-decimal places;
s.pack()

window.mainloop()
