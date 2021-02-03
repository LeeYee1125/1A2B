from tkinter import*#載入模組
import random as rd
from tkinter import messagebox

def gameover():#結束遊戲內容
      MsgBox = messagebox.askquestion ('結束遊戲','是否結束遊戲?',icon = 'error')
      if MsgBox == 'yes':
          win1.destroy()
      else:
          messagebox.showinfo('歡迎','歡迎回來')

def game():#遊戲介面
    win2 = Tk()#視窗
    win2.title("開始遊戲")
    win2.configure(bg = 'lightpink' )
    win2.geometry("400x200")

    guessLabel = Label(win2,text='請輸入一組4位數:',bg = 'lightpink' ,font = (24))#玩家輸入的地方
    var = StringVar()
    guessnumber = Entry(win2,textvariable=var,bg = 'lightgray')
    guessLabel.place(x=40,y=20)
    guessnumber.place(x=210,y=25) 
    
    anser = rd.randint(1000,9999)#定義變數

    def enter():#輸入鍵內容
        guess=guessnumber.get()#遊戲開始
        guess=int(guess)
        if guess>anser:
            messagebox.showinfo("未猜中","太大了，再小一點")
            guessnumber.delete(0,'end')
        if guess < anser:
            messagebox.showinfo("未猜中","太小了，再大一點")
            guessnumber.delete(0,'end')
        if guess == anser:
            messagebox.showinfo("猜中了","恭喜你，猜中了，請按開始遊戲重新開始")
            win2.destroy()

    def stopgame():#結束按鈕內容
      MsgBox = messagebox.askquestion ('結束','重新進入後，會重新開始新遊戲，是否繼續退出?',icon = 'error')
      if MsgBox == 'yes':
          win2.destroy()
      else:
          messagebox.showinfo('歡迎','歡迎回來')

    enterbutton = Button(win2,text = '確定',command = enter,bg = 'forestgreen' ,width=10,height=5)#輸入按鈕
    stopgamebtn = Button(win2,text = '結束',command = stopgame, bg = 'crimson', width=10,height=5)#結束按鈕
    enterbutton.place(x=70,y=60)
    stopgamebtn.place(x=250,y=60)
    creatname3 = Label(win2,text = '創作者:李彥璋',bg = 'lightpink' ).place(x=320,y=157)
    creatname4 = Label(win2,text = '曲采妮',bg = 'lightpink' ).place(x=359,y=180)

    win2.mainloop()

win1 = Tk()  #開始畫面
win1.title("歡迎來到猜數字遊戲")
win1.configure(bg = 'lightblue' )
win1.geometry("400x200")

namelabel = Label(win1,text = '~~猜猜樂~~',bg = 'lightblue' ,font = (48)).place(x=150,y=10)
creatname1 = Label(win1,text = '創作者:李彥璋',bg = 'lightblue' ).place(x=320,y=157)
creatname2 = Label(win1,text = '曲采妮',bg = 'lightblue' ).place(x=359,y=180)

startgamebutton = Button(win1,text="開始遊戲",bg="green",command = game, width=10,height=5)#開始遊戲按鈕
startgamebutton.place(x=70,y=60)

gameoverbutton = Button(win1,text="結束遊戲",bg='red',command=gameover, width=10,height=5)#結束遊戲按鈕
gameoverbutton.place(x=250,y=60)

win1.mainloop()