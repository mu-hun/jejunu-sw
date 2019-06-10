import tkinter


window = tkinter.Tk()
window.title('win')
window.geometry('100x100+10+10')
window.resizable(True, True)

lable = tkinter.Label(window, text='결과:')
lable.pack()

entry = tkinter.Entry(window)
entry.bind('<Return>', lambda _: lable.config(text=eval(entry.get())))
entry.pack()

window.mainloop()
