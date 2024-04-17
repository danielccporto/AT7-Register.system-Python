nomes = []
sobrenomes = []
datas = []
cpfs = []
IDs = []
indice1=0
indice2=0
listaopcoes = [1,2,3,4,5,6]

nome = ""
nome1= ""
nome2= ""
sobrenome = ""
data = ""
CP = 0
cadastro = 0
cadastro_2 = 0



print("1.Inserir novo cadastro:")
print("2.Alterar CPF: ")
print("3.Trocar Sobrenomes: ")
print("4.Remover cadastro: ")
print("5. Listar todos os cadastros.")
print("6. Encerrar")


opcao = int(input("Insira o número da sua escolha: "))

while opcao in listaopcoes:
  
  if opcao == 1 :
    cadastro = int(input("Digite seu ID: "))
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    data = input("Digite sua data de nascimento: ")
    CP = input("Digite seu CPF: ")
     
    if cadastro in IDs: 
      IDs.insert(int(cadastro), cadastro)
      nomes.insert(int(cadastro), nome)
      sobrenomes.insert(int(cadastro), sobrenome)
      cpfs.insert(int(cadastro), CP)
      datas.insert(int(cadastro), data)
                   
      print("O novo cadastro foi inserido. ")
                  
    else: 
      nomes.append(nome)
      sobrenomes.append(sobrenome)
      IDs.append(cadastro)
      datas.append(data)
      cpfs.append(CP)
      
      print("Cadastro realizado com sucesso!")

  elif opcao == 2 : 
    cadastro = int(input("Digite o ID do registro a ser alterado: "))
    CP = input("Digite o novo CPF: ")
    
    if cadastro in IDs :
      del cpfs[int(cadastro -1)]
      cpfs.insert((cadastro -1), CP)
      print("O CPF foi alterado com sucesso!")
      
    else: 
      print("O CPF não existe.")
      
  elif opcao == 3 : 
    
    cadastro = int(input("Digite o ID do registro a ser alterado: "))
    
    
    if cadastro in IDs:
      
      cadastro_2 = input("Digite o 2o ID de registro a ser alterado: ")
      
      nome1 = sobrenomes[cadastro -1]
      nome2 = sobrenomes[int(cadastro_2) -1]
      print(f"nome1: {nome1}, nome2 : {nome2}")
      sobrenomes[cadastro -1] = nome2
      sobrenomes[int(cadastro_2) -1] = nome1

      print(f"sobrenome1: {sobrenomes[int(cadastro -1)]} e sobrenome 2 : {sobrenomes[int(cadastro_2) -1]}")

      
    else:
      print(f"O sobrenome não existe!")

  elif opcao == 4  : 
    
    cadastro = int(input("Digite o ID do registro a ser alterado: "))

    if cadastro in IDs :
      print(f"O cadastro de {nomes[int(cadastro -1)]}  {sobrenomes[int(cadastro -1)]}, de ID {IDs[int(cadastro -1)]} será removido.")
      
      del nomes[int(cadastro -1)]
      del sobrenomes[int(cadastro -1)]
      del datas[int(cadastro -1)]
      del cpfs[int(cadastro -1)]
      del IDs[int(cadastro -1)]
      print(f"O ID {cadastro} foi removido!")
      
      
    else: 
      print(f"O ID {cadastro} não existe.")
      
  elif opcao == 5:
    for i in range(len(IDs)):
      print(f"ID : {IDs[int(i)]}, Nome : {nomes[int(i)]}, CPF : {cpfs[int(i)]}, Data de nascimento : {datas[int(i)]}")

  
  elif opcao == 6 :
    print("O programma está encerrado")
    break

  
  
  print("1.Inserir novo cadastro:")
  print("2.Alterar CPF: ")
  print("3.Trocar Sobrenomes: ")
  print("4.Remover cadastro: ")
  print("5. Listar todos os cadastros.")
  print("6. Encerrar")
  opcao = int(input("Escolha uma opção: "))
      
      
    
    
      




      
      
    
      
      
      
      
      
      
    

