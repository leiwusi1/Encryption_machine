import main
import tkinter as tk
import tkinter.messagebox
t = main.text()
root = tk.Tk()
def a():
    if tkinter.messagebox.askokcancel("试图挽回希望的窗口","你真的要退出吗？"):
        root.destroy()




root.protocol("WM_DELETE_WINDOW", a)
root.configure(bg='white')
root.title("加密机")
root.geometry('1200x700')

L1 = tk.Label(root, text="要加密的文本：",font=("苹方字体",50))
L2 = tk.Label(root, text="要解密的文本：",font=("苹方字体",50))
L1.place(x=30,y=60)
L2.place(x=30,y=200)
L3 = tk.Label(root, text="温馨提示：加密时数字用文字输入，否则会出错！",font=("苹方字体",30))
L3.place(x=250,y=600)
secret = tk.StringVar()
text = tk.StringVar()

entry = tk.Entry(root, textvariable=text,font=("苹方字体",50))
entry.pack()
entry.place(x=390, y=57)

entry = tk.Entry(root, textvariable=secret,font=("苹方字体",50))
entry.pack()
entry.place(x=390, y=197)

def se():
    t.input_txt(text.get())
    t.produce()
    if tkinter.messagebox.askokcancel("", "你确定要加密吗，这会使原文本消失"):
        secret.set(t.txt)
        text.set("")

Bot1 = tk.Button(root, text = "加密",command=lambda :se(),height=10,width=30)
Bot1.place(x = 120, y = 360)

def va():
    t.input_txt(secret.get())
    t.decoding()
    if tkinter.messagebox.askokcancel("", "你确定要解密吗，这会使原文本消失"):
        text.set(t.txt)
        secret.set("")

Bot1 = tk.Button(root, text = "解密",command=lambda :va(),height=10,width=30)
Bot1.place(x = 550, y = 360)


root.mainloop()