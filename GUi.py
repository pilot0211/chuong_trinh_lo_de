import tkinter
import random
giao_dien = tkinter.Tk()
giao_dien.title("Chương trình lô đề")
giao_dien.geometry('800x700')
font = ("Comic Sans MS",18)
#def
tb6 = 1000000
list = []
def onclick():
    global list
    list.clear()
    Giaidacbiet = '{:05d}'.format(random.randint(0, 100000))
    Giai1 = '{:05d}'.format(random.randint(0, 100000))
    Giai2 = '{:05d}'.format(random.randint(0, 100000))
    Giai2a = '{:05d}'.format(random.randint(0, 100000))
    Giai3 = '{:05d}'.format(random.randint(0, 100000) )
    Giai3a = '{:05d}'.format(random.randint(0, 100000)) 
    Giai3b = '{:05d}'.format(random.randint(0, 100000)) 
    Giai3c = '{:05d}'.format(random.randint(0, 100000) )
    Giai3d = '{:05d}'.format(random.randint(0, 100000)) 
    Giai3e = '{:05d}'.format(random.randint(0, 100000) )
    Giai4 = '{:04d}'.format(random.randint(0, 10000) )
    Giai4a = '{:04d}'.format(random.randint(0, 10000)) 
    Giai4b = '{:04d}'.format(random.randint(0, 10000) )
    Giai4c = '{:04d}'.format(random.randint(0, 10000) )
    Giai5 = '{:04d}'.format(random.randint(0, 10000) )
    Giai5a = '{:04d}'.format(random.randint(0, 10000) )
    Giai5b = '{:04d}'.format(random.randint(0, 10000)) 
    Giai5c = '{:04d}'.format(random.randint(0, 10000) )
    Giai5d = '{:04d}'.format(random.randint(0, 10000) )
    Giai5e = '{:04d}'.format(random.randint(0, 10000)) 
    Giai6 = '{:03d}'.format(random.randint(0, 1000) )
    Giai6a = '{:03d}'.format(random.randint(0, 1000) )
    Giai6b = '{:03d}'.format(random.randint(0, 1000) )
    Giai7 = '{:02d}'.format(random.randint(0, 100))
    Giai7a = '{:02d}'.format(random.randint(0, 100)) 
    Giai7b = '{:02d}'.format(random.randint(0, 100) )
    Giai7c = '{:02d}'.format(random.randint(0, 100))
    list.append(int(Giaidacbiet)%100)
    list.append(int(Giai1)%100)
    list.append(int(Giai2)%100)
    list.append( int(Giai2a)%100)
    list.append(int(Giai3)%100)
    list.append(int(Giai3a)%100)
    list.append(int(Giai3b)%100)
    list.append(int(Giai3c)%100)
    list.append(int(Giai3d)%100)
    list.append(int(Giai3e)%100)
    list.append(int(Giai4)%100)
    list.append(int(Giai4a)%100)
    list.append(int(Giai4b)%100)
    list.append(int(Giai4c)%100)
    list.append( int(Giai5)%100)
    list.append(int(Giai5a)%100)
    list.append(int(Giai5b)%100)
    list.append(int(Giai5c)%100)
    list.append(int(Giai5d)%100)
    list.append(int(Giai5e)%100)
    list.append(int(Giai6)%100)
    list.append(int(Giai6a)%100)
    list.append(int(Giai6b)%100)
    list.append(int(Giai7)%100)
    list.append(int(Giai7a)%100)
    list.append(int(Giai7b)%100)
    list.append(int(Giai7c )%100)
    text_box5.configure(state="normal")
    text_box5.delete('1.0', 'end')  
    text_box5.insert(tkinter.INSERT, "Giải Đb:"+"\t\t\t"+ str(Giaidacbiet)+ "\n")
    text_box5.insert(tkinter.INSERT, "   1:"+"\t\t\t"+ str(Giai1)+ "\n")
    text_box5.insert(tkinter.INSERT, "   2:"+"\t\t     "+ str(Giai2)+ " "+str(Giai2a) +'\n')
    text_box5.insert(tkinter.INSERT, "   3:"+"\t\t   "+ str(Giai3)+ " "+str(Giai3a)+' '+str(Giai3b) +"\n"+"\t\t   "+str(Giai3c)+" "+str(Giai3d)+' '+str(Giai3e)+'\n')
    text_box5.insert(tkinter.INSERT, "   4:"+"\t\t  "+ str(Giai4)+" "+str(Giai4a)+ " "+str(Giai4b)+ " "+ str(Giai4c) +"\n")
    text_box5.insert(tkinter.INSERT, "   5:"+"\t\t    "+ str(Giai5)+ " "+str(Giai5a)+' '+str(Giai5b) +"\n"+"\t\t    "+str(Giai5c)+" "+str(Giai5d)+' '+str(Giai5e)+'\n')
    text_box5.insert(tkinter.INSERT, "   6:"+"\t\t     "+ str(Giai6)+" "+str(Giai6a)+ " "+str(Giai6b) +"\n")
    text_box5.insert(tkinter.INSERT, "   7:"+"\t\t     "+ str(Giai7)+" "+str(Giai7a)+ " "+str(Giai7b)+ " "+ str(Giai7c))
    text_box5.configure(state='disable')
def count():
    global list
    global tb6
    if tb1.get() in list:
        tb6 = tb6 -(tb2.get()*23000)+(tb2.get()*80000)
        tb7.set(str(tb6)+" VNĐ")
    else:
        tb6 = tb6 -(tb2.get()*23000)
        tb7.set(str(tb6)+" VNĐ")
        list1 = tb7.get().split()
        if(int(list1[0])<=0):
            btn1.configure(state="disable")
            tb7.set("số tiền của bạn đã hết")
def count1():
    global list
    global tb6
    if(tb3.get()==list[0]):
        tb6 = tb6 -(tb4.get()*10000)+(tb4.get()*700000)
        tb7.set(str(tb6)+" VNĐ")
    else:
        tb6 = tb6 -(tb4.get()*10000)
        tb7.set(str(tb6)+" VNĐ")
        list1 = tb7.get().split()
        if(int(list1[0])<=0):
            btn2.configure(state="disable")
            tb7.set("số tiền của bạn đã hết")       
#label
Font_tuple = ("Comic Sans MS", 15, "bold")
label = tkinter.Label(giao_dien,text="CHƯƠNG TRÌNH LÔ ĐỀ" ,fg='black',font=Font_tuple)
label.place(relx = 0.5, rely = 0.05, anchor = 'center')

label1 = tkinter.Label(giao_dien,text="I. Chơi lô" ,fg='black',font=font)
label1.place(relx = 0.05, rely = 0.07)

label2 = tkinter.Label(giao_dien,text="Chọn số: " ,fg='black',font=("Comic Sans MS",15))
label2.place(relx = 0.05, rely = 0.12)

label3 = tkinter.Label(giao_dien,text="Đánh mấy điểm : " ,fg='black',font=("Comic Sans MS",15))
label3.place(relx = 0.5, rely = 0.12)

label4 = tkinter.Label(giao_dien,text="1 điểm = 23000VNĐ " ,fg='black',font=("Comic Sans MS",12))
label4.place(relx = 0.7, rely = 0.17)

label5 = tkinter.Label(giao_dien,text="II. Chơi đề" ,fg='black',font=font)
label5.place(relx = 0.05, rely = 0.20)

label6 = tkinter.Label(giao_dien,text="Chọn số: " ,fg='black',font=("Comic Sans MS",15))
label6.place(relx = 0.05, rely = 0.25)

label7 = tkinter.Label(giao_dien,text="Đánh mấy điểm : " ,fg='black',font=("Comic Sans MS",15))
label7.place(relx = 0.5, rely = 0.25)

label8 = tkinter.Label(giao_dien,text="1 điểm = 10000VNĐ " ,fg='black',font=("Comic Sans MS",12))
label8.place(relx = 0.7, rely = 0.3)

label9 = tkinter.Label(giao_dien,text="Tổng Tiền: " ,fg='black',font=font)
label9.place(relx = 0.05, rely = 0.7)

label10 = tkinter.Label(giao_dien,text="Số tiền còn lại: " ,fg='black',font=font)
label10.place(relx = 0.05, rely = 0.8)

#text box
tb1 = tkinter.IntVar()
text_box1 = tkinter.Entry(giao_dien,textvariable=tb1)
text_box1.place(relx = 0.17, rely = 0.13,width=200)

tb2 = tkinter.IntVar()
text_box2 = tkinter.Entry(giao_dien,textvariable=tb2)
text_box2.place(relx = 0.7, rely = 0.13,width=200)

tb3 = tkinter.IntVar()
text_box3= tkinter.Entry(giao_dien,textvariable=tb3)
text_box3.place(relx = 0.17, rely = 0.25,width=200)

tb4 = tkinter.IntVar()
text_box4 = tkinter.Entry(giao_dien,textvariable=tb4)
text_box4.place(relx = 0.7, rely = 0.25,width=200)

text_box5 = tkinter.Text(giao_dien)
text_box5.place(relx = 0.5,rely = 0.5,anchor="center",width=350,height=200)
text_box5.configure(state="disable")

tb6a = tkinter.StringVar(value=str(tb6)+' VNĐ')
text_box6 = tkinter.Entry(giao_dien, width = 18,bg='#dcdcdc', relief='flat',textvariable=tb6a,font=font)
text_box6.place(relx = 0.23, rely = 0.7)
text_box6.configure(state='disable')

tb7 = tkinter.StringVar()
text_box7 = tkinter.Entry(giao_dien, width = 18,bg='#dcdcdc', relief='flat',textvariable=tb7,font=font)
text_box7.place(relx = 0.27, rely = 0.8)
text_box7.configure(state='disable')

#button
btn1 = tkinter.Button(giao_dien,text='Chơi đi đừng sợ',command=lambda:[onclick(),count()],activebackground='#dcdcdc')
btn1.place(relx = 0.5, rely = 0.17)

btn2 = tkinter.Button(giao_dien,text='Chơi đi đừng sợ',command=lambda:[onclick(),count1()],activebackground='#dcdcdc')
btn2.place(relx = 0.5, rely = 0.3)




giao_dien.mainloop()