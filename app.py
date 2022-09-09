from tkinter import *
import random

root = Tk()
root.title("")
root.geometry('300x300')
root.configure(bg = '#cfcfcf')

def raise_frame(frame):                                                 #transition b/w windows
    frame.tkraise()

frame1 = Frame(root)
frame1.config(bg= "#cfcfcf")

frame2 = Frame(root)
frame2.config(bg= "#cfcfcf")
for frame in (frame1,frame2):
    frame.grid(row=0, column=0, sticky='news')

def no():
    x = random.randint(200, 280)
    y = random.randint(200, 250)
    nobtn.place(x=x,y=y)
# def main_frame(x,y):
Label(frame1,text='Are You Stupid?',font=('Franklin Gothic Heavy','22'),fg='#000',bg='#cfcfcf',borderwidth=0).grid(row=1,column=0,columnspan=3,padx=50,pady=100)
Button(frame1,text='Yes',font=('Arial Rounded MT Bold','12'),fg='#000',bg='#cfcfcf',borderwidth=1,command = lambda:raise_frame(frame2)).grid(row=4,column=0,padx=20,pady=5)
nobtn = Button(frame1,text='No',font=('Arial Rounded MT Bold','12'),fg='#000',bg='#cfcfcf',borderwidth=1, command= lambda: no()) # 250 and above
nobtn.place(x=200,y=240)

Label(frame2,text='i knew it! :3',font=('Franklin Gothic Heavy','22'),fg='#000',bg='#cfcfcf',borderwidth=0).grid(row=1,column=0,columnspan=3,padx=19,pady=100)
#.grid(row=4,column=2,padx=20)
#,command = lambda:main_frame(1,1) 
raise_frame(frame1)
# main_frame(1,1)
root.mainloop()