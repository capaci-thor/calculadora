import tkinter as tk

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.B1= tk.Button(self, text = "1", fg = "gray", command = self.numero_1)
        self.B1.grid(row=1, column=1)
        self.B2= tk.Button(self, text = "2", fg = "gray", command = self.numero_2)
        self.B2.grid(row=1, column=2)
        self.B3= tk.Button(self, text = "3", fg = "gray",command = self.numero_3)
        self.B3.grid(row=1, column=3)
        self.B4= tk.Button(self, text = "4", fg = "gray", command = self.numero_4)
        self.B4.grid(row=2, column=1)
        self.B5= tk.Button(self, text = "5", fg = "gray", command = self.numero_5)
        self.B5.grid(row=2, column=2)
        self.B6= tk.Button(self, text = "6", fg = "gray",command = self.numero_6)
        self.B6.grid(row=2, column=3)
        self.B7= tk.Button(self, text = "7", fg = "gray", command = self.numero_7)
        self.B7.grid(row=3, column=1)
        self.B8= tk.Button(self, text = "8", fg = "gray", command = self.numero_8)
        self.B8.grid(row=3, column=2)
        self.B9= tk.Button(self, text = "9", fg = "gray",command = self.numero_9)
        self.B9.grid(row=3, column=3) 
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("")
        self.entrythingy["textvariable"] = self.contents  

    def numero_1(self):
        print("Número 1")
        self.contents.set(self.contents.get()+str(1))
    def numero_2(self):
        print("Número 2")
        self.contents.set(self.contents.get()+str(2))
    def numero_3(self):
        print("Número 3")
        self.contents.set(self.contents.get()+str(3))
    def numero_4(self):
        print("Número 4")
        self.contents.set(self.contents.get()+str(4))
    def numero_5(self):
        print("Número 5")
        self.contents.set(self.contents.get()+str(5))
    def numero_6(self):
        print("Número 6")
        self.contents.set(self.contents.get()+str(6))
    def numero_7(self):
        print("Número 7")
        self.contents.set(self.contents.get()+str(7))
    def numero_8(self):
        print("Número 8")
        self.contents.set(self.contents.get()+str(8))
    def numero_9(self):
        print("Número 9")
        self.contents.set(self.contents.get()+str(9))
    
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title("CALCULADORA")
app = Application(master=root)

app.mainloop()
