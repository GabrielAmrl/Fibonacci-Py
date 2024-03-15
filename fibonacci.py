def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = 10  
resultado = fibonacci(n)
print("Sequencia de Fibonacci para os primeiros", n, "numeros:", resultado)
