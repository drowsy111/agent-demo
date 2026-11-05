def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def safe_divide(a: float, b: float) -> float:
    # Bug: 没有判断 b 是否为 0
    return a / b

def factorial(n: int) -> int:
    # Bug: 这是一个死循环，且没有处理负数
    result = 1
    while n > 0:
        result *= n
    return result
