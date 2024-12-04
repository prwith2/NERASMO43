import pyodbc


try:
    conexao = pyodbc.connect("DRIVER={SQL server}; SERVER='+VITOR+';DATABASE='+petshop+';UID='+sa+';PWD='+123456HAS")
    consulta = conexao.cursor()
    verificado = True
except:
    verificado = False

def cadastrarPets():
    nome = input("Digite o nome do bicho")
    tipo = input("Digite o tipo do bicho")
    idade = int(input("Digite a idade "))

    query = f"INSERT INTO petshop(nome, tipo, idade) VALUES('{nome}','{tipo}', {idade})"
    consulta.execute(query)
    consulta.commit()

def mostrarPets():
    print(consulta.execute("SELECT * FROM petshop"))

def editarPets():
    idPet = int(input("Digite o id do seu pet: "))
    if consulta.execute(f"SELECT * FROM petshop where id = {idPet}") == True:
        nome = input("Digite o novo nome: ")
        idade = int(input("Digite uma nova idade: "))
        tipo = input("Digite o novo tipo: ")
        query = f"UPDATE petshop SET nome = '{nome}', idade = {idade}, tipo = '{tipo}'"

        consulta.execute(query)
        consulta.commit()
    else:
        print("Vai se fuder seu merda")

def excluirPets():
    idPet = int(input("Digite o id do pet: "))
    if consulta.execute(f"SELECT * FROM petshop where id = {idPet}") == True:
        query = f"DELETE petshop where id = {idPet}"
        consulta.execute(query)
        consulta.commit()
    else:
        print("vai se fuder ")


while verificado:
    print("""
        coloca aqui as opção
    """)
    escolha = int(input("Digite a escolha: "))
    match escolha:
        case 1:
            cadastrarPets()
        case 2:
            mostrarPets()
        case 3:
            editarPets()
        case 4:
            excluirPets()
        case _:
            print("vai se fuder")
        case 0:
            verificado = False