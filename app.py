import tkinter as tk
from models import email as mdEmail
from views import email_frame as frEmail
from controllers import email as ctrEmail

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title('Sistema')
    self.geometry('400x150')
    self.resizable(0,0)

    email_model = mdEmail.Model('user@domain.type')
    email_view = frEmail.View(self)
    email_view.grid(row=0, column=0, padx=10, pady=10)
    email_controller = ctrEmail.Controller(email_model, email_view)
    email_view.set_controller(email_controller)


if __name__ == '__main__':
  app = App()
  app.mainloop()