import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()  # define a string variable
l = tk.Label(window, bg='yellow', width=4, textvariable=var1) # display the selected content
l.pack()

def print_selection():
    value = lb.get(lb.curselection()) # get  content selected by your curse
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))

lb = tk.Listbox(window, listvariable=var2) # display the options
list_items = [1,2,3,4]
for item in list_items: # insert items into listbox at the end
    lb.insert('end', item)
lb.insert(1, 'first') # insert items according to the indexes
lb.insert(2, 'second')
lb.delete(2) #delete items according to the indexes
lb.pack() #show

window.mainloop()
