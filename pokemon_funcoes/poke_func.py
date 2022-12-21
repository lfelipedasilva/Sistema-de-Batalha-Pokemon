from modulos_pessoais import cores as c


def danoCalc(atq=100, move=60, defIni=100):
    """
    :param: atq: recebe o status de ataque do pokemon que atacara e retorna 100 se nada for informado.
    :param: move: recebe o base power do movimento que será usado pelo pokemon e retorna 60 se nada for informado.
    :param: defIni: recebe o status de defesa do pokemon adversário e retorna 100 se nada for informado.
    :return: retorna o resultado final do calculo de dano.

    """
    calc1 = ((((2 * 100 / 5 + 2) * atq * move / defIni) / 50) + 2) * \
        1.5 * 2 * 100/100
    dano = calc1
    return dano


# MOVIMENTOS DO MEWTWO
def psystrike(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Mewtwo usou PsyStrike')
    print('\n')
    dano = danoCalc(447, 100, defesa)
    return dano


def aura_sphere(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Mewtwo usou Aura Sphere')
    print('\n')
    dano = danoCalc(447, 80, defesa)
    return dano


def thunderbolt(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Mewtwo usou Thunderbolt')
    print('\n')
    dano = danoCalc(447, 90, defesa)
    return dano


def shadow_ball(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Mewtwo usou Shadow Ball')
    print('\n')
    dano = danoCalc(447, 70, defesa)
    return dano


# MOVIMENTOS DO VENUSSAUR
def giga_drain(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Venussaur usou Giga Drain')
    print('\n')
    dano = danoCalc(328, 75, defesa)
    return dano


def sludge_wave(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Venussaur usou Sludge Wave')
    print('\n')
    dano = danoCalc(328, 95, defesa)
    return dano


def earthquake(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Venussaur usou Earthquake')
    print('\n')
    dano = danoCalc(328, 100, defesa)
    return dano


def rock_climb(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Venussaur usou Rock Climb')
    print('\n')
    dano = danoCalc(328, 80, defesa)
    return dano


# MOVIMENTOS DO CHARIZARD
def flamethower(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Charizard usou Flamethower')
    print('\n')
    dano = danoCalc(348, 90, defesa)
    return dano


def air_slash(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Charizard usou Air Slash')
    print('\n')
    dano = danoCalc(348, 75, defesa)
    return dano


def dragon_pulse(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Charizard usou Dragon Pulse')
    print('\n')
    dano = danoCalc(348, 80, defesa)
    return dano


def solar_beam(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Charizard usou Solar Beam')
    print('\n')
    dano = danoCalc(348, 120, defesa)
    return dano


# MOVIMENTOS DO BLASTOISE
def surf(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Blastoise usou Surf')
    print('\n')
    dano = danoCalc(295, 90, defesa)
    return dano


def flash_cannon(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Blastoise usou Flash Cannon')
    print('\n')
    dano = danoCalc(295, 80, defesa)
    return dano


def focus_blast(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Blastoise usou Focus Blast')
    print('\n')
    dano = danoCalc(295, 120, defesa)
    return dano


def giga_impact(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Blastoise usou Giga Impact')
    print('\n')
    dano = danoCalc(295, 150, defesa)
    return dano


# MOVIMENTOS DO ROTOM-WASH
def discharge(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Rotom usou Discharge')
    print('\n')
    dano = danoCalc(339, 80, defesa)
    return dano


def volt_switch(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Rotom usou Volt Switch')
    print('\n')
    dano = danoCalc(339, 75, defesa)
    return dano


def dark_pulse(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Rotom usou Dark Pulse')
    print('\n')
    dano = danoCalc(339, 80, defesa)
    return dano


def charge_beam(defesa=100, pr=False):
    if pr == True:
        c.amarelo('Rotom usou Charge Beam')
    print('\n')
    dano = danoCalc(339, 60, defesa)
    return dano
