#módulo de cores (não funciona em input's)

from rich import print

# PRINT

def verde(txt):
    print(f'[bold][green]{txt}[/]')


def amarelo(txt):
    print(f'[bold][yellow]{txt}[/]')


def azul(txt):
    print(f'[bold][blue]{txt}[/]')


def vermelho(txt):
    print(f'[bold][red]{txt}[/]')


def roxo(txt):
    print(f'[bold][purple]{txt}[/]')


def branco(txt):
    print(f'[bold][white]{txt}[/]')


def brancoTxt(txt, c=False):
    if c == True:
        print(f'[bold][white]{txt}[/]'.center(85))
    else:
        print(f'[bold][white]{txt}[/]')

