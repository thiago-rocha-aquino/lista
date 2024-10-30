numeros =[]
par = []
impar = []
for i in range(10):
    num = int(input("digite 10 números: "))
    numeros.append(num)
    if (num % 2 == 0):
        par.append(num)
    else:
        impar.append(num)  
print("lista de todos os números: ", numeros)
print("lista de todos os números pares: ", par)
print("lista de todos os números ímpares: ", impar)        