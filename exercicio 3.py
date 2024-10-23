# Lê os dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os números e imprime o resultado
if numero1 > numero2:
    print(f"O maior número é: {numero1}")
    print(f"O menor número é: {numero2}")
elif numero1 < numero2:
    print(f"O maior número é: {numero2}")
    print(f"O menor número é: {numero1}")
else:
    print("Os números são iguais.")