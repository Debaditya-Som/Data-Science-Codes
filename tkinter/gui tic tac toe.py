from tkinter import *
def newgame():
    global move,turn

    r1=['','','']
    r2=['','','']
    r3=['','','']

    def empty():
        screen.destroy()
        newgame()

    def gameover():
        btn1.config(command=empty)
        btn2.config(command=empty)
        btn3.config(command=empty)
        btn4.config(command=empty)
        btn5.config(command=empty)
        btn6.config(command=empty)
        btn7.config(command=empty)
        btn8.config(command=empty)
        btn9.config(command=empty)
        screen.geometry('400x450+400+200')
        if r1[0] != '' and r1[0] == r1[1] and r1[0] == r1[2] or r1[2]!='' and r1[2]==r1[0] and r1[2]==r1[1]:
            b= r1[0]
            movelbl.config(text='%s is the winner' % b)
            btn1.config(bg='green')
            btn2.config(bg='green')
            btn3.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)


        elif r2[0] != '' and r2[0] == r2[1] and r2[0] == r2[2] or r2[2]!='' and r2[2]==r2[0] and r2[2]==r2[1] :
            b = r2[0]
            movelbl.config(text='%s is the winner' % b)
            btn4.config(bg='green')
            btn5.config(bg='green')
            btn6.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r3[0] != '' and r3[0] == r3[1] and r3[0] == r3[2] or r3[2]!='' and r3[2]==r3[0] and r3[2]==r3[1]: #3B
            b = r3[0]
            movelbl.config(text='%s is the winner' % b)
            btn7.config(bg='green')
            btn8.config(bg='green')
            btn9.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r1[0] != '' and r1[0] == r2[0] and r1[0] == r3[0] or r3[0]!='' and r3[0]==r1[0] and r3[0]==r2[0]:
            b = r1[0]
            movelbl.config(text='%s is the winner' % b)
            btn1.config(bg='green')
            btn4.config(bg='green')
            btn7.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r1[1] != '' and r1[1] == r2[1] and r1[1] == r3[1] or r3[1]!='' and r3[1]==r1[1] and r3[1]==r2[1]:
            b = r1[1]
            movelbl.config(text='%s is the winner' % b)
            btn2.config(bg='green')
            btn5.config(bg='green')
            btn8.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r1[2] != '' and r1[2] == r2[2] and r1[2] == r3[2] or r3[2]!='' and r3[2]==r1[2] and r3[2]==r2[2]:
            b = r1[2]
            movelbl.config(text='%s is the winner' % b)
            btn3.config(bg='green')
            btn6.config(bg='green')
            btn9.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r1[0] != '' and r1[0] == r2[1] and r1[0] == r3[2] or r3[2]!='' and r3[2]==r1[0] and r3[2]==r2[1]:
            b = r1[0]
            movelbl.config(text='%s is the winner' % b)
            btn1.config(bg='green')
            btn5.config(bg='green')
            btn9.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)
        elif r1[2] != '' and r1[2] == r2[1] and r1[2] == r3[0] or r3[0]!='' and r3[0]==r2[1] and r3[0]==r1[2]:
            b = r1[2]
            movelbl.config(text='%s is the winner' % b)
            btn3.config(bg='green')
            btn5.config(bg='green')
            btn7.config(bg='green')
            btn10.grid(row=3,column=0, columnspan=3, ipadx=24, ipady = 5)

    def win():
        if r1[0]!='' and r1[0]==r1[1] and r1[0]==r1[2]: #1A  #horizontal wins
            return True
        if r1[2]!='' and r1[2]==r1[0] and r1[2]==r1[1]: #1B
            return True
        if r2[0]!='' and r2[0]==r2[1] and r2[0]==r2[2]: #2A
            return True
        if r2[2]!='' and r2[2]==r2[0] and r2[2]==r2[1]: #2B
            return True
        if r3[0]!='' and r3[0]==r3[1] and r3[0]==r3[2]: #3A
            return True
        if r3[2]!='' and r3[2]==r3[0] and r3[2]==r3[1]: #3B
            return True
        if r1[0]!='' and r1[0]==r2[0] and r1[0]==r3[0]: #4A #vertical wins
            return True
        if r3[0]!='' and r3[0]==r1[0] and r3[0]==r2[0]: #4B
            return True
        if r1[1]!='' and r1[1] == r2[1] and r1[1] == r3[1]: #5A
            return True
        if r3[1]!='' and r3[1]==r1[1] and r3[1]==r2[1]: #5B
            return True
        if r1[2]!='' and r1[2] == r2[2] and r1[2] == r3[2]: #6A
            return True
        if r3[2]!='' and r3[2]==r1[2] and r3[2]==r2[2]: #6B
            return True
        if r1[0]!='' and r1[0]==r2[1] and r1[0]==r3[2]: #7A # diagonal wins
            return True
        if r3[2]!='' and r3[2]==r1[0] and r3[2]==r2[1]: #7B
            return True
        if r3[0]!='' and r3[0]==r2[1] and r3[0]==r1[2]: #8A
            return True
        if r1[2]!='' and r1[2]==r2[1] and r1[2]==r3[0]: #8B
            return True
        else:
            return False
    def cl1():
        if len(move)%2==0:
            btn1.config(text='O')
            if r1[0]=='':
                r1[0]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn1.config(text='X')
            if r1[0] == '':
                r1[0] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn1.config(command=empty)
    def cl2():
        if len(move)%2==0:
            btn2.config(text='O')
            if r1[1]=='':
                r1[1]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn2.config(text='X')
            if r1[1] == '':
                r1[1] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn2.config(command=empty)
    def cl3():
        if len(move)%2==0:
            btn3.config(text='O')
            if r1[2]=='':
                r1[2]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn3.config(text='X')
            if r1[2] == '':
                r1[2] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn3.config(command=empty)
    def cl4():
        if len(move)%2==0:
            btn4.config(text='O')
            if r2[0]=='':
                r2[0]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn4.config(text='X')
            if r2[0] == '':
                r2[0] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn4.config(command=empty)
    def cl5():
        if len(move)%2==0:
            btn5.config(text='O')
            if r2[1]=='':
                r2[1]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn5.config(text='X')
            if r2[1] == '':
                r2[1] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn5.config(command=empty)

    def cl6():
        if len(move)%2==0:
            btn6.config(text='O')
            if r2[2]=='':
                r2[2]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn6.config(text='X')
            if r2[2] == '':
                r2[2] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn6.config(command=empty)
    def cl7():
        if len(move)%2==0:
            btn7.config(text='O')
            if r3[0]=='':
                r3[0]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn7.config(text='X')
            if r3[0] == '':
                r3[0] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn7.config(command=empty)
    def cl8():
        if len(move)%2==0:
            btn8.config(text='O')
            if r3[1]=='':
                r3[1]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn8.config(text='X')
            if r3[1] == '':
                r3[1] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn8.config(command=empty)
    def cl9():
        if len(move)%2==0:
            btn9.config(text='O')
            if r3[2]=='':
                r3[2]='0'
                b = win()
                if b==True:
                    gameover()
                else:
                    btn1.config(bg='blue')
                    btn2.config(bg='blue')
                    btn3.config(bg='blue')
                    btn4.config(bg='blue')
                    btn5.config(bg='blue')
                    btn6.config(bg='blue')
                    btn7.config(bg='blue')
                    btn8.config(bg='blue')
                    btn9.config(bg='blue')
                    move.pop()
                    movelbl.config(text=turn[0],bg='blue')
        else:
            btn9.config(text='X')
            if r3[2] == '':
                r3[2] = 'X'
                b = win()
                if b == True:
                    gameover()
                else:
                    btn1.config(bg='red')
                    btn2.config(bg='red')
                    btn3.config(bg='red')
                    btn4.config(bg='red')
                    btn5.config(bg='red')
                    btn6.config(bg='red')
                    btn7.config(bg='red')
                    btn8.config(bg='red')
                    btn9.config(bg='red')
                    move.pop()
                    movelbl.config(text=turn[1],bg='red')
        btn9.config(command=empty)


    screen= Tk()
    screen.title('TIC TAC TOE')
    screen.geometry('400x400+400+200')

    turn= ["X's Turn","O's Turn"]

    move = [1,2,3,4,5,6,7,8,9]
    if len(move)%2==1:
        movelbl = Label(screen,text=turn[0],font=('times new roman',22),bg='blue',fg='yellow')
        movelbl.pack(pady=20)

    frame = Frame(screen,bg='orange')
    frame.pack(side=TOP,padx = 10, pady =5)

    font=('times new roman',38,'bold')

    btn1= Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl1)
    btn1.grid(row=0,column=0)
    btn1.bind('<Button-1>')
    btn2 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl2)
    btn2.grid(row=0,column=1)
    btn2.bind('<Button-1>')
    btn3 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl3)
    btn3.grid(row=0,column=2)
    btn3.bind('<Button-1>')
    btn4 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl4)
    btn4.grid(row=1,column=0)
    btn4.bind('<Button-1>')
    btn5 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl5)
    btn5.grid(row=1,column=1)
    btn5.bind('<Button-1>')
    btn6 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl6)
    btn6.grid(row=1,column=2)
    btn6.bind('<Button-1>')
    btn7 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl7)
    btn7.grid(row=2,column=0)
    btn7.bind('<Button-1>')
    btn8 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl8)
    btn8.grid(row=2,column=1)
    btn8.bind('<Button-1>')
    btn9 =Button(frame,text='',font=font,bg='blue',fg='#ffffff',width= 3,height=1,activebackground='#903812',activeforeground='#111111',command=cl9)
    btn9.grid(row=2,column=2)
    btn9.bind('<Button-1>')

    btn10 =Button(frame,text='Reset',font=('times new roman',20,'bold'),bg='orange',fg='#ffffff',width= 3,height=1,activebackground='blue',activeforeground='#111111',command=empty)
    

    screen.mainloop()

newgame()
