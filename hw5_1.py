def caching_fibonacci():
    cache = dict()
    def fibonacci(n:int):
        if n <= 0: return 0 # повернення мінімальних значень рекурсії при їх досягненні
        if n == 1: return 1
        if cache.get(n) == None: # перевірка на наявність n-го числа
            cache[n] = fibonacci(n-1) + fibonacci(n-2) # обчислення такого якщо його нема
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(7))
print(fib(10))
print(fib(20))
print(fib(25))
print(fib(30))
print(fib(50))
print(fib(77))
