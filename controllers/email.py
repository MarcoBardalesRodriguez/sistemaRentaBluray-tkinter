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