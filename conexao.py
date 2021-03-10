from mysql.connector import connect, Error

def connection():
  try:
    db_connection = connect(
      host='db4free.net',
      user='visie_user',
      password='visie_pass',
      database='visie_db'
    )
    return db_connection
  except Error as error:
    print(error.message)
  else:
    db_connection.close()

def select():
  with connection() as connect:
    with connect.cursor(buffered=True) as cursor:
      cursor.execute("SELECT nome, data_admissao, id_pessoa FROM pessoas")
    return cursor.fetchall()

def salvar(val):
  print(val)
  with connection() as connect:
    with connect.cursor() as cursor:
      cursor.execute(f"INSERT INTO pessoas (nome, rg, cpf, data_nascimento, data_admissao, funcao) VALUES ('{val['nome']}','{val['rg']}','{val['cpf']}','{val['data_nasc']}','{val['data']}', '{val['funcao']}')")
    connect.commit()
  
def deletar(id):
  with connection() as connect:
    with connect.cursor() as cursor:
      cursor.execute(f'DELETE FROM pessoas WHERE id_pessoa= "{id}"')
    connect.commit()
