def boas_vindas(turma):
  # def é uma palavra-chave usada para definir uma função. Quando você usa def, está criando   uma nova função que pode ser chamada posteriormente no seu código.
 
  print("Bem-vindos à turma de programação da nossa eletiva!")
  print("Estamos muito felizes em ter vocês aqui!")
  print("Vamos aprender e nos divertir juntos!")
#print é uma função usada para exibir mensagens ou valores na tela.
  for aluno in turma:
    print(f"Olá, {aluno}! Prepare-se para uma jornada incrível de aprendizado.")
 
# for e in são usados juntos para criar um loop que itera sobre uma sequência (como uma lista, ou string)
 
 
turma = ["Renan Salermo", "Clândio da Silva", "Dani Silva"]
# Colocar a lista da turma
 
boas_vindas(turma)
 
# Chama a função de boas-vindas
