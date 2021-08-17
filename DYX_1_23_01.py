import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

import numpy as np
from PIL import Image,ImageTk
from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

img_png =None

def btLogin_click():  #登录按钮的事件响应函数，点击该按钮时被调用
    if username.get() == "1" and password.get()  == "1": #正确的用户名和密码
        lbHint["text"] = "登录成功!"  #修改lbHint的文字
        lbHint["fg"] = "black"	#文字变成黑色，"fg"表示前景色,"bg"表示背景色
        win.destroy()
        create()
    else:
        username.set("")  #将用户名输入框清空
        password.set("")  #将密码输入框清空
        lbHint["fg"] = "red"  #文字变成红色
        lbHint["text"] =  "用户名密码错误，请重新输入!"

def cbPassword_click(): #“显示密码”单选框的事件响应函数，点击该单选框时被调用
    if showPassword.get():  #showPassword是和cbPassword绑定的tkinter布尔变量
        etPassword["show"] = ""  #使得密码输入框能正常显示密码。Entry有show属性
    else:
        etPassword["show"] = "*" #使得密码输入框只显示'*'字符




def create():
    win2 = tk.Tk()
    win2.title('石头剪子布图像辨别系统')

    # frm01Red = tk.Frame(win2, bg="gray", highlightthickness=2)  # 背景红色，边框宽度2
    # frm01Red.grid(row=0, column=1, sticky="WE")
    # tk.Label(frm01Red, text="姓名：1").grid(row=0, column=0, padx=6, pady=6)
    # tk.Entry(frm01Red).grid(row=0, column=1, padx=6, pady=6)


    frm00Blue = tk.Frame(win2, bg="gray", highlightthickness=2)
    frm00Blue.grid(row=0, column=0, rowspan=2, sticky="NS")
    frm00Blue.rowconfigure(12, weight=1)
    tk.Label(frm00Blue, text="石头/剪子/布").grid(row=0,
                                           padx=6, pady=6, sticky="W")
    tk.Button(frm00Blue, text="输入图片", command=lambda:innerCmd1()).grid(row=1,
                                           padx=6, pady=6, sticky="W")

    # tk.Label(frm00Blue, text="人/马").grid(row=2,
    #                                        padx=6, pady=6, sticky="W")
    # tk.Button(frm00Blue, text="输入图片", command=lambda:innerCmd()).grid(row=3,
    #                                        padx=6, pady=6, sticky="W")
    # tk.Label(frm00Blue, text="猫/狗").grid(row=4,
    #                                        padx=6, pady=6, sticky="W")
    # tk.Button(frm00Blue, text="输入图片", command=lambda:innerCmd()).grid(row=5,
    #                                        padx=6, pady=6, sticky="W")


    frm21Green = tk.Frame(win2, bg='gray', highlightthickness=2)
    frm21Green.grid(row=2, column=0, columnspan=2, sticky="WE")
    tk.Label(frm21Green, text="提示：目前一切正常").grid(row=0, padx=6, pady=6)

    frm11Yellow = tk.Frame(win2, bg='yellow', highlightthickness=2)
    frm11Yellow.grid(row=1, column=1, sticky="NSWE")  # 要贴住单元格四条边
    frm11Yellow.rowconfigure(1, weight=1)  # 使得frm11Yellow中第1行高度会自动伸缩
    frm11Yellow.columnconfigure(0, weight=1)
    tk.Label(frm11Yellow).grid(row=1, padx=250, pady=250, sticky="NSWE")

    # sticky="NSWE"使得该多行编辑框会自动保持填满整个单元格

    def innerCmd1():
        # https: // blog.csdn.net / qq_28888837 / article / details / 113716814
        value_innerCmd = filedialog.askopenfilenames(title='打开文件',filetypes=[('images', '*.jpg *.png'), ('All Files', '*')])
        if value_innerCmd != "":
            print(value_innerCmd)
            global img_png
            img_open = Image.open(value_innerCmd[0])
            img_png = ImageTk.PhotoImage(img_open)
            tk.Label(frm11Yellow,image = img_png)

            tk.Label(frm11Yellow,text="我爱阅读",image=img_png,compound = tk.CENTER,font=("华文行楷",20),fg = "white")

        return value_innerCmd




win = tk.Tk()
win.title("系统登录")
username,password = tk.StringVar(),tk.StringVar()
#两个字符串类型变量，分别用于关联用户名输入框和密码输入框

lbHint = tk.Label(win,text = "请登录")
lbHint.grid(row=0,column=0,columnspan=2)

lbUsername = tk.Label(win,text="用户名：")
lbUsername.grid(row=1,column=0,padx=5,pady=5)

lbPassword = tk.Label(win,text="密码：")
lbPassword.grid(row=2,column=0,padx=5,pady=5)

etUsername = tk.Entry(win,textvariable = username)
#输入框etUsername和变量username关联
etUsername.grid(row=1,column = 1,padx=5,pady=5)

etPassword = tk.Entry(win,textvariable = password,show="*")
#Entry的属性show="*"表示该输入框不论内容是啥，只显示'*'字符，为""则正常显示
etPassword.grid(row=2,column = 1,padx=5,pady=5)

showPassword = tk.BooleanVar() #用于关联“显示密码”单选框
showPassword.set(False)  #使得cbPassowrd开始就是非选中状态
cbPassword = tk.Checkbutton(win,text="显示密码",
                            variable=showPassword,command=cbPassword_click)
#cbPassword关联变量showPassword，其事件响应函数是cbPassword_click，即点击它时，
#会调用 cbPassword_click()
cbPassword.grid(row=3,column = 0,padx=5,pady=5)

btLogin = tk.Button(win,text="登录",command=btLogin_click)
#点击btLogin按钮会执行btLogin_click()
btLogin.grid(row=4,column=0,pady=5)

btQuit = tk.Button(win,text="退出",command=win.quit)
#点击btQuit会执行win.quit()，win.quit()导致窗口关闭，于是整个程序结束
btQuit.grid(row=4,column=1,pady=5)

win.mainloop()

