from random import randint

print('Hello, World!')

a = int(input('Digite um número aleatório: '))
print(a)


print("""Olá mundo! testando modificação de arquivo commitado no github
      hahah que legal, muito divertido, androi app de angrboa, god of war ragnarok
      é muito bom e the last of us também, tanto a part 1 quanto a part 2 (a história
      da part 1 é melhor""")


# vamos jogar um jogo ?

while True:
    comp = randint(1, 10)
    jog = int(input('Tente adivinhar o numero de 1 á 10: '))
    if jog == comp:
        break
