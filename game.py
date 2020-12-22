from tkinter import*
win = Tk()  #製作按鈕
win.title("請問是否要開始遊戲?")
win.geometry("400x200")

#def game():
    #import random   #1A2B
#x=random.sample('1234567890',4)
#i=0
#j=0
#t=0
#while play:
    #y = input("請輸入你猜的4位數字:")
    #z = list(y)
    #if x == z:
      #t=t+1
      #print("4A0B","共猜",t,"次") 
      #break
      #win.mainloop()    
    #else: 
      #a=0
      #b=0     
      #t=t+1
      #for i in range(4):
        #if x[i] == z[i]:
          #a=a+1
      #for i in range(4):
       # for j in range(4):
          #if i == j:
            #pass
          #else:
            #if x[i] == z[j]:
              #b = b + 1            
      #print(a,"A",b,"B")     
      #continue

#def off():
      #print("謝謝，歡迎再來玩")

btn1 = Button(text="開始遊戲",bg="sky blue")
#btn1.config(command = game)
btn1.pack()

btn2 = Button(text="結束遊戲",bg="red")
#btn2.config(commang = off)
btn2.pack()

win.mainloop()