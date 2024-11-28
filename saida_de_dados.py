idade: int
salario: float; altura: float 
genero: str 
nome: str 
idade = 20 
salario = 5800.5 
altura = 1.63 
genero = "F" 
nome = "Maria Silva" 
print(f"IDADE = {idade}") 
print(f"SALARIO = {salario:.2f}") 
print(f"ALTURA = {altura:.2f}") 
print(f"GENERO = {genero}") 
print(f"NOME = {nome}")

print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))
