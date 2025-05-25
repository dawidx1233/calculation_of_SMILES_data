import logging as l

l.basicConfig(level=l.INFO)
logger = l.getLogger("Divider")


def dzielnik(a: float, b: float) -> float | None:
    logger.info(f"Próba podzielenia {a} przez {b}")
    if b == 0:
        logger.error("Dzielenie przez zero!")
        return None
    wynik = a / b
    logger.info(f"Wynik: {wynik}")
    return wynik

dzielnik(10, 2)
dzielnik(10, 0)
dzielnik(11, 3)
