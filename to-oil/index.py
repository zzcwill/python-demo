import tkinter as tk
import view

page = tk.Tk()

page.geometry('600x400+400+300')

page.minsize(600, 400)
page.maxsize(600,400)

page.title('加油计费程序')

view.main(page)

page.mainloop()