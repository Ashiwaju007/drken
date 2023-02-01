from tkinter import *
root = Tk()
root.title("Dr Ken")
def send():
    send = "You -> "+e.get()
    txt.insert(END, ""+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "" + "Bot -> Great! how can I help you.")
    else:
        txt.insert(END, "" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()