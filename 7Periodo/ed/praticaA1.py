# LISTA = coleção ordenada e mútavel, permitindo membros duplicados
print("\n----LISTA----")
lista = ["carro", "avião", "barco", "bicicleta"]
lista2 = ("carro", True, 2, 2.5)

#imprime toda lista
print(f'\nA lista de palavras: {lista}')
print(f'\nTestando segunda lista: {lista2}')

# para imprimir cada palavra 
c = 0
for palavra in lista: 
    print(f'\n Na posição {c}: {palavra}')
    c += 1 

# como saber o tipo de dado se é lista/chave
print(f'\n{type(lista)}')


print("\n----TUPLA----")


# TUPLA | USA OS () = coleção ordenada e Imútavel, permitindo membros duplicados
tupla = ("carro", True, 2, 2.5)
print(f'\n{tupla}')
print(f'\n{type(tupla)}')


print("\n----DICIONÁRIO----") # = coleção ordenada e mútavel, NÃO permite membros duplicados


# DICIONÁRIO | USA AS {} | chave : valor
dicionario = {"chave", "valor"}
dicionario2 = {"nome": "HB20", "logica": True, "numero": 2}

print(f'\n{dicionario}')
print(f'\n{type(dicionario)}')
print(f'\n{dicionario2}')


print("\n----CONJUNTO----") # = coleção NÃO ordenada e NÃO indexada, NÃO permite membros duplicados


# CONJUNTO/SET | {}
conjunto = {"carro", True, 2, 2.3}
print(f'\n{conjunto}')
print(f'\n{type(conjunto)}')