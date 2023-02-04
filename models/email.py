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