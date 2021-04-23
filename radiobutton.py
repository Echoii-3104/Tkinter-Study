import tkinter as tk

window = tk.Tk()
window.title('radiobutton window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, text='empty', bg='yellow', width=20)
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get()) # get the content of 'var' and modify the configs of the label

r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A', # change the content of 'var'
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()


window.mainloop()
