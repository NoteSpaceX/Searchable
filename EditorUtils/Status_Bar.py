from tkinter import Frame, X, SUNKEN, W, Label


class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W, height="1",background="#E8E8E8")
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args, font="{Arial} 10", foreground="#404040")
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()