
def validate_rut(rut: str) -> bool:
    rut = rut.replace(".", "").replace("-", "").upper()
    cuerpo, dv = rut[:-1], rut[-1]
    return module_11(cuerpo) == dv

def module_11(num: str) -> str:
    factors = [2, 3, 4, 5, 6, 7]
    sum = 0
    factor_index = 0
    for digito in reversed(num):
        sum += int(digito) * factors[factor_index]
        factor_index = (factor_index + 1) % len(factors)
    rest = 11 - (sum % 11)
    if rest == 11:
        return "0"
    elif rest == 10:
        return "K"
    else:
        return str(rest)