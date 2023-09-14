
from tkinter import *
from tkinter import ttk

class calc:
    def __init__(self,root):
        self.root=root
        self.root.title('CALCULATER')
        self.root.geometry('400x440+300+150')
        self.root.resizable(False,False)
        
        
        diff=70
        row1=85
        row2=row1+diff*1
        row3=row1+diff*2
        row4=row1+diff*3
        row5=row1+diff*4
    

        self.scvalue = StringVar()
        self.scvalue.set("")
        self.main_text = Entry(self.root,textvariable=self.scvalue,width=50 ,font="ariel, 20 italic bold")
        self.main_text.pack(padx=10,pady=10)

        def add():
            a=10

        def click(event):
            # global self.scvalue
            text=event.widget.cget("text")
            # print("\u221a")
            if text=='=':
                if self.scvalue.get().isdigit():
                    value = int(self.scvalue.get())
                else:
                    gotRoot=False
                    str=""
                    length=len(self.scvalue.get())
                    cntr=0
                    for i in self.scvalue.get():
                        cntr=cntr+1
                        if i!="√":
                            # print(i.isdigit())
                            if gotRoot==True and i.isdigit()==False:
                                str=str+"**(1/2)"
                                gotRoot=False

                            str=str+i    
                            
                            print(length)
                            print(cntr)
                            if gotRoot==True and i.isdigit()==True and cntr==length:
                                str=str+"**(1/2)"
                                gotRoot=False
                        else:
                            gotRoot=True    
                    print(str)        
                    # str=self.scvalue.get()  
                    value= eval(str)        
                
                self.scvalue.set(value)
                self.main_text.update()

            elif text=="<-":
                str=self.scvalue.get()
                str=str[:len(str)-1]
                self.scvalue.set(str)
                self.main_text.update()

            elif text=="c":
                self.scvalue.set("")
                self.main_text.update()
            elif text=="√":
                self.scvalue.set(self.scvalue.get()+"√")
                self.main_text.update()       
            else:
                self.scvalue.set(self.scvalue.get()+text)
                self.main_text.update()
            
            # a=4*4+2**(1/2)
            # print(a)

            # new=self.main_text.get(0)+f"{a}"
            # self.main_text.insert(1, f"{new}")
            
            # str=str(line)
            # str=str+f"{a}"
            # self.main_text.insert(0,str)
        
        self.button1 = Button(self.root,text="c", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button1.place(x=10,y=row1)
        self.button1.bind("<Button-1>",click)

        self.button2 = Button(self.root,text="√", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button2.place(x=117,y=row1)
        self.button2.bind("<Button-1>",click)

        self.button3 = Button(self.root,text="/", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button3.place(x=217,y=row1)
        self.button3.bind("<Button-1>",click)

        self.button4 = Button(self.root,text="<-", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button4.place(x=317,y=row1)
        self.button4.bind("<Button-1>",click)

        self.button5 = Button(self.root,text="7", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button5.place(x=10,y=row2)
        self.button5.bind("<Button-1>",click)

        self.button6 = Button(self.root,text="8", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button6.place(x=117,y=row2)
        self.button6.bind("<Button-1>",click)

        self.button7 = Button(self.root,text="9", font="sarif, 20 bold italic ", width=3, 
        bd=5,bg='purple',fg='white', command=add)
        self.button7.place(x=217,y=row2)
        self.button7.bind("<Button-1>",click)

        self.button8 = Button(self.root,text="*", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button8.place(x=317,y=row2)
        self.button8.bind("<Button-1>",click)

        self.button9 = Button(self.root,text="4", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button9.place(x=10,y=row3)
        self.button9.bind("<Button-1>",click)

        self.button10 = Button(self.root,text="5", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button10.place(x=117,y=row3)
        self.button10.bind("<Button-1>",click)

        self.button11 = Button(self.root,text=f"{6}", font="sarif, 20 bold italic ", width=3, 
        bd=5,bg='purple',fg='white', command=add)
        self.button11.place(x=217,y=row3)
        self.button11.bind("<Button-1>",click)

        self.button20 = Button(self.root,text="-", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button20.place(x=317,y=row3)
        self.button20.bind("<Button-1>",click)

        self.button12 = Button(self.root,text="1", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button12.place(x=10,y=row4)
        self.button12.bind("<Button-1>",click)

        self.button13 = Button(self.root,text="2", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button13.place(x=117,y=row4)
        self.button13.bind("<Button-1>",click)

        self.button14 = Button(self.root,text="3", font="sarif, 20 bold italic ", width=3, 
        bd=5,bg='purple',fg='white', command=add)
        self.button14.place(x=217,y=row4)
        self.button14.bind("<Button-1>",click)

        self.button15 = Button(self.root,text="+", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button15.place(x=317,y=row4)
        self.button15.bind("<Button-1>",click)

        self.button16 = Button(self.root,text="!", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button16.place(x=10,y=row5)
        self.button16.bind("<Button-1>",click)

        self.button17 = Button(self.root,text="0", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button17.place(x=117,y=row5)
        self.button17.bind("<Button-1>",click)

        self.button18 = Button(self.root,text=".", font="sarif, 20 bold italic ", width=3, 
        bd=5,bg='purple',fg='white', command=add)
        self.button18.place(x=217,y=row5)
        self.button18.bind("<Button-1>",click)

        self.button19 = Button(self.root,text="=", font="sarif, 20 bold italic ", width=3, bd=5,bg='purple',fg='white', command=add)
        self.button19.place(x=317,y=row5)
        self.button19.bind("<Button-1>",click)


def main():
    root=Tk()
    ui=calc(root)
    root.mainloop()

if __name__== "__main__":
    main()
