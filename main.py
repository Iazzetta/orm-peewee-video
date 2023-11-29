from database import db, Usuario, Anuncio

# conectar no banco de dados
db.connect()

# criar tabelas no banco ou usar existentes
db.create_tables([Usuario, Anuncio])


# inserir um usuário
usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="123456")
print("\n@ Novo usuario: ", usuario.id, usuario.nome, usuario.email)

# inserir mais 3 usuários
Usuario.create(nome="Guilherme", email="gui@teste.com", senha="123456")
Usuario.create(nome="Joao", email="joao@teste.com", senha="123456")
Usuario.create(nome="Maria", email="maria@teste.com", senha="123456")

# listar usuarios
lista_usuarios = Usuario.select()
print("\n@ Listando usuários cadastrados:")
for u in lista_usuarios:
    print("-", u.id, u.nome, u.email)
    
# obter um usuario pelo id
usuario1 = Usuario.get(Usuario.id == 1)
print("\n@ Obter id 1: ", usuario1.nome)
    
# obter um usuario pelo email
joao = Usuario.get(Usuario.email == "joao@teste.com")
print("\n@ Obter joao: ", joao.nome)

# alterar nome da maria
maria = Usuario.get(Usuario.email == "maria@teste.com")
maria.nome = "Maria Python"
maria.save()
print("\n@ Maria atualizada: ", maria.nome)

# impedir de criar um usuário com o mesmo email
print("\n@ Tentando criar usuário com e-mail existente")
try:
    usuario_duplicado = Usuario.create(nome="ProgramadorPython2", email="teste@teste.com", senha="123456")
except:
    print("Não foi possivel criar o usuário pois o e-mail ja existe!")
    

# deletando um usuário
print("\n@ Deletando um usuário")
programador_python = Usuario.get(Usuario.email == "teste@teste.com")
programador_python.delete_instance()

try:
    usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
    print("Usuario encontrado: ", usuario_deletado.nome)
except:
    print("Usuário foi deletado!")
    
    
# criando um anuncio
maria = Usuario.get(Usuario.email == "maria@teste.com")
anuncio = Anuncio.create(
    usuario = maria,
    titulo = "Video de Banco de Dados",
    descricao = "O projeto seria criar um video sobre banco de dados e ORM com Python",
    valor = 500.99
)
print(f"\n@ Novo freela: [R$ {anuncio.valor}] {anuncio.titulo}")

# criando varios anuncios de um usuario
Anuncio.create(usuario = maria, titulo = "Anuncio 1", descricao = "Deixa o like", valor = 1000)
Anuncio.create(usuario = maria, titulo = "Anuncio 2", descricao = "Faça um comentário", valor = 5000)
Anuncio.create(usuario = maria, titulo = "Anuncio 3", descricao = "Se inscreva", valor = 10000)

# listando os anuncios de um usuario
print("\n@ Anuncios da Maria!")
anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@teste.com")
for a in anuncios_maria:
    print("-", a.id, a.titulo, a.descricao, a.valor)
    
# deletando todos os registros de uma tabela anuncios
Anuncio.delete().execute()
print("\n@ Anuncios deletados! Quantidade atual: ", Anuncio.select().count())