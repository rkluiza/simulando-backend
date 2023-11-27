from peewee import *

mysql_db = MySQLDatabase('simulando', user='root', password='ienh', host='localhost', port=3306)

class BaseModel(Model):
    class Meta:
        database = mysql_db

class Materia(BaseModel):
    nome = CharField()

    class Meta:
        table_name = 'materia'
        database = mysql_db

class Usuario(BaseModel):
    nome = CharField()
    email = CharField()
    senha = CharField()

    #produtos = ManyToManyField(Produto, backref='categorias')
    class Meta:
        table_name = 'usuario'
        database = mysql_db

class Questao(BaseModel):
    enunciado = CharField()
    alternativa1 = CharField()
    alternativa2 = CharField()
    alternativa3 = CharField()
    alternativa4 = CharField()
    correta = CharField()
    img = BlobField()
    materia = ForeignKeyField(Materia, backref='questoes')

    class Meta:
        table_name = 'questao'
        database = mysql_db

class Resposta(BaseModel):
    questao = ForeignKeyField(Questao, backref='respostas')
    hora = TimeField()
    data = DateField()
    acerto = BooleanField()
    materia = ForeignKeyField(Materia, backref='respostas')
    retorno_usuario = BlobField()

    class Meta:
        table_name = 'resposta'
        database = mysql_db

class quiz(BaseModel):
    usuario = ForeignKeyField(Usuario, backref='quizs')
    questao = ForeignKeyField(Questao, backref='questoes')
    hit = IntegerField()
    tempo = TimeField()

    class Meta:
        table_name = 'quiz'
        database = mysql_db