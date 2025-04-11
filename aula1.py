idade = int (input('Qual a sua idade?'))
 
if idade <12:
    print ('criança')
elif idade >=12 and idade <=17:
    print ('adolescente')
if idade > 18:
    print('adulto')

 # Solicita ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os dois números
if numero1 > numero2:
    print(f"O maior número é {numero1}")
elif numero2 > numero1:
    print(f"O maior número é {numero2}")
else:
    print("Os dois números são iguais.")

 # Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se a entrada é uma letra
if letra.isalpha() and len(letra) == 1:
    # Verifica se a letra é uma vogal
    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("Por favor, digite apenas uma letra válida.")


# Solicita ao usuário para definir uma senha
senha = input("Defina uma senha: ")

# Solicita a confirmação da senha
confirmacao_senha = input("Confirme a senha: ")

# Compara as senhas
if senha == confirmacao_senha:
    print("Acesso permitido")
else:
    print("Senhas não coincidem")

# Leitura dos 3 números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprime os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros)

 # Entrada de dados
tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

# Cálculo da distância percorrida (DISTÂNCIA = TEMPO * VELOCIDADE)
distancia_percorrida = tempo_gasto * velocidade_media

# Cálculo da quantidade de litros de combustível usados (LITROS_USADOS = DISTÂNCIA / 12)
litros_usados = distancia_percorrida / 12

# Exibição dos resultados
print(f"\nVelocidade média: {velocidade_media} km/h")
print(f"Tempo gasto: {tempo_gasto} horas")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Quantidade de litros de combustível utilizados: {litros_usados:.2f} litros")

