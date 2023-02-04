import tkinter as tk
from tkinter import ttk

class View(tk.Frame):
  def __init__(self, contenedor):
    super().__init__(contenedor)

    self.label = tk.Label(self, text='hola mundo')
    self.label.grid(row=1, column=0)


class View2(tk.Frame):
  def __init__(self, contenedor):
    super().__init__(contenedor)

    self.label = tk.Label(self, text='adios mundo')
    self.label.grid(row=1, column=0)

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title('App')

    view = View(self)
    view.grid(row=0, column=0, padx=10, pady=10)

    view2 = View2(self)
    view2.grid(row=1, column=0, padx=10, pady=10)


app = App()
app.mainloop()