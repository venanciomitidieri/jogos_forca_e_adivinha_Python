import random


def jogar():
    print('***************')
    print('Bem vindo ao jogo de adivinhação!')
    print('***************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Define o nível: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou:', chute)

        if 0 < chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos}!')
            break
        else:
            if maior:
                print('Você errou! Seu número foi maior que o número secreto')
            elif menor:
                print('Você errou! Seu chute foi menor que o número secreto')
            pontas_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontas_perdidos

    print('Fim do Jogo...')


if __name__ == '__main__':
    jogar()


