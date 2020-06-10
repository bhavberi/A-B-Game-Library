import os
import sqlite3
from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.title("B&B Game Library")
root.geometry("1920x1080")
t = StringVar()
global t1, t2, t3, t4, t5, t6, t7, t8, t9
global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, s

t1, t2, t3, t4, t5, t6, t7, t8, t9 = "", "", "", "", '', '', '', '', ''
player_a_turn = True
player_b_won = False
player_a_won = False
draw = False
play_again = False
won = ""
firstTurn = 0
s = ""

def Menu():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9
    global button1, button2, button3, button4, button5, button6, button6, button7, button8, button9, btn1, btn2

    button1 = Button(dFrame, text=t1, font=('arial', 10, 'bold'), cursor="heart", command=button1ActionPerformed)
    button2 = Button(dFrame, text=t2, font=('arial', 10, 'bold'), cursor="spider", command=button2ActionPerformed)
    button3 = Button(dFrame, text=t3, font=('arial', 10, 'bold'), cursor="heart", command=button3ActionPerformed)
    button4 = Button(dFrame, text=t4, font=('arial', 10, 'bold'), cursor="spider", command=button4ActionPerformed)
    button5 = Button(dFrame, text=t5, font=('arial', 10, 'bold'), cursor="heart", command=button5ActionPerformed)
    button6 = Button(dFrame, text=t6, font=('arial', 10, 'bold'), cursor="spider", command=button6ActionPerformed)
    button7 = Button(dFrame, text=t7, font=('arial', 10, 'bold'), cursor="heart", command=button7ActionPerformed)
    button8 = Button(dFrame, text=t8, font=('arial', 10, 'bold'), cursor="spider", command=button8ActionPerformed)
    button9 = Button(dFrame, text=t9, font=('arial', 10, 'bold'), cursor="heart", command=button9ActionPerformed)

    button1.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.3)
    button2.place(relx=0.25, rely=0.05, relwidth=0.2, relheight=0.3)
    button3.place(relx=0.45, rely=0.05, relwidth=0.2, relheight=0.3)
    button4.place(relx=0.05, rely=0.35, relwidth=0.2, relheight=0.3)
    button5.place(relx=0.25, rely=0.35, relwidth=0.2, relheight=0.3)
    button6.place(relx=0.45, rely=0.35, relwidth=0.2, relheight=0.3)
    button7.place(relx=0.05, rely=0.65, relwidth=0.2, relheight=0.3)
    button8.place(relx=0.25, rely=0.65, relwidth=0.2, relheight=0.3)
    button9.place(relx=0.45, rely=0.65, relwidth=0.2, relheight=0.3)

def button1ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t1
    if (button1['text'] == ("")):
        if (player_a_turn == True):
            t1 = "X"
            Menu()
            button1.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t1 = "O"
            Menu()
            button1.configure(state='disabled')
            check()
            player_a_turn = True

def button2ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t2
    if (button2['text'] == ("")):
        if (player_a_turn == True):
            t2 = "X"
            Menu()
            button2.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t2 = "O"
            Menu()
            button2.configure(state='disabled')
            check()
            player_a_turn = True


def button3ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t3
    if (button3['text'] == ("")):
        if (player_a_turn == True):
            t3 = "X"
            Menu()
            button3.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t3 = "O"
            Menu()
            button3.configure(state='disabled')
            check()
            player_a_turn = True


def button4ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t4
    if (button4['text'] == ("")):
        if (player_a_turn == True):
            t4 = "X"
            Menu()
            button4.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t4 = "O"
            Menu()
            button4.configure(state='disabled')
            check()
            player_a_turn = True


def button5ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t5
    if (button5['text'] == ("")):
        if (player_a_turn == True):
            t5 = "X"
            Menu()
            button5.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t5 = "O"
            Menu()
            button5.configure(state='disabled')
            check()
            player_a_turn = True


def button6ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t6
    if (button6['text'] == ("")):
        if (player_a_turn == True):
            t6 = "X"
            Menu()
            button6.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t6 = "O"
            Menu()
            button6.configure(state='disabled')
            check()
            player_a_turn = True

def button7ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t7
    if (button7['text'] == ("")):
        if (player_a_turn == True):
            t7 = "X"
            Menu()
            button7.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t7 = "O"
            Menu()
            button7.configure(state='disabled')
            check()
            player_a_turn = True

def button8ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t8
    if (button8['text'] == ("")):
        if (player_a_turn == True):
            t8 = "X"
            Menu()
            button8.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t8 = "O"
            Menu()
            button8.configure(state='disabled')
            check()
            player_a_turn = True

def button9ActionPerformed():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, t9
    if (button9['text'] == ("")):
        if (player_a_turn == True):
            t9 = "X"
            Menu()
            button9.configure(state='disabled')
            check()
            player_a_turn = False
        else:
            t9 = "O"
            Menu()
            button9.configure(state='disabled')
            check()
            player_a_turn = True

def quit_fn():
    root.destroy()
    root.quit()
def scoreSet():
    global s
    scoreFrame = Entry(dFrame, state="normal", bd=10, relief=GROOVE, cursor="star")
    scoreFrame.place(relx=0.68, rely=0.1, relwidth=0.3, relheight=0.4)
    scoreFrame.delete(0, END)
    scoreFrame.insert(0, s)
    scoreFrame.configure(state='disabled')

def check():
    global player_a_turn, player_b_won, player_a_won, draw, play_again, won, firstTurn, s
    global t1, t2, t3, t4, t5, t6, t7, t8, t9
    t1 = button1['text']
    t2 = button2['text']
    t3 = button3['text']
    t4 = button4['text']
    t5 = button5['text']
    t6 = button6['text']
    t7 = button7['text']
    t8 = button8['text']
    t9 = button9['text']

    s1 = button1['state']
    s2 = button2['state']
    s3 = button3['state']
    s4 = button4['state']
    s5 = button5['state']
    s6 = button6['state']
    s7 = button7['state']
    s8 = button8['state']
    s9 = button9['state']

    if ((button1['text'] == ("X")) or (button1['text'] == ("O"))):
        if ((button2['text'] == ("X")) or (button2['text'] == ("O"))):
            if ((button3['text'] == ("X")) or (button3['text'] == ("O"))):
                if ((button4['text'] == ("X")) or (button4['text'] == ("O"))):
                    if ((button5['text'] == ("X")) or (button5['text'] == ("O"))):
                        if ((button6['text'] == ("X")) or (button6['text'] == ("O"))):
                            if ((button7['text'] == ("X")) or (button7['text'] == ("O"))):
                                if ((button8['text'] == ("X")) or (button8['text'] == ("O"))):
                                    if ((button9['text'] == ("X")) or (button9['text'] == ("O"))):
                                        draw = True
                                        won = "The Match has drawn"

    if (button1['text'] == ("X")):
        if (button4['text'] == ("X")):
            if (button7['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button1['text'] == ("X")):
        if (button5['text'] == ("X")):
            if (button9['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button1['text'] == ("X")):
        if (button2['text'] == ("X")):
            if (button3['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button3['text'] == ("X")):
        if (button5['text'] == ("X")):
            if (button7['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button3['text'] == ("X")):
        if (button6['text'] == ("X")):
            if (button9['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button7['text'] == ("X")):
        if (button8['text'] == ("X")):
            if (button9['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button4['text'] == ("X")):
        if (button5['text'] == ("X")):
            if (button6['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button2['text'] == ("X")):
        if (button5['text'] == ("X")):
            if (button8['text'] == ("X")):
                player_a_won = True
                player_b_won = False
                won = "Player X has won"

    if (button1['text'] == ("O")):
        if (button4['text'] == ("O")):
            if (button7['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button1['text'] == ("O")):
        if (button5['text'] == ("O")):
            if (button9['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button1['text'] == ("O")):
        if (button2['text'] == ("O")):
            if (button3['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button3['text'] == ("O")):
        if (button5['text'] == ("O")):
            if (button7['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button3['text'] == ("O")):
        if (button6['text'] == ("O")):
            if (button9['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button7['text'] == ("O")):
        if (button8['text'] == ("O")):
            if (button9['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button4['text'] == ("O")):
        if (button5['text'] == ("O")):
            if (button6['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    if (button2['text'] == ("O")):
        if (button5['text'] == ("O")):
            if (button8['text'] == ("O")):
                player_a_won = False
                player_b_won = True
                won = "Player O has won"

    """if ((button1['text'] == ("X")) or (button1['text'] == ("O"))):
        if ((button2['text'] == ("X")) or (button2['text'] == ("O"))):
            if ((button3['text'] == ("X")) or (button3['text'] == ("O"))):
                if ((button4['text'] == ("X")) or (button4['text'] == ("O"))):
                    if ((button5['text'] == ("X")) or (button5['text'] == ("O"))):
                        if ((button6['text'] == ("X")) or (button6['text'] == ("O"))):
                            if ((button7['text'] == ("X")) or (button7['text'] == ("O"))):
                                if ((button8['text'] == ("X")) or (button8['text'] == ("O"))):
                                    if ((button9['text'] == ("X")) or (button9['text'] == ("O"))):
                                        draw = True
                                        won = "The Match has drawn"
    """                                    
    if (player_b_won == True or player_a_won == True or draw == True):
        if player_b_won == True:
            s = "Player B has won  \t\n" + won
        elif player_a_won == True:
            s = "Player A has won  \t\n" + won
        elif draw == True:
            s = won
        scoreSet()
        Menu()
        button9.configure(state='disabled')
        button8.configure(state='disabled')
        button7.configure(state='disabled')
        button6.configure(state='disabled')
        button5.configure(state='disabled')
        button4.configure(state='disabled')
        button3.configure(state='disabled')
        button2.configure(state='disabled')
        button1.configure(state='disabled')
        #sleep(10)
        #quit_fn()



################################## Frames #########################################################################

dFrame = Frame(root, bd=20, relief=RIDGE)
dFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

d = Label(dFrame, font=('Times New ROman', 40, 'bold'), text="B&B Game Library")
d.place(relx=0.3, rely=0.2)

quitBtn = Button(dFrame, text="QUIT", font=("arial", 10, 'bold'), command=quit_fn)
quitBtn.place(relx=0.87, rely=0.4, relwidth=0.1)

dFrame = Frame(root, bd=20, relief=RIDGE)
dFrame.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)

displayFrame = Frame(dFrame, bd=10, relief=SOLID, bg='white')
displayFrame.place(relx=0.038, rely=0.03, relwidth=0.63, relheight=0.95)

scoreFrame = Entry(dFrame, state="disabled", bd=10, relief=GROOVE, textvariable=t, cursor="star")
scoreFrame.place(relx=0.68, rely=0.1, relwidth=0.3, relheight=0.4)

################################################################################

Menu()
root.title("B&B Game Library - TicTacToe")
t.set("Hello\tPlayer A - X\tPlayer B - O")
root.mainloop()
