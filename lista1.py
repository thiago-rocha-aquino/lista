#lista para mercado
compras = []
element = 0
while element != "fim":
    element = input("digite produto: ")
    print("digite fim para finalizar: ")
    if(element != "fim"):
        compras.append(element)
print(compras)   
for produtos in compras:
    print(produtos)
compras.sort()
print(compras)         