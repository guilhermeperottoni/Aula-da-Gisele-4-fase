num0 = "zero\n"
num1 = "Um\n"
num2 = "Dois\n"
num3 = "Três\n"
num4 = "Quatro\n"
num5 = "Cinco\n"

numero = -1

while numero != 0:
    numero = int (input("Para encerrar o programa digite 0 \nDigite um numero inteiro entre 1 e 5: "))

    if numero < 1 or numero > 5:
        print ("Numero inválido! Para encerrar o programa digite 0 \n Digite um numero entre 1 e 5: ")

    if numero == 0:
        print(num0)
    if numero == 1:
        print(num1)

    if numero == 2:
        print(num2)
    
    if numero == 3:
        print(num3)
    
    if numero == 4:
        print (num4)
    
    if numero == 5:
        print (num5)

print("Programa finalizado!!!")
