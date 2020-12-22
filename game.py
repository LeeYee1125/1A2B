from tkinter import*
win = Tk()  #製作按鈕
win.title("請問是否要繼續下一場遊戲?")
win.geometry("400x200")

def game():
    import random   #1A2B遊戲碼
    x=random.sample('1234567890',4)
    play=True
    while play:
        y=input("輸入4個不同數字:")
        z=list(y)
        a=0
        b=0
        t=0
        n=0    
        for i in range(4):
            if x[i]==z[i]:
                a=a+1
            t=t+1
            for i in range(4):
                for j in range(4):
                    if i == j:
                        pass
                    else:
                        if x[i]==z[j]:
                            b = b + 1 
                            n=n+1       
            print(a,'A', b, 'B')
            if a==4:
                play=False
            print('總共花了',t+n,'次')

def off():
      print("謝謝，歡迎再來玩")

btn1 = Button(text="開始遊戲",bg="green")
btn1.config(command = game)
btn1.pack()

btn2 = Button(text="是",bg="yellow")
btn2.config(command = game)
btn2.pack()

btn3 = Button(text="否")
btn3.config(commang = off)
btn3.pack()

win.mainloop()