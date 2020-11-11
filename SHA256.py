import hashlib
import sqlite3
#import getpass


def inserir(loginfinal, senhafinal):  # funcao para criar a conta
    try:
        conn = sqlite3.connect('banco.db') #abre o banco
        cursor = conn.cursor() #cria o cursor
        cursor.execute("INSERT INTO login (usuario,senha) VALUES ('" + loginfinal + "', '" + senhafinal + "');") # manda a linha de codigo para o banco
        conn.commit() #salva
        conn.close() #finaliza
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')
def loginfunc(loginfinal, senhafinal): # função de Login 
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT usuario,senha FROM login WHERE '
                       'usuario = "' + loginfinal + '" AND senha = "' + senhafinal + '";')
        resultado = cursor.fetchall()  # checar se deu certo
        if resultado:
            print("Login realizado com sucesso!")
            q = 0
            while q == 0:
                print("")
                print("=================================TRIPULAÇÃO=================================")
                print("Digite a letra desejada:")
                print("       VT para ver a Tripulação")
                print("       CT para criar uma Tripulação")
                print("       AVT para Atualizar Valores de Tripulação")
                print("       DT para Deletar um Valor de Tripulação")
                print("================================SUBSTÂNCIAS================================")
                print("       VS para ver as Substâncias")
                print("       CS para cadastrar uma nova substância")
                print("       AVS para Atualizar Valores")
                print("       DS para Deletar uma Substância")
                print("       F para Fechar")
                po = input("")

                if po.upper() == 'VS':
                    ler()

                if po.upper() == 'CS':
                    nome = input("Substancia: ")
                    qtd = input("Quantidade(número em toneladas): ")
                    qtd = qtd + " Toneladas"
                    cadastrarsub(nome, qtd)

                if po.upper() == 'AVS':
                    nnome = input("Nome da Substancia: ")
                    nqtd = input("Nova Quantidade: ")
                    nqtd = nqtd + " Toneladas"
                    att(nqtd, nnome)

                if po.upper() == 'DS':
                    dnome = input("Nome da substancia que deseja deletar: ")
                    delete(dnome)

                if po.upper() == 'F':
                    break

                f = input("V para retornar - F para fechar: ")
                if f.upper() == 'V':
                    q = 0
                if f.upper() == 'F':
                    q = 1

        else:
            print("ERRO - Conta não encontrada, Verifique Letras maiúsculas e/ou caracteres especiais.")
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')

def ler():
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('Select * FROM substancias;')
        print('')
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')

def cadastrarsub(nome, qtd):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO substancias (nome,qtd) VALUES ('" + nome + "', '" + qtd + "');")
        conn.commit()
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')

def att(nqtd, nnome):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE substancias SET qtd = "' + nqtd + '" WHERE nome = "' + nnome + '";')
        conn.commit()
        cursor.execute('SELECT nome,qtd FROM substancias WHERE '
                       'nome = "' + nnome + '" AND qtd = "' + nqtd + '";')
        resultado = cursor.fetchall()

        if resultado:
            print("Quantidade atualizada com sucesso!")
        else:
            print("ERRO - verifique se o nome da substancia foi digitado corretamente.")
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')
def delete(dnome):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM substancias WHERE nome = "' + dnome + '";')
        conn.commit()
        cursor.execute('SELECT nome FROM substancias WHERE '
                       'nome = "' + dnome + '";')
        resultado = cursor.fetchall()

        if resultado:
            print("Substancia deletada com sucesso!")
        else:
            print("Substancia nao encontrada.")
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')


def cadastrarTripulacao(profissao,nome,idade,rg,data_nasc,sex,alt,peso,tipoSanguineo):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tripulacao (profissao,nome,idade,rg,data_nasc,sex,alt,peso,tipoSanguineo) VALUES ('" + profissao + "', '" + nome + "', '" + idade + "', '" + rg + "', '" + data_nasc + "', '" + sex + "', '" + alt + "', '" + peso + "', '" + tipoSanguineo + "');")
        conn.commit()
        conn.close()
    except:
        print('ERRO - Não foi possível conectar ao banco de dados "banco.db".')
        


j = 0
while j == 0:

    op = input("Digite L para logar ou C para criar um login:\n") # ficar perguntando ate resposta aceita

    if op.upper() == 'C':
        login = input("Login: ") #pegar dados
        senha = input("Senha: ")

        enclogin = hashlib.sha256()  #funcao do hashlib
        encsenha = hashlib.sha256()

        enclogin.update(login.encode("utf-8"))  #mudando para utf-8
        encsenha.update(senha.encode("utf-8"))

        loginfinal = enclogin.hexdigest()  # traduzindo
        senhafinal = encsenha.hexdigest()
        inserir(loginfinal, senhafinal)   #chamando funcao para criar o login
        print("Login registrado com sucesso")
        j = 1 #quebra o loop
    if op.upper() == 'L':
        login = input("Login: ")  #mesma coisa em tudo
        senha = input("Senha: ")

        enclogin = hashlib.sha256()
        encsenha = hashlib.sha256()

        enclogin.update(login.encode("utf-8"))
        encsenha.update(senha.encode("utf-8"))

        loginfinal = enclogin.hexdigest()
        senhafinal = encsenha.hexdigest()
        loginfunc(loginfinal, senhafinal)
        j = 1





