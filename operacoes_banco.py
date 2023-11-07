import mysql.connector

# Conexão com o banco de dados
def obterConexao():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="simulando"
    )
    return conexao

#Obtém todos os cursos disponíveis
def obterUsuariosExistentes():
    conexao = obterConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

print(obterUsuariosExistentes())