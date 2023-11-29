from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

def login(email, senha):
    try:
        usuario = Usuario.get(Usuario.email == email)
        return usuario
    except:
        raise Exception("E-mail ou senha incorretos")
    
def cadastrar(nome, email, senha):
    try:
        novo_usuario = Usuario.create(nome=nome, email=email, senha=senha)
        return novo_usuario
    except:
        raise Exception("E-mail já cadastrado")
    


    