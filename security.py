from tkinter import *
import os 
from tkinter import messagebox

#creating a window
root = Tk()
root.title("TERMINATOR USER LOGIN")
mas = messagebox

#define a function
def login():
    if enter1.get() == "admin" and enter2.get() == "passwd":
        os.system(code())
        root.destroy()
        
    else:
        mas.showinfo("warning","NO ENTRY TO THE TERMINATOR")
        exit(root)
    quit()
def cancel():
    exit(root)


lab1 = Label(root, text='USERNAME ')
lab1.grid(row=0, column=0)

lab2 = Label(root, text='PASSWORD')
lab2.grid(row=2, column=0)

#entry window
enter1 = Entry(root)
enter1.grid(row=0, column=2)

enter2 = Entry(root, show="*")
enter2.grid(row=2, column=2)

#buttons
but1 = Button(root, text="Cancel", command=cancel)
but1.grid(row=5, column=0, pady=10)

but2 = Button(root, text="Login", command=login)
but2.grid(row=5, column=1, columnspan=5)


def code():
    import time
    import webbrowser

    while 1:
        x = input("terminator@kali# ")
        if x == 'exit':
            break

        else:
            if x == 'ls':
                print(os.listdir("/home/kali/"))
            elif x == 'cd desktop':
                path = "/home/kali/Desktop/"
                os.chdir(path)
                print("Access Granted")
            elif x == 'ls desktop':
                print(os.listdir("/home/kali/Desktop"))
            elif x == 'cd':
                path1 = "/home/kali"
                print(os.chdir(path1))
                print(os.getcwd())
            elif x == 'hello':
                print("hello sir")
            elif x == 'how are you jarvis':
                print('i am fine sir')
            elif x == 'what is going on ':
                print('nothing too good sir')
            elif x == 'todays news':
                webbrowser.open("https://www.polimernews.com/dlive-tv")
            elif x == 'what is my name':
                print("sir your name is rakesh")
            elif x == 'what is the time':
                print("the current time is:", time.asctime())
            elif x == 'open youtube':
                url = 'www.youtube.com'
                webbrowser.open(url)
            elif x == 'open firefox':
                url1 = 'www.google.com'
                webbrowser.open(url1)
            elif x == 'open gmail':
                url2 = 'www.gmail.com'
                webbrowser.open(url2)
            elif x == 'open twitter':
                webbrowser.open('www.twitter.com')
            elif x == 'open telegram':
                webbrowser.open('www.telegram.com')
            elif x == 'open instagram':
                webbrowser.open('www.instagram.com')
            elif x == 'good job':
                print('thank you sir')
            else:
                print("sorry try again")


root.mainloop()





