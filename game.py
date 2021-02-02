from tkinter import*#載入模組
import random as rd
from tkinter import messagebox

def gameover():#結束遊戲內容
      MsgBox = messagebox.askquestion ('結束遊戲','是否繼續退出?',icon = 'error')
      if MsgBox == 'yes':
          win1.destroy()
      else:
          messagebox.showinfo('歡迎','歡迎回來')

def game():#遊戲介面
    win2 = Tk()#視窗
    win2.title("開始遊戲")
    win2.geometry("400x200")

    guessLabel = Label(win2,text='請輸入一組2位數')#玩家輸入的地方
    guessnumber = Entry(win2)
    guessLabel.pack()
    guessnumber.pack() 
    
    anser = rd.randint(10,99)#定義變數

    def enter():#輸入鍵內容
        num = 0
        play = True
        while True:#遊戲開始
            guess = int(guessnumber.get())
            if anser == guess:
                num+=1
                play = False
                MsgBox = messagebox.askquestion ('獲勝','恭喜你贏得勝利，是否繼續下一局?',icon = 'warning')
                if MsgBox == 'yes':
                    reset()
                else:
                    win2.destroy()
            elif anser < guess:
                Label(win2,text = '太大了，再小一點!')
                num+=1
            else :
                Label(win2,text = '太小了，再大一點!')
                num+=1

        def numguess():#猜的次數
            if num == 1 :
                Label(win2,text = '好厲害，一次就答對了')
            elif 1 < num < 20 :
                Label(win2,text = '不錯喔，你很有實力!')
            else :
                Label(win2,text = '再加油吧，已經猜超過20次了!')

    def reset():#重玩內容
        global num
        global running
        anser = rd.randint(10,99)
        num = 0
        running = True
        guessnumber.delete(0,'end')
        resetlabel = messagebox.showinfo('重新開始','重新一局新遊戲')


    def stopgame():#結束按鈕內容
      MsgBox = messagebox.askquestion ('結束','重新進入後，會重新開始新遊戲，是否繼續退出?',icon = 'error')
      if MsgBox == 'yes':
          win2.destroy()
      else:
          messagebox.showinfo('歡迎','歡迎回來')

    enterbutton = Button(win2,text = '確定',command = enter)#輸入按鈕
    resetbutton = Button(win2,text = '重新一局',command = reset)#重玩按鈕
    stopgamebtn = Button(win2,text = '結束',command = stopgame)#結束按鈕
    enterbutton.pack()
    resetbutton.pack()
    stopgamebtn.pack()

    win2.mainloop()

win1 = Tk()  #開始畫面
win1.title("歡迎來到猜數字遊戲")
win1.geometry("400x200")

startgamebutton = Button(win1,text="開始遊戲",bg="green",command = game)#開始遊戲按鈕
startgamebutton.pack()

gameoverbutton = Button(win1,text="結束遊戲",bg='red',command=gameover)#結束遊戲按鈕
gameoverbutton.pack()

win1.mainloop()