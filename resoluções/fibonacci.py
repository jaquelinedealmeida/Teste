def calcula_fibonacci(num):

    fibonacci = [0,1]

    while fibonacci[-1] < num:
       fibonacci.append(fibonacci[-1] + fibonacci[-2])

    if  num in fibonacci:
        return f"O número {num} pertence a sequência Fibonacci"
    else:
        return f"O número {num} não pertence a sequência Fibonacci"

numero = int(input("Informe um número"))

print(calcula_fibonacci(numero))