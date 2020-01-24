import mysql.connector

# Cria Conexão com o Banco de Dados
connection = mysql.connector.connect(host="#", user="#",password="#",database="#", charset="utf8")
# Cria o Cursos de retorno em modo dicionraio
cursor = connection.cursor(dictionary=True)
