import tkinter as tk

window = tk.Tk()
window.title('my first try')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='blue', font=('Arial', 12), width=15,
             height=2)
l.pack() # place on an area(up,down,left,right)
#l.place() # place at one definite location

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,  height=2, command=hit_me)
b.pack()

window.mainloop() # window refresh loop -- required for all windows
