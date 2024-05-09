from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter.filedialog import *
import pyautogui
import instaloader



class St():
    def __init__(self,root):
        self.num_var= StringVar()
        self.pro_name= StringVar()
        self.root=root
        self.root.geometry('157x120+20+20')
        self.root.resizable(0,0)
        nb=ttk.Notebook(self.root)
        self.root.config(bg='grey')
        nb.pack()
        title= Label(self.root,text='Hyouka',bg='black',fg='grey',height=4,font=('Arial Bold',15)).pack(fill=X,)
        frame1= Frame(nb,width="410",height='440',bg='#A569BD')
        nb.add(frame1,text="ScreenShot",)
        frame2= Frame(nb,width="410",height='440')
        nb.add(frame2,text='IST download')


        ent= Entry(frame1,bd=2,justify='center',textvariable=self.num_var,cursor='heart',width=25)
        ent.grid(row=0,column=0,padx=0,pady=0)
        print(ent.get())
        but=Button(frame1,justify='left',text='TAKE Screenshot',bg='#3498DB',width=20,height=5,activebackground='#F1948A',activeforeground='#2E86C1',
        command=self.screenshot2)
        but.grid(column=0,row=1,padx=0,pady=0,columnspan=1)
        en1= Entry(frame2,bd=2,justify='center',cursor='heart',textvariable=self.pro_name,width=25)
        en1.grid(column=0,row=0,padx=0,pady=0,)
        #---------------buttons------------------
        b1= Button(frame2,text='Go',activebackground='red',activeforeground='blue',width=21,height=5,command=self.load,justify='left',bg='#3498DB')
        #width=16,height=5
        b1.grid(column=0,row=1,padx=0,pady=0)
    def screenshot2(self,):
        try:
            r=int(self.num_var.get())
            time.sleep(int(r))
            screen= pyautogui.screenshot()
            file_name=asksaveasfilename()
            screen.save(file_name+'_screenshot_hehe.jpg')
            messagebox.showinfo('saving','The screenshot saved in your Pc',)
            
        except Exception as e:
            print(e)
            messagebox.showerror('eror 502','enter some interroger not strings or enter some number')
        self.num_var.set('')


        #insta
    

    def load(self):
        try:
            
            profile_name=self.pro_name.get() 
            instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
            messagebox.showinfo('The download is Complete!','Check the directory some dossier was created with the same name you searche it')
            self.pro_name.set('')
        except Exception as e:
            messagebox.showerror(e," Eror try again maybe the name is incorrect or check internet connection")
            self.pro_name.set('')
        

        

root=Tk()
ob=St(root=root)
root.mainloop()
#nb.select(frame2)
