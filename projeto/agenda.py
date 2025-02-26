def adicionar_contato():
  nome = input("Digiter o nome do contato: ")
  telefone = input("Digite o telefone: ")
  email = input("Digite o email: ")
  favorito = False # por padrão, não é favorito
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
  contatos.append(contato)
  print("Contato adicionado com sucesso!")

def listar_contatos():
  if not contatos:
    print("Nenhum contato cadastrado.")
    return
  print("\nLista de Contatos")
  for numero_do_contato, contato in enumerate(contatos, start=1):
    contato_favorito = " (Favorito)" if contato["favorito"] else ""
    print(f"{numero_do_contato}. {contato['nome']} - {contato['telefone']} - {contato['email']}{contato_favorito}")

def editar_contato():
  listar_contatos()
  if not contatos:
    return
  try:
    escolha = int(input("Digite o número do contato que deseja editar: "))
    if escolha < 1 or escolha > len(contatos):
      print("Número inválido!")
      return
    contato = contatos[escolha - 1]
    print(f"Editando contato: {contato['nome']}")
    novo_nome = input(f"Novo nome (pressione enter para manter '{contato['nome']}'): ")
    novo_telefone = input(f"Novo telefone (pressione enter para manter '{contato['telefone']}'): ")
    novo_email = input(f"Novo email (pressione enter para manter '{contato['email']}'): ")

    if novo_nome:
      contato['nome'] = novo_nome
    if novo_telefone:
      contato['telefone'] = novo_telefone
    if novo_email:
      contato['email'] = novo_email

    print("Contato atualizado com sucesso!")
  except ValueError:
    print("Entrada inválida!")

def marcar_favorito():
  listar_contatos()
  if not contatos:
    return
  try:
      escolha = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: "))
      if escolha < 1 or escolha > len(contatos):
        print("Número inválido!")
        return
      contato = contatos[escolha - 1]
      contato['favorito'] = not contato['favorito']
      status = "marcado como favorito" if contato['favorito'] else "removido dos favoritos"
      print(f"Contato {status} com sucesso!")
  except ValueError:
    print("Entrada inválida!")

def listar_favoritos():
  favoritos = [contato for contato in contatos if contato["favorito"]]
  if not favoritos:
    print("Nenhum contato marcado como favorito.")
    return
  print("\nContatos Favoritos")
  for numero_do_contato, contato in enumerate(favoritos, start=1):
    print(f"{numero_do_contato}, {contato['nome']} - {contato['telefone']} - {contato['email']}")

def apagar_contato():
  listar_contatos()
  if not contatos:
    return
  try:
      escolha = int(input("Digite o número do contato que deseja apagar: "))
      if escolha < 1 or escolha > len(contatos):
        print("Número inválido!")
        return
      removido = contatos.pop(escolha - 1)
      print(f"Contato '{removido['nome']}' apagado com sucesso!")
  except ValueError:
    print("Entrada inválida!")

contatos = []
while True:
  print("\nAgenda de Contatos")
  print("1. Adicionar contato")
  print("2. Listar contatos")
  print("3. Editar contato")
  print("4. Marcar/Desmarcar favorito")
  print("5. Listar contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair")


  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    adicionar_contato()

  elif escolha == "2":
    listar_contatos()

  elif escolha == "3":
    editar_contato()

  elif escolha == "4":
    marcar_favorito()

  elif escolha == "5":
    listar_favoritos()

  elif escolha == "6":
    apagar_contato()

  elif escolha == "7":
    break