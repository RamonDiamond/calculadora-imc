peso = float(input("informe o seu peso (kg) "))
altura = float(input("informe a sua altura (m) "))

imc = peso / (altura ** 2)

print(f"Seu imc é {imc: .2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")
