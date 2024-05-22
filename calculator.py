# Simple basic calculator by using python 
import tkinter
from tkinter import * 
root = Tk()
root.title("Simple Calculator")
root.geometry("540x550+100+200")  # background measurements (width * height)
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
	global equation
	equation += value
	label_result.config(text=equation)
	
def clear():
	global equation
	equation = ""
	label_result.config(text=equation)
	
def calculate():
	global equation
	result = ""
	if equation != "":
		try:
			result = eval(equation)
		except:
			result = "error"
			equation = ""
	label_result.config(text=result)

label_result = Label(root,width=27,height=2,text="",font=("arial",30))  #result background measurements 
label_result.pack()

Button(root,text="C",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#ff0000",command=lambda: clear()).place(x=10,y=110)
Button(root,text="/",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("/")).place(x=150,y=110)
Button(root,text="%",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("%")).place(x=290,y=110)
Button(root,text="*",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("*")).place(x=430,y=110)

Button(root,text="7",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("7")).place(x=10,y=190)
Button(root,text="8",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("8")).place(x=150,y=190)
Button(root,text="9",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("9")).place(x=290,y=190)
Button(root,text="-",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("-")).place(x=430,y=190)

Button(root,text="4",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("4")).place(x=10,y=270)
Button(root,text="5",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("5")).place(x=150,y=270)
Button(root,text="6",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("6")).place(x=290,y=270)
Button(root,text="+",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("+")).place(x=430,y=270)

Button(root,text="1",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("1")).place(x=10,y=350)
Button(root,text="2",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("2")).place(x=150,y=350)
Button(root,text="3",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("3")).place(x=290,y=350)
Button(root,text="0",width=9, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("0")).place(x=10,y=440)

Button(root,text=".",width=3, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show(".")).place(x=290,y=440)
Button(root,text="=",width=3, height=3, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#00ff00",command=lambda: calculate() ).place(x=430,y=350)


root.mainloop()


