# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    raiz = b**2-4*a*c
    if raiz < 0:
        return "( )"
    
    primer_raiz = (-b+(raiz)**1/2)/(2*a)
    if raiz == 0:
        return f"({primer_raiz})"

    segunda_raiz = (-b-(raiz)**1/2)/(2*a)
    return f"({primer_raiz}, {segunda_raiz})"

def value_y(a, b, c, x):
    resultado = a*x*x+b*x+c
    return resultado


def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    return f"f'(x) = {2*a}x + {b}"
