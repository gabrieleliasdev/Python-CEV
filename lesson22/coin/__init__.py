def half(p, format=False):
    p = p / 2
    return p if format is False else money(p)

def double(p, format=False):
    p = p * 2
    return p if format is False else money(p)

def increase(p=float, rate=0, format=False):
    p = p + (p * rate / 100)
    return p if format is False else money(p)

def decrease(p=float, rate=0, format=False):
    p = p - (p * rate / 100)
    return p if format is False else money(p)

def money(p=0, sign="R$"):
    return f"{sign}{p:>.2f}".replace(".", ",")

def resume(p=0, rate1=0, rate2=0):
    from textwrap import dedent
    print(dedent(f"""
                      Analyzed Price » \t{money(p)}
                      Double the Price » \t{double(p, True)}
                      Half-price » \t\t{half(p, True)}
                      {rate1}% increase » \t\t{increase(p, rate1, True)}
                      {rate2}% reduction » \t{decrease(p, rate2, True)}
                """))
