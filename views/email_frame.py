import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
  def __init__(self, container):
    super().__init__(container)

    self.label = ttk.Label(self, text='Email: ')
    self.label.grid(row=1, column=0)

    self.email_var = tk.StringVar()
    self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
    self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

    self.save_button = ttk.Button(self, text='Guardar', command=self.save_email)
    self.save_button.grid(row=1, column=2, sticky=tk.W)

    self.message_label = ttk.Label(self, text='', foreground='red')
    self.message_label.grid(row=2, column=1, sticky=tk.W)

    self.controller = None

    
  def set_controller(self, extern_controller):
    self.controller = extern_controller
    
    
  def save_email(self):
    #si existe un controlador 
    #envia el email recivido en el entry 
    #al metodo guardar del controlador
    if self.controller:
      self.controller.save(self.email_var.get())

    
  def show_error(self,message):
    self.message_label['text'] = message
    self.message_label['foreground'] = 'red'
    #after -> recive un tiempo y un comando(metodo) a ejecutar
    self.message_label.after(3000, self.hide_message)
    self.email_entry['foreground'] = 'red'
  
  
  def show_success(self, message):
    self.message_label['text'] = message
    self.message_label['foreground'] = 'green'
    #after -> recive un tiempo y un comando(metodo) a ejecutar
    self.message_label.after(3000, self.hide_message)
    self.email_entry['foreground'] = 'black'
    #limpiamos la variable que recive el texto del entry
    self.email_var.set('')

  
  def  hide_message(self):
    self.message_label['text'] = ''