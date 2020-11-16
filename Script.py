import hashlib
import sqlite3

def novoLogin (loginfinal, senhafinal):
    try:
        conn = sqlite3.connect('Navio.db') 
        cursor = conn.cursor()
        cursor.execute("INSERT INTO login (usuario,senha) VALUES ('" + loginfinal + "', '" + senhafinal + "');")
        conn.commit() 
        conn.close()
    except:
        print("Erro ao conectar ao banco de dados")

def loginfunc(loginfinal, senhafinal):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("SELECT usuario,senha FROM login WHERE usuario = '" + loginfinal + "' AND senha = '" + senhafinal + "';")
        resultado = cursor.fetchall()
        if resultado:
            print("Login realizado com sucesso!")
            q = 0
            while q == 0:
                print("")
                print("================================SUBSTÂNCIAS=================================")
                print("       VS para ver as Substâncias")
                print("       CS para cadastrar uma nova substância")
                print("       AVS para Atualizar Valores")
                print("       DS para Deletar uma Substância")
                print("=================================TRIPULAÇÃO=================================")
                print("       VT para ver a Tripulação") 
                print("       CT para criar uma Tripulação")
                print("       AVT para Atualizar Valores de Tripulação")
                print("       DT para Deletar um Valor de Tripulação")
                print("============================================================================")
                po = input("Digite a letra desejada ou aperte Control C para Fechar: ")

# =========================== CHAMADO DAS FUNÇÕES =============================

# ================================ SUBSTÂNCIAS ================================

                if po.upper == "VS":
                    verSubs()
                
                if po.upper == "CS":
                    print("Insira os Novos Dados:")
                    nomeSub = input("Substância: ")
                    pesoSub = input("Quantidade (em Toneladas): ")
                    cadSubs(nomeSub,pesoSub)

                if po.upper == "AVS":
                    print("Insira os Novos Dados:")
                    nomeSub = input("Substância: ")
                    pesoSub = input("Quantidade (em Toneladas): ")
                    attValSubs(nomeSub,pesoSub)

                if po.upper == "DS":
                    nomeSub = input("Substância: ")
                    delSubs(nomeSub)

# ================================ TRIPULAÇÃO ================================

                if po.upper == "VT":
                    verTrip()
                
                if po.upper == "CT":
                    print("Insira os Novos Dados:")
                    profissao = input("Profissão: ")
                    nomeT = input("Nome: ")
                    idade = input("Idade: ")
                    rg = input("RG: ")
                    dataNasc = input("Data de Nascimento: ")
                    sexo = input("Sexo: ")
                    altura = input("Altura: ")
                    pesoT = input("Peso: ")
                    tipoSang = input("Tipo Sanguíneo: ")
                    cadTrip(profissao,nomeT,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang)

                if po.upper == "AVT":
                    print("Insira os Novos Dados:")
                    profissao = input("Profissão: ")
                    idade = input("Idade: ")
                    rg = input("RG: ")
                    dataNasc = input("Data de Nascimento: ")
                    sexo = input("Sexo: ")
                    altura = input("Altura: ")
                    pesoT = input("Peso: ")
                    tipoSang = input("Tipo Sanguíneo: ")
                    attValTrip(profissao,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang)

                if po.upper == "DT":
                    nomeT = input("Nome: ")
                    delTrip(nomeT)

                if po.upper == "F":
                    q = 1
                    break
                
                f = input("Digite V para Voltar ao Menu Principal ou aperte Control C para Fechar o Sistema: ")

                if f.upper == "V":
                    q = 0

        else:
            print("Erro: Conta não encontrada. Verifique Maiúsculas e/ou Caracteres Especiais.")
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")

# ================================ FUNÇÕES ================================

def verSubs():
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM substancias;')
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")

def verTrip():
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tripulacao;')
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")

def cadSubs(nomeSub,pesoSub):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO substancias (nomeSub,pesoSub) VALUES ('" + nomeSub + "', '" + pesoSub + "');")
        conn.commit()
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")

def cadTrip(profissao,nomeT,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tripulacao (profissao,nomeT,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang) VALUES ('" + profissao + "', '" + nomeT + "', '" + idade + "', '" + rg + "', '" + dataNasc + "', '" + sexo + "', '" + altura + "', '" + pesoT + "', '" + tipoSang + "');")
        conn.commit()
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")
    
def attValSubs(nomeSub,pesoSub):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE substancias SET pesoSub = '" + pesoSub + "' WHERE nome = '" + nomeSub + "';")
        conn.commit()
        cursor.execute("SELECT nomeSub,pesoSub FROM substancias WHERE nomeSub = '" + nomeSub + "' AND pesoSub = '" + pesoSub + "';")
        resultado = cursor.fetchall()

        if resultado:
            print("Atualizado com sucesso!")
        else:
            print("Erro: Verifique Maiúsculas e Caracteres Especiais")
        conn.close()
    except:
        print("Erro: Não foi possível conectar ao banco de dados")
        
def attValTrip(profissao,nomeT,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE substancias SET profissao = '" + profissao + "' AND idade ='" + idade + "' AND rg ='" + rg + "' AND dataNasc ='" + dataNasc + "' AND sexo ='" + sexo + "' AND altura='" + altura + "' AND pesoT ='" + pesoT + "' tipoSang = '" + tipoSang + "' WHERE nome = '" + nomeT + "' ;")
        conn.commit()
        cursor.execute("SELECT profissao,nomeT,idade,rg,dataNasc,sexo,altura,pesoT,tipoSang FROM tripulacao WHERE profissao = '" + profissao + "' AND nomeT = '" + nomeT + "' AND idade ='" + idade + "' AND rg ='" + rg + "' AND dataNasc ='" + dataNasc + "' AND sexo ='" + sexo + "' AND altura='" + altura + "' AND pesoT ='" + pesoT + "' tipoSang = '" + tipoSang + "' ;")
        resultado = conn.fetchall()

        if resultado:
            print("Atualizado com sucesso!")
        else:
            print("Erro: Verifique Maiúsculas e Caracteres Especiais")
        conn.close()

    except:
        print("Erro: Não foi possível conectar ao banco de dados")

def delSubs(nomeSub):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM substancias WHERE nomeSub = '" + nomeSub + "' ;")
        conn.commit()
        resultado = cursor.fetchall()

        if resultado:
            print("Deletado com sucesso!")
        else:
            print("Erro: Verifique Maiúsculas e Caracteres Especiais")
        conn.close()
        
    except:
        print("Erro: Não foi possível conectar ao banco de dados")

def delTrip(nomeT):
    try:
        conn = sqlite3.connect('Navio.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tripulacao WHERE nomeT = '" + nomeT + "' ;")
        conn.commit()
        resultado = cursor.fetchall()

        if resultado:
            print("Deletado com sucesso!")
        else:
            print("Erro: Verifique Maiúsculas e Caracteres Especiais")
        conn.close()
        
    except:
        print("Erro: Não foi possível conectar ao banco de dados")


# ================================ CRIPTOGRAFIA ================================

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
        novoLogin(loginfinal, senhafinal)   #chamando funcao para criar o login
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

