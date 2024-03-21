import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()

    # Métodos de Clase
    # Método para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de Texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()