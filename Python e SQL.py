import oracledb
try:
  conn = oracledb.connect(user="XXX", password="XXX", dsn="XXX:1521/orcl")
except Exception as e:
  print("Erro:", e)
  #Conexao com o banco falhou
  #Flag para não executar a aplicacao
  conexao = False
else:
  #Flag para executar a aplicacao
  conexao = True

while conexao:
  #Apresentando o menu
  print("------ ALUNO -------")
  print("""
  1-Recuperar todos os alunos
  2-Listar o aluno pelo id
  3-Cadastrar um aluno
  4-Alterar um aluno
  5-Excluir um aluno
  6-Excluir todos os alunos
  7-Salvar em um arquivo CSV
  8-SAIR
  """)
  #Capturar a escolha do usuario
  escolha = input("Escolha ->")
  #Verificar se é um valor numerico
  if escolha.isdigit():
    escolha = int(escolha)
  else:
    print("Digite um numero.\nReinicie a Aplicacao")
    escolha = 8 #alterando a escolha para 8 que é o sair

  if escolha == 1:
    #recuperar dados da tabela T_PY_ALUNO COM CURSOR
    with conn.cursor () as c_consulta:
      cons = "select * from T_PY_ALUNO"
      print('Recuperando todos os alunos da tabela')
      c_consulta.execute(cons)
      #Esta linha recupera todos os resultados da consulta SQL e os armazena na lista alunos:
      alunos=list(c_consulta.fetchall())
      if len(alunos) == 0:
        print('Não há alunos na tabela')
      else:  
        print(alunos)

  if escolha == 2:
    with conn.cursor() as c_consulta:
      id_aluno = int(input("Qual o número do ID do aluno que gostaria de recuperar? "))
      print(f'Recuperando o ID {id_aluno} do aluno da tabela')
      c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id_aluno}")
      aluno = list(c_consulta.fetchone())
      if len(aluno) == 0:
        print('Não há alunos na tabela')
      else:  
        print(aluno)

  if escolha == 3:
    print("\nCadastrar um aluno")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    endereco = input("Digite o endereço do aluno: ")
    curso = input("Digite o curso do aluno: ")
    with conn.cursor() as c_insert:
        c_insert.execute(f"INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES ('{nome}', {idade}, '{endereco}', '{curso}')")
        conn.commit()
        print("Aluno cadastrado com sucesso!")
    aluno=[]
    with conn.cursor() as c_consulta:
       cons=f"SELECT * FROM T_PY_ALUNO WHERE nome = '{nome}'"
       c_consulta.execute(cons)
       aluno=list(c_consulta.fetchall())
       if len(aluno) == 0:
          print('Não há alunos na tabela')
       else:  
          print(aluno)

  if escolha == 4:
    print("\nAlterar um aluno")
    aluno = []
    id = int(input("Qual o número do ID do aluno que gostaria de alterar? "))
    with conn.cursor() as c_consulta: 
      c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id}")
      aluno=list(c_consulta.fetchall())
      if len(aluno) == 0:
        print(f'Nao há dados deste aluno de id:{id}')
      else:  
        print(aluno)
        print('Dados a serem alterados')
        #solicita dados dos alunos
        nome=input("Entre com o nome: ")
        idade=int(input("Entre com a idade: "))
        endereco=input("Entre com o endereco: ")
        curso=input("Entre com o curso: ")
        #monta o comando de insercao
        cmd = f"UPDATE T_PY_ALUNO SET nome = '{nome}', idade = {idade}, endereco = '{endereco}', curso='{curso}' WHERE id = {id} "
        with conn.cursor() as c_update:
          c_update.execute(cmd)
        conn.commit()
        aluno=[]
        with conn.cursor() as c_consulta:
          cons=f"select * from T_PY_ALUNO where nome = '{nome}'"
          c_consulta.execute(cons)
          aluno = list(c_consulta.fetchall())
          if len(aluno) == 0:
            print('Aluno não se encontra na base')
          else:  
            print(aluno)

  if escolha == 5:
    print("\nExcluindo um aluno")
    aluno = []
    id = int(input("Qual o número do ID do aluno que gostaria de excluir? "))
    with conn.cursor() as c_consulta: 
      c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id}")
      aluno=list(c_consulta.fetchall())
      if len(aluno) == 0:
        print(f'Nao ha dados deste aluno de id:{id}')
      else:  
        print(aluno)
        with conn.cursor() as c_delete:
          cmd="DELETE T_PY_ALUNO WHERE id = :1"
          c_delete.execute(cmd,(id,))
          print("aluno excluido com sucesso")
        conn.commit()

  if escolha == 6:
    print("\nExcluindo TODOS os alunos")
    cmd="DELETE FROM T_PY_ALUNO"
    with conn.cursor() as c_delete:
      c_delete.execute(cmd)
      print("Alunos excluídos com sucesso")
    conn.commit()

  if escolha == 7:
    import csv

    with open('alunos.csv', 'r', encoding='UTF-8') as arqAluno:
        csvAluno = csv.reader(arqAluno, delimiter=';')
        listaAlunos=list(csvAluno)
        print(listaAlunos)

        print('\n\nLinhas da Lista')
        print(listaAlunos[1:])
        for linha in listaAlunos[1:]:
            print(linha)
            with conn.cursor() as c_insert:
                c_insert.execute("INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES (:1, :2, :3, :4)", (linha[0], linha[1], linha[2], linha[3]))
            conn.commit()
            print("Aluno cadastrado com sucesso.")
  
  if escolha == 8:
    conexao = False
    conn.close()
    print('Conexão encerrada')