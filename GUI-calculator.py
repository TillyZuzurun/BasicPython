from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk() #Tตัวใหญ่ kตัวเล็ก
GUI.title('โปรแกรมคำนวนราคาปลา')
GUI.geometry('700x600')

bg = PhotoImage(file='fish2.png')

BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา(กิโลกรัม)',font=(None,20))
L.pack()

v_quantity = StringVar() #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จ
E1 = ttk.Entry(GUI, textvariable=v_quantity,font=(None,20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 39 # 39 บาทต่อกิโล * จำนวนปลา
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity.set('')
		E1.focus()	
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลข')
		v_quantity.set('1')

B = ttk.Button(GUI, text='คำนวน',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ความกว้างปุ่ม x,y

GUI.mainloop() #ให้โปรแกรมรันตลอด