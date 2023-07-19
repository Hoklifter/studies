
def factorial(n):
    if n == 1:
        return (1)
    else:
        # fatorial(5) = 5 * fatorial(4) = 4 * fatorial(3) = 3 * fatorial(2) = 2 * fatorial(1) = 1
        return (n * factorial(n - 1))

        # fatorial(1) = 1, fatorial(2) = 2 * 1 = 2, fatorial(3) = 3*2=6, fatorial(4) = 4*6 = 24, fatorial(5) = 5*24 = 120
        # Retornará o argumento multiplicado pelo número antecessor dado pela mesma função com o argumento-1 como parâmetro, até o argumento se tornar 1 e a função se dar por encerrada.
print(factorial(5))


# COMPREHENSION FUNC


def factorial2(n):
    if n == 1:
        print(n)
        return n
    else:
        num = (n * factorial2(n - 1))
        print(num)
        return num


factorial2(5)
