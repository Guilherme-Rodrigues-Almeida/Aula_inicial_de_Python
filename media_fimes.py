filme1 = "Toy story"
filme2 = "Shrek 2"
filme3 = "Matrix 3"

filmes = ["Toy story", "Shrek 2", "Matrix 3"]
print(filmes) 

filmes2 = [filme1, filme2, filme3]
print(filmes)

print(filmes[-1])
print(filmes[-2:])
print("")
print("")
print("")

def imprime_filmes(filmes_que_quero_imprimir):
    print("A lista de filmes disponivel: ")
    print(filmes_que_quero_imprimir)

imprime_filmes(filmes)

print("")
print("")

for filme in filmes:
    print("...")
    print (filme)
print("...")

print("")
print("")

def imprime_filmes(filmes_que_quero_imprimir):
    print("A lista de filmes disponivel: ")
    for filme in filmes_que_quero_imprimir: 
        print("...")
        print (filme)
    print("...")

imprime_filmes(filmes)

print("")
print("")

dados = {"nome" : "Guilherme", 
        "idade": 37,
        "empresa" : "Alura"}

print(dados["nome"])
print(dados["idade"])
print(dados["empresa"])