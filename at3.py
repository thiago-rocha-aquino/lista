#Desenvolver um programa em Python que recebe a temperatura média
# de cada mês do ano armazenando-as em uma lista. Após isto,
# calcule a média anual das temperaturas e mostre todas as temperaturas
# acima da média anual e, em que mês elas ocorrem.
temp = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
for i in range(12):
    temperatura = float(input(f"Digite a temperatura em graus celsius média de {meses[i]}: "))
    temp.append(temperatura)
media_anual = sum(temp) / len(temp)
print(f"\nMédia anual de temperatura: {media_anual}°C")

print("\nMeses com temperatura acima da média anual:")
for i in range(12):
    if temp[i] > media_anual:
        print(f"{meses[i]} - {temp[i]}°C")