from tkinter import*
light=Tk()
light.title("Simple Calculator")
light.iconbitmap("calcu.ico")
e=Entry(light,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()                                                         #get the value from entry box in current variable set
    e.delete(0,END)
    e.insert(0,str(current)+str(number)) 

def button_clear():
    e.delete(0,END)                                                                               #sceeen clear

def button_add():
    first_number=e.get()                                        #access first number from entry box (they are in string)
    global f_num                #access globally cause its defined inside the function which automatically makes it local variable
    global math
    math = "addition"
    f_num=int(first_number)                     #the store string value is convetred into int
    e.delete(0,END)                                     #clicking operation button clears the screen

def button_equal():
    second_number=e.get()                                              #access second number from entry box
    e.delete(0,END)
    if math == "addition":
            e.insert(0,f_num+int(second_number))                   #convet into int value from str value
    if math=="sub":
         e.insert(0,f_num-int(second_number))
    if math=="mul":
        e.insert(0,f_num*int(second_number))
    if math=="div":
        e.insert(0,f_num//int(second_number))

def button_sub():
    first_number=e.get()
    global f_num
    global math
    math = "sub"
    f_num=int(first_number)
    e.delete(0,END)

def button_mul():
    first_number=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    global math
    math="div"
    f_num=int(first_number)
    e.delete(0,END)



button1=Button(light,text="1",padx=40,pady=20,command=lambda :button_click(1))      #for taking one exp only 
button2=Button(light,text="2",padx=40,pady=20,command=lambda:button_click(2))
button3=Button(light,text="3",padx=40,pady=20,command=lambda:button_click(3))
button4=Button(light,text="4",padx=40,pady=20,command=lambda:button_click(4))
button5=Button(light,text="5",padx=40,pady=20,command=lambda:button_click(5))
button6=Button(light,text="6",padx=40,pady=20,command=lambda:button_click(6))
button7=Button(light,text="7",padx=40,pady=20,command=lambda:button_click(7))
button8=Button(light,text="8",padx=40,pady=20,command=lambda:button_click(8))
button9=Button(light,text="9",padx=40,pady=20,command=lambda:button_click(9))
button0=Button(light,text="0",padx=40,pady=20,command=lambda:button_click(0))

button_add=Button(light,text='+',padx=39,pady=20,command=button_add)
button_equal=Button(light,text="=",padx=87,pady=20,command=button_equal)
button_sub=Button(light,text="-",padx=40,pady=20,command=button_sub)
button_mul=Button(light,text="*",padx=39,pady=20,command=button_mul)
button_div=Button(light,text="/",padx=41,pady=20,command=button_div)
button_clear=Button(light,text="Clear",padx=77,pady=20,command=button_clear)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)
print("Hello world")

light.mainloop()
