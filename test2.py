import tkinter as tk
from tkinter import ttk
# from models import email as mdEmail
# from views import email_frame as frEmail
# from controllers import email as ctrEmail
import re

class Model:
  def __init__(self, email):
    self.email = email
    
  # property -> getter
  @property
  def email(self):
    #retorna un atributo privado
    return self._email
  
  
  #property -> setter
  @email.setter
  def email(self, new_email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(pattern, new_email):
      #setter -> permite actualizar un atributo privado
      self._email = new_email
    else:
      raise ValueError(f'El email {new_email} es invalido')


  #almacenamos el nuevo valor recivido en el setter
  def save(self):
    with open('db_emails.txt', 'a') as db_emails:
      db_emails.write(self.email + '\n')







class View(ttk.Frame):
  def __init__(self, container):
    super().__init__(container)

    self.label = ttk.Label(self, text='Email: ')
    self.label.grid(row=1, column=0)

    self.email_var = tk.StringVar()
    self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
    self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

    # self.save_button = ttk.Button(self, text='Guardar', command=self.save_button_email)
    # self.save_button.grid(row=1, column=1, sticky=tk.W)

    self.message_label = ttk.Label(self, text='', foreground='red')
    self.message_label.grid(row=2, column=1, sticky=tk.W)

    self.controller = None

    
    def set_controller(self, extern_controller):
      self.controller = extern_controller
      
      
    def save_button_email(self):
      #si existe un controlador 
      if self.controller:
      #envia el email recivido en el entry 
      #al metodo guardar del controlador
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









class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view

  
  def save(self, email):
    try:
      #envia el email al modelo
      self.model.email = email
      self.model.save()
      self.view.show_success(f'El email {email} fue guardado')
      
    #recibe ValueError desde el email.setter del modelo  
    except ValueError as error_message:
      self.view.show_error(error_message)







class App(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title('Sistema')
    # self.geometry('')

    email_model = Model('user@domain.type')
    email_view = View(self)
    email_view.grid(row=0, column=0, padx=10, pady=10)
    email_controller = Controller(email_model, email_view)
    email_view.set_controller(email_controller)


if __name__ == '__main__':
  app = App()
  app.mainloop()