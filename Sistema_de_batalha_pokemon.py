# Antes de testar o código principal pega os módulos que eu fiz seu pateta >:(

from rich.table import Table
from modulos_pessoais import cores as c
from rich.console import Console
from random import randint
from pokemon_funcoes import poke_func as fu

console = Console()

c.branco('-'*75)
c.brancoTxt('SISTEMA DE BATALHA POKEMON', True)
c.branco('-'*75)
c.amarelo('Olá jogador, bem vindo ao SBP, escolha abaixo qual pokemon deseja usar:')
print('\n')

# Pokemon do jogador

pokJogador = Table(title=c.branco('POKEMONS DISPONÍVEIS'), style='blue')

pokJogador.add_column('[bold][white]Venussaur[/]', justify='center')
pokJogador.add_column('[bold][white]Charizard[/]', justify='center')
pokJogador.add_column('[bold][white]Blastoise[/]', justify='center')

pokJogador.add_row('HP: [bold][green]1564[/]',
                   'HP: [bold][green]1150[/]', 'HP: [bold][green]1482[/]')
pokJogador.add_row('Ataque: [bold][green]328[/]',
                   'Ataque: [bold][green]348[/]', 'Ataque: [bold][green]295[/]')
pokJogador.add_row('Defesa: [bold][green]328[/]',
                   'Defesa: [bold][green]295[/]', 'Defesa: [bold][green]349[/]')
pokJogador.add_row('Velocidade: [bold][green]284[/]',
                   'Velocidade: [bold][green]328[/]', 'Velocidade: [bold][green]280[/]')

pokJogador.add_row('-'*20, '-'*20, '-'*20)

pokJogador.add_row('[bold][white]1 -[/] Giga Drain: [green]75[/]',
                   '[bold][white]1 -[/] Flamethower: [green]90[/]', '[bold][white]1 -[/] Surf: [green]90[/]')
pokJogador.add_row('[bold][white]2 -[/] Sludge Wave: [green]95[/]',
                   '[bold][white]2 -[/] Air Slash: [green]75[/]', '[bold][white]2 -[/] Flash Cannon: [green]80[/]')
pokJogador.add_row('[bold][white]3 -[/] Earthquake: [green]100[/]',
                   '[bold][white]3 -[/] Dragon Pulse: [green]80[/]', '[bold][white]3 -[/] Focus Blast: [green]120[/]')
pokJogador.add_row('[bold][white]4 -[/] Rock Climb: [green]80[/]',
                   '[bold][white]4 -[/] Solar Beam: [green]120[/]', '[bold][white]4 -[/] Giga Impact: [green]150[/]')

console.print(pokJogador)
print('\n')

while True:
    opJog = str(input('Qual pokemon deseja escolher? ')).strip().upper()
    if opJog == 'BLASTOISE' or opJog == 'CHARIZARD' or opJog == 'VENUSSAUR':
        break
    else:
        c.vermelho('Por Favor, digite uma opção válida!')

print('\n')
c.verde(f'VOCÊ ESCOLHEU O {opJog}!')

# Escolha do pokemon advcersário contra quem irá batalhar

c.branco('-'*75)
c.amarelo('Agora escolha contra qual pokemon deseja batalhar: ')
print('\n')

pokInimigo = Table(title=c.branco('POKEMONS ADVERSÁRIOS DISPONÍVEIS'), style='yellow')

pokInimigo.add_column('MewTwo', justify='center')
pokInimigo.add_column('Rotom-Wash', justify='center')
pokInimigo.add_column('Arceus', justify='center')

pokInimigo.add_row('HP: [bold][green]1280[/]',
                   'HP: [bold][green]942[/]', '[red]Não é possível ver os stats desse pokemon.[/]')
pokInimigo.add_row('Ataque: [bold][green]447[/]',
                   'Ataque: [bold][green]339[/]', '-')
pokInimigo.add_row('Defesa: [bold][green]306[/]',
                   'Defesa: [bold][green]455[/]', '-')
pokInimigo.add_row('Velocidade: [bold][green]394[/]',
                   'Velocidade: [bold][green]298[/]', '-')

pokInimigo.add_row('-'*20, '-'*20, '-'*20)

pokInimigo.add_row('[bold][white]1 -[/] PsyStrike: [green]100[/]',
                   '[bold][white]1 -[/] Discharge: [green]80[/]', '-')
pokInimigo.add_row('[bold][white]2 -[/] Aura Sphere: [green]80[/]',
                   '[bold][white]2 -[/] Volt Switch: [green]75[/]', '-')
pokInimigo.add_row('[bold][white]3 -[/] Thunderbolt: [green]90[/]',
                   '[bold][white]3 -[/] Dark Pulse: [green]80[/]', '-')
pokInimigo.add_row('[bold][white]4 -[/] Shadow Ball: [green]70[/]',
                   '[bold][white]4 -[/] Charge Beam: [green]60[/]', '-')

console.print(pokInimigo)
print('\n')

while True:
    opIni = str(input('Contra qual pokemon deseja batalha? ')).strip().upper()
    if opIni == 'MEWTWO' or opIni == 'ROTOM' or opIni == 'ROTOM-WASH' or opIni == 'ARCEUS':
        break
    else:
        c.vermelho('Por Favor, digite uma opção válida!')

print('\n')
c.verde(f'VOCÊ ESCOLHEU ENFRENTAR O {opIni}!')

# VIDA DO POKEMON DO JOGADOR

venussaur = {'hp': 1564}

charizard = {'hp': 1150}

blastoise = {'hp': 1482}

# VIDA DO ADVERSÁRIO

mewtwo = {'hp': 1280}

rotom = {'hp': 942}


# Batalhas pokemon

print('-'*75)
print(f'{opJog} X {opIni}')
c.amarelo('QUE COMEÇE A BATALHA!')
print('\n')

# Venussaur X MewTwo
if opJog == 'VENUSSAUR' and opIni == 'MEWTWO':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # MEWTWO ----------------------------------------------------------------------------------------

            print('\n')
            mewtwoMoves = randint(1, 4)

            if mewtwoMoves == 1:
                venussaur['hp'] -= fu.psystrike(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.psystrike(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 2:
                venussaur['hp'] -= fu.aura_sphere(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.aura_sphere(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 3:
                venussaur['hp'] -= fu.thunderbolt(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.thunderbolt(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 4:
                venussaur['hp'] -= fu.shadow_ball(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.shadow_ball(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if venussaur['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')

        # VENUSSAUR -----------------------------------------------------------------------------------
        if opMove == 1:
            mewtwo['hp'] -= fu.giga_drain(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.giga_drain(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 2:
            mewtwo['hp'] -= fu.sludge_wave(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.sludge_wave(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 3:
            mewtwo['hp'] -= fu.earthquake(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.earthquake(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 4:
            mewtwo['hp'] -= fu.rock_climb(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.rock_climb(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if mewtwo['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O MEWTWO!')
            break


# CHARIZARD X MEWTWO
if opJog == 'CHARIZARD' and opIni == 'MEWTWO':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # MEWTWO ----------------------------------------------------------------------------------------

            print('\n')
            mewtwoMoves = randint(1, 4)

            if mewtwoMoves == 1:
                charizard['hp'] -= fu.psystrike(295, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.psystrike(295):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 2:
                charizard['hp'] -= fu.aura_sphere(295, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.aura_sphere(295):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 3:
                charizard['hp'] -= fu.thunderbolt(295, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.thunderbolt(295):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 4:
                charizard['hp'] -= fu.shadow_ball(295, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.shadow_ball(295):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if charizard['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')

        # CHARIZARD -----------------------------------------------------------------------------------
        if opMove == 1:
            mewtwo['hp'] -= fu.flamethower(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.flamethower(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 2:
            mewtwo['hp'] -= fu.air_slash(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.air_slash(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 3:
            mewtwo['hp'] -= fu.dragon_pulse(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.dragon_pulse(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 4:
            mewtwo['hp'] -= fu.solar_beam(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.solar_beam(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if mewtwo['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O MEWTWO!')
            break


# BLASTOISE X MEWTWO
if opJog == 'BLASTOISE' and opIni == 'MEWTWO':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # MEWTWO ----------------------------------------------------------------------------------------

            print('\n')
            mewtwoMoves = randint(1, 4)

            if mewtwoMoves == 1:
                blastoise['hp'] -= fu.psystrike(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.psystrike(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 2:
                blastoise['hp'] -= fu.aura_sphere(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.aura_sphere(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 3:
                blastoise['hp'] -= fu.thunderbolt(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.thunderbolt(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if mewtwoMoves == 4:
                blastoise['hp'] -= fu.shadow_ball(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.shadow_ball(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if blastoise['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')

        # BLASTOISE -----------------------------------------------------------------------------------
        if opMove == 1:
            mewtwo['hp'] -= fu.surf(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.surf(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 2:
            mewtwo['hp'] -= fu.flash_cannon(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.flash_cannon(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 3:
            mewtwo['hp'] -= fu.focus_blast(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.focus_blast(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if opMove == 4:
            mewtwo['hp'] -= fu.giga_impact(306, True)
            if mewtwo['hp'] < 0:
                mewtwo['hp'] = 0
            c.verde(f'Mewtwo tomou {fu.giga_impact(306):.0f} de dano e agora tem {mewtwo["hp"]:.0f} de HP')

        if mewtwo['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O MEWTWO!')
            break


# BLASTOISE X ROTOM-WASH
if opJog == 'BLASTOISE' and opIni == 'ROTOM' or opJog == 'BLASTOISE' and opIni == 'ROTOM-WASH':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # ROTOM-WASH ----------------------------------------------------------------------------------------

            print('\n')
            rotomMoves = randint(1, 4)

            if rotomMoves == 1:
                blastoise['hp'] -= fu.discharge(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.discharge(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 2:
                blastoise['hp'] -= fu.volt_switch(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.volt_switch(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 3:
                blastoise['hp'] -= fu.dark_pulse(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.dark_pulse(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 4:
                blastoise['hp'] -= fu.charge_beam(349, True)
                if blastoise['hp'] < 0:
                    blastoise['hp'] = 0
                c.verde(f'Você tomou {fu.charge_beam(349):.0f} de dano, agora lhe resta {blastoise["hp"]:.0f} de hp')
                print('\n')

            if blastoise['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')

        # BLASTOISE -----------------------------------------------------------------------------------
        if opMove == 1:
            rotom['hp'] -= fu.surf(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.surf(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 2:
            rotom['hp'] -= fu.flash_cannon(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.flash_cannon(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 3:
            rotom['hp'] -= fu.focus_blast(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.focus_blast(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 4:
            rotom['hp'] -= fu.giga_impact(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.giga_impact(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if rotom['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O ROTOM-WASH!')
            break


# VENUSSAUR X ROTOM-WASH
if opJog == 'VENUSSAUR' and opIni == 'ROTOM' or opJog == 'VENUSSAUR' and opIni == 'ROTOM-WASH':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # ROTOM-WASH ----------------------------------------------------------------------------------------

            print('\n')
            rotomMoves = randint(1, 4)

            if rotomMoves == 1:
                venussaur['hp'] -= fu.discharge(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.discharge(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 2:
                venussaur['hp'] -= fu.volt_switch(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.volt_switch(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 3:
                venussaur['hp'] -= fu.dark_pulse(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.dark_pulse(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 4:
                venussaur['hp'] -= fu.charge_beam(328, True)
                if venussaur['hp'] < 0:
                    venussaur['hp'] = 0
                c.verde(f'Você tomou {fu.charge_beam(328):.0f} de dano, agora lhe resta {venussaur["hp"]:.0f} de hp')
                print('\n')

            if venussaur['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')

        # VENUSSAUR -----------------------------------------------------------------------------------
        if opMove == 1:
            rotom['hp'] -= fu.giga_drain(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.giga_drain(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 2:
            rotom['hp'] -= fu.sludge_wave(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.sludge_wave(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 3:
            rotom['hp'] -= fu.earthquake(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.earthquake(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 4:
            rotom['hp'] -= fu.focus_blast(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.focus_blast(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if rotom['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O ROTOM-WASH!')
            break


# CHARIZARD X ROTOM-WASH
if opJog == 'CHARIZARD' and opIni == 'ROTOM' or opJog == 'CHARIZARD' and opIni == 'ROTOM-WASH':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        # CHARIZARD -----------------------------------------------------------------------------------
        if opMove == 1:
            rotom['hp'] -= fu.flamethower(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.flamethower(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 2:
            rotom['hp'] -= fu.air_slash(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.air_slash(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 3:
            rotom['hp'] -= fu.dragon_pulse(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.dragon_pulse(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if opMove == 4:
            rotom['hp'] -= fu.solar_beam(455, True)
            if rotom['hp'] < 0:
                rotom['hp'] = 0
            c.verde(f'Rotom tomou {fu.solar_beam(455):.0f} de dano e agora tem {rotom["hp"]:.0f} de HP')

        if rotom['hp'] == 0:
            print('\n')
            c.amarelo('VOCÊ DERROTOU O ROTOM-WASH!')
            break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            # ROTOM-WASH ----------------------------------------------------------------------------------------

            print('\n')
            rotomMoves = randint(1, 4)

            if rotomMoves == 1:
                charizard['hp'] -= fu.discharge(328, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.discharge(328):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 2:
                charizard['hp'] -= fu.volt_switch(328, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.volt_switch(328):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 3:
                charizard['hp'] -= fu.dark_pulse(328, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.dark_pulse(328):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if rotomMoves == 4:
                charizard['hp'] -= fu.charge_beam(328, True)
                if charizard['hp'] < 0:
                    charizard['hp'] = 0
                c.verde(f'Você tomou {fu.charge_beam(328):.0f} de dano, agora lhe resta {charizard["hp"]:.0f} de hp')
                print('\n')

            if charizard['hp'] <= 0:
                print('\n')
                c.vermelho('VOCÊ PERDEU!')
                break

        elif opMove == 5:
            console.print(pokJogador)

        elif opMove == 0:
            print('\n')
            c.vermelho('O jogador preferiu desistir e fugiu.')
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            break
        else:
            c.vermelho('Por Favor, digite uma opção válida.')


# VENUSSAUR, CHARIZARD OU BLASTOISE X ARCEUS
if opIni == 'ARCEUS':
    while True:
        while True:
            try:
                print('\n')
                opMove = int(input('Qual movimento deseja usar?[0 - FUGIR][5 - VER TABELA]: '))
            except Exception:
                c.vermelho('Por Favor, digite uma opção válida!')
            else:
                break

        if opMove == 1 or opMove == 2 or opMove == 3 or opMove == 4:
            print('\n')
            c.vermelho('VOCÊ PERDEU!')
            print('\n')
            c.amarelo('KKKK Você realmente achou que ia vencer o DEUS pokemon? ._.')
            break
        
        elif opMove == 5:
            console.print(pokJogador)
        
        elif opMove == 0:
            print('\n')
            c.vermelho('Você não pode fugir do DEUS pokemon.')

        else:
            print('\n')
            c.vermelho('Por Favor, digite uma opção válida!')



# Sim eu sei, é grande :>

# Se eu quisesse eu podia ter encurtado o código modularizando as batalhas ja que a base delas
# é basicamente um CTRL c CTRL v mas fiquei com preguiça :v (o que é meio contraditório, srsr mas enfim)
# :)
