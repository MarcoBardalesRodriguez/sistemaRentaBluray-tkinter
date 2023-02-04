import sqlite3

class Usuario:
  """
  Objeto usuario que recive los valores para cada usuario
  y retorna una sentencia insert sql en su metodo .query
  """
  def __init__(self, id, nombre, apellido):
    self.id = id
    self.nombre = nombre
    self.apellido = apellido

  
  def query(self):
    self.query = f" INSERT INTO usuarios Values({self.id}, '{self.nombre}', '{self.apellido}')"
    return self.query
  
  
  def values(self):
    self.values = (self.id, self.nombre, self.apellido)
    return self.values


  def insertar(self):
    cursor.execute(self.query)
  
  
  def actualizar(self, new_nombre, new_apellido):
    #llama a __init__ para que se reasignen los valores de atributos del objeto
    self.__init__(self.id, new_nombre, new_apellido)
    #se actualiza usando los nuevos valores
    cursor.execute("UPDATE usuarios SET nombre=?, apellido=? WHERE id=?",(self.nombre, self.apellido, self.id))
  
  
  def eliminar(self):
    cursor.execute("DELETE from usuarios WHERE id=?",(self.id))

    

#Crea la conexion
conn = sqlite3.connect('db_test.db')

#Crea un cursor para consultas
cursor = conn.cursor()

#DDL
cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios(
  id INTEGER PRIMARY KEY,
  nombre VARCHAR(25) NOT NULL,
  apellido VARCHAR(50) NOT NULL) """)

#DML
# cursor.execute(" INSERT INTO usuarios VALUES(1, 'Marco', 'Bardales Rodriguez')")
user_1 = Usuario(1, 'Marco', 'Bardales Rodriguez')
# cursor.execute(" INSERT INTO usuarios VALUES(2, 'Adrian', 'Llauce Santisteban')")
user_2 = Usuario(2, 'Adrian', 'Llauce Santisteban')

user_3 = Usuario(3, 'Julia', 'Sosa Ulloque')
user_4 = Usuario(4, 'Marleny', 'De la Cruz de la Cruz')

# cursor.execute(user_n.query())

lista_usuarios = [(user_1.values()), # definicion de tuplas de solo un valor -> (value,)
                          (user_2.values()), 
                          (user_3.values()), 
                          (user_4.values())] 

# print(lista_usuarios) 
# [(1, 'Marco', 'Bardales Rodriguez'), (2, 'Adrian', 'Llauce Santisteban'), (3, 'Julia', 'Sosa Ulloque'), (4, 'Marleny', 'De la Cruz de la Cruz')]

#ejecuta una sentencia usando como parametros una lista
# cursor.executemany(" INSERT INTO usuarios VALUES(?, ?, ?)",lista_usuarios)

#Actualizar un registro
# user_1.actualizar('Antonio', 'Bardales Rodriguez')



#Almacena los datos insertados
conn.commit()

cursor.execute("SELECT * FROM usuarios")
# cursor.execute("SELECT * FROM usuarios WHERE nombre=?", ('Marco',))

# fetch -> los registros que toma se limpian del cache del cursor

#retorna el primer dato almacenado en el cursor (<- SELECT)
primer_usuario = cursor.fetchone()
print(primer_usuario) #registro 1
  
#retorna x numero de datos almacenados en el cursor (<- SELECT)
usuarios = cursor.fetchmany(2)
print(usuarios) #registro 2 y 3 / el registro 1 ya fue tomado
  
#retorna todos los datos almacenados en el cursor (<- SELECT)
usuarios = cursor.fetchall()
print(usuarios) #registro 4 - n / los registros anteriores ya fueron tomados

#Cierra la conexion
conn.close()
