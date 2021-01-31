#this is for a test commit

import random
from tkinter import *
score = 0

root = Tk()
root.title("Spanish Revision Resource")


el1 = Label(text = "English 1.", font = "Serif 11 bold")
el1.place(x=50,y=30)
ee1 = Entry(bd = 5)
ee1.place(x=50,y=50)
ee1.focus()

sl1 = Label(text = "Spanish 1.", font = "Serif 11 bold")
sl1.place(x=315,y=30)
se1 = Entry(bd = 5)
se1.place(x=315,y=50)


el2 = Label(text = "English 2.", font = "Serif 11 bold")
el2.place(x=50,y=80)
ee2 = Entry(bd = 5)
ee2.place(x=50,y=100)

sl2 = Label(text = "Spanish 2.", font = "Serif 11 bold")
sl2.place(x=315,y=80)
se2 = Entry(bd = 5)
se2.place(x=315,y=100)


el3 = Label(text = "English 3.", font = "Serif 11 bold")
el3.place(x=50,y=130)
ee3 = Entry(bd = 5)
ee3.place(x=50,y=150)

sl3 = Label(text = "Spanish 3.", font = "Serif 11 bold")
sl3.place(x=315,y=130)
se3 = Entry(bd = 5)
se3.place(x=315,y=150)


el4 = Label(text = "English 4.", font = "Serif 11 bold")
el4.place(x=50,y=180)
ee4 = Entry(bd = 5)
ee4.place(x=50,y=200)

sl4 = Label(text = "Spanish 4.", font = "Serif 11 bold")
sl4.place(x=315,y=180)
se4 = Entry(bd = 5)
se4.place(x=315,y=200)


el5 = Label(text = "English 5.", font = "Serif 11 bold")
el5.place(x=50,y=230)
ee5 = Entry(bd = 5)
ee5.place(x=50,y=250)

sl5 = Label(text = "Spanish 5.", font = "Serif 11 bold")
sl5.place(x=315,y=230)
se5 = Entry(bd = 5)
se5.place(x=315,y=250)


el6 = Label(text = "English 6.", font = "Serif 11 bold")
el6.place(x=50,y=280)
ee6 = Entry(bd = 5)
ee6.place(x=50,y=300)

sl6 = Label(text = "Spanish 6.", font = "Serif 11 bold")
sl6.place(x=315,y=280)
se6 = Entry(bd = 5)
se6.place(x=315,y=300)


el7 = Label(text = "English 7.", font = "Serif 11 bold")
el7.place(x=50,y=330)
ee7 = Entry(bd = 5)
ee7.place(x=50,y=350)

sl7 = Label(text = "Spanish 7.", font = "Serif 11 bold")
sl7.place(x=315,y=330)
se7 = Entry(bd = 5)
se7.place(x=315,y=350)


el8 = Label(text = "English 8.", font = "Serif 11 bold")
el8.place(x=50,y=380)
ee8 = Entry(bd = 5)
ee8.place(x=50,y=400)

sl8 = Label(text = "Spanish 8.", font = "Serif 11 bold")
sl8.place(x=315,y=380)
se8 = Entry(bd = 5)
se8.place(x=315,y=400)


el9 = Label(text = "English 9.", font = "Serif 11 bold")
el9.place(x=50,y=430)
ee9 = Entry(bd = 5)
ee9.place(x=50,y=450)

sl9 = Label(text = "Spanish 9.", font = "Serif 11 bold")
sl9.place(x=315,y=430)
se9 = Entry(bd = 5)
se9.place(x=315,y=450)


el10 = Label(text = "English 10.", font = "Serif 11 bold")
el10.place(x=50,y=480)
ee10 = Entry(bd = 5)
ee10.place(x=50,y=500)

sl10 = Label(text = "Spanish 10.", font = "Serif 11 bold")
sl10.place(x=315,y=480)
se10 = Entry(bd = 5)
se10.place(x=315,y=500)

def execute():
    window = Tk()
    window.title("Spanish Revision Resource")
    
    entryinputs = [ee1.get(), ee2.get(), ee3.get(), ee4.get(), ee5.get(), ee6.get(), ee7.get(), ee8.get(), ee9.get(), ee10.get()]
    choose = random.choice(entryinputs)
    context = f'What is "{choose}" in Spanish?'
    labelquestion = Label(window, text = context, font = "Serif 10 bold")
    labelquestion.place(x=175,y=100)
    
    guess_one = Entry(window, bd = 5)
    guess_one.place(x=185,y=135)
    guess_one.focus()
    submit_button = Button(window, text = "           Enter           ", font = "Helvetica 10 bold", bd = 2.5, command = guessing1)
    submit_button.place(x=182.8,y=180)

    window.geometry("600x600")
    window.mainloop()
    end()
        
btn = Button(root, text = "                    Submit                    ", font = "Helvetica 10 bold", bd = 5, command = execute)
btn.place(x=143,y=550)

def guessing1():     
     if choose == guess_one.get():
        score = score+10
        context_other = f'Correct!\nYour score is {score}!'
        correct = Label(window, text = context_other, font = "Helvetica 10 bold", bg = "green")
        correct.place(x=175,y=500)
        window.destroy()
        window2 = Tk()

root.geometry("600x600")
root.mainloop()
