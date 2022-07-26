def cor(txt, cor=0):
    """
    param txt: Texto que vai mudar de cor.
    return: Texto formatado na cor VERDE (0) ou VERMELHA (1)
    """
    if cor == 0:
        return f'\033[32m{txt}\033[m'
    elif cor == 1:
        return f'\033[31m{txt}\033[m'
    else:
        return txt