import tkinter as tk
from math import sqrt
class Application(tk.Frame):
    numeroUno = None
    numeroDos = None
    sumaEstado = False
    restaEstado = False
    multiplicacionEstado = False
    divisionEstado = False
    cuadradoEstado = False
    raizEstado = False
    #self.array = []
    #self.sumaEstado = False
    
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
        self.Bdivision= tk.Button(self, text = "/", fg = "gray", command = self.division)
        self.Bdivision.grid(row=1, column=4)
        self.Bb= tk.Button(self, text = "←", fg = "gray", command = self.borrarAnterior)
        self.Bb.grid(row=1, column=5)
        self.Bdel= tk.Button(self, text = "c", fg = "gray", command = self.borrar)
        self.Bdel.grid(row=1, column=6)
        
        self.B4= tk.Button(self, text = "4", fg = "gray", command = self.numero_4)
        self.B4.grid(row=2, column=1)
        self.B5= tk.Button(self, text = "5", fg = "gray", command = self.numero_5)
        self.B5.grid(row=2, column=2)
        self.B6= tk.Button(self, text = "6", fg = "gray",command = self.numero_6)
        self.B6.grid(row=2, column=3)
        self.Bx= tk.Button(self, text = "x", fg = "gray", command = self.multiplicacion)
        self.Bx.grid(row=2, column=4)
        self.Bx= tk.Button(self, text = "(", fg = "gray", command = self.parentesisA)
        self.Bx.grid(row=2, column=5)
        self.Bx= tk.Button(self, text = ")", fg = "gray", command = self.parentesisC)
        self.Bx.grid(row=2, column=6)

        self.B7= tk.Button(self, text = "7", fg = "gray", command = self.numero_7)
        self.B7.grid(row=3, column=1)
        self.B8= tk.Button(self, text = "8", fg = "gray", command = self.numero_8)
        self.B8.grid(row=3, column=2)
        self.B9= tk.Button(self, text = "9", fg = "gray",command = self.numero_9)
        self.B9.grid(row=3, column=3) 
        self.Bm= tk.Button(self, text = "-", fg = "gray",command = self.resta)
        self.Bm.grid(row=3, column=4)
        self.Bex= tk.Button(self, text = "x²", fg = "gray",command = self.cuadrado)
        self.Bex.grid(row=3, column=5) 
        self.Bra= tk.Button(self, text = "√x", fg = "gray",command = self.raiz)
        self.Bra.grid(row=3, column=6)

        self.B0= tk.Button(self, text = "0", fg = "gray",command = self.numero_0)
        self.B0.grid(row=4, column=1)
        self.Bp= tk.Button(self, text = ".", fg = "gray",command = self.punto)
        self.Bp.grid(row=4, column=2)
        self.Bporcentaje= tk.Button(self, text = "%", fg = "gray", command = self.procentaje)
        self.Bporcentaje.grid(row=4, column=3)
        self.BM= tk.Button(self, text = "+", fg = "gray", command = self.suma)
        self.BM.grid(row=4, column=4)
        self.Be= tk.Button(self, text = "=", fg = "gray", command = self.igual)
        self.Be.grid(row=4, column=5, columnspan = 2)


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
    def numero_0(self):
        print("Número 0")
        self.contents.set(self.contents.get()+str(0))
    def suma(self):
        self.sumaEstado = True
        self.numeroUno = float(self.contents.get())
        print("+")
        self.contents.set(self.contents.get()+ "+")
    def resta(self):
        self.restaEstado = True
        self.numeroUno = float(self.contents.get())
        print("-")
        self.contents.set(self.contents.get()+ "-")
    def multiplicacion(self):
        print("x")
        self.multiplicacionEstado = True
        self.numeroUno = float(self.contents.get())
        self.contents.set(self.contents.get()+"x")
    def division(self):
        print("/")
        self.divisionEstado = True
        self.numeroUno = float(self.contents.get())
        self.contents.set(self.contents.get()+"/")
    def borrar(self):
        self.sumaEstado = False
        self.restaEstado = False
        self.multiplicacionEstado = False
        self.divisionEstado = False
        self.cuadradoEstado = False
        self.raiz = False
        print("BORAR")
        self.contents.set("")
    def borrarAnterior(self):
        print("Borrar anterior")
    def procentaje(self):
        print("porcentaje")
        self.contents.set(self.contents.get()+"%")
    def punto(self):
        print("punto")
        self.contents.set(self.contents.get()+".")
    def parentesisA(self):
        print("(")
        self.contents.set(self.contents.get()+"(")
    def parentesisC(self):
        print(")")
        self.contents.set(self.contents.get()+")")
    def raiz(self):
        self.raizEstado = True
        
        print("Raiz")
        self.contents.set(self.contents.get()+"√")
    def cuadrado(self):
        self.cuadradoEstado = True
        self.numeroUno = float(self.contents.get())
        print("Cuadrado")
        self.contents.set(self.contents.get()+"²")
    def igual(self):
        if(self.sumaEstado):
            try:
                self.numeroDos = float(self.contents.get()[self.contents.get().find("+"):])
                self.contents.set(self.contents.get()+"=" + str(self.numeroDos + self.numeroUno))
            except ValueError:
                self.contents.set("syntax error")
        elif(self.restaEstado):
            try:
                self.numeroDos = float(self.contents.get()[self.contents.get().find("-")+1:])
                self.contents.set(self.contents.get()+"=" + str(self.numeroUno - self.numeroDos))
            except ValueError:
                self.contents.set("syntax error")
        elif(self.multiplicacionEstado):
            try:
                self.numeroDos = float(self.contents.get()[self.contents.get().find("x")+1:])
                self.contents.set(self.contents.get()+"=" + str(self.numeroUno*self.numeroDos))
            except ValueError:
                self.contents.set("syntax error")
        elif(self.divisionEstado):
            try:
                self.numeroDos = float(self.contents.get()[self.contents.get().find("/")+1:])
                self.contents.set(self.contents.get()+"=" + str(self.numeroUno/self.numeroDos))
            except ValueError:
                self.contents.set("syntax error")
        elif(self.cuadradoEstado):
            try:
                self.contents.set(self.contents.get()+"=" + str(self.numeroUno**2))
            except ValueError:
                self.contents.set("syntax error")
        elif(self.raizEstado):
            try:
                self.numeroUno = float(self.contents.get()[1:])
                self.contents.set(self.contents.get()+"=" + str(sqrt(self.numeroUno)))
            except ValueError:
                self.contents.set("syntax error")
        print("Igual")
        #print(self.contents.get())

root = tk.Tk()
root.title("CALCULADORA")
app = Application(master=root)

app.mainloop()
