def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        return 0.0
    return a / b

def factorial(n: int) -> int:
    if n <= 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
