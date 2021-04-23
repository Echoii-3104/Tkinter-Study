import tkinter as tk

window = tk.Tk()
window.title('input-text window')
window.geometry('200x200')

e = tk.Entry(window, show="*")  # define an input box
e.pack() #show on the window

def insert_point():
    var = e.get() # get the context from the input box
    t.insert('insert', var)
    
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()

window.mainloop()
