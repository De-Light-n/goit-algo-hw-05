import re

def generator_numbers(text: str):
    pattern = r"\s\d+\.*\d*\s"# патерн відкликається на цілі і дійсні числа написані через "."
    numbers = map(float, re.findall(pattern, text)) # створює список з усіх найдених /
    for number in numbers:                          # чисел перетворюючи його на float
        yield number

def sum_profit(text, func):
    total_sum = 0
    gen = func(text) # присвоєння змінній функції генератора
    for number in gen: # ітерація по генератору
        total_sum += number
    return total_sum

if __name__=="__main__":
    text = """Загальний дохід працівника складається з декількох
            частин: 1000.01 як основний дохід,
            доповнений додатковими надходженнями 27.45 і 324.00 доларів.
            Ше трохи тексту 10000 лалалала 49.50 ."""
            
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
