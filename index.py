def multiply(a:float , b:float) -> float:
    return (a*b)

def multiply(a:int, b:int) -> int:
    return(a*b)

def multiply(a:float, b:int) -> int:
    return(a*b)

def multiply(a:int, b:float) -> int:
    return(a*b)

def multiply(a: complex, b: complex) -> int:
    # Complex numbers must be denoted with a j behind the number
    return(a*b)

def multiply(a: complex, b: complex) -> float:
    return(a*b)

def divide(a:float , b:float) -> float:
    return (a/b)

def divide(a:int, b:int) -> int:
    return(a/b)

def divide(a:int, b:float) -> int:
    return(a/b)

def divide(a:float, b:int) -> int:
    return(a/b)

def divide(a: complex, b: complex) -> int:
    # Complex numbers must be denoted with a j behind the number
    return(a/b)

def divide(a: complex, b: complex) -> float:
    return(a/b)

def exp(a: int, b: int) -> int:
    return(a**b)

def exp(a: float, b: int) -> float:
    return(a**b)

def exp(a: int, b: float) -> float:
    return(a**b)

def exp(a: float, b: float) -> float:
    return(a**b)