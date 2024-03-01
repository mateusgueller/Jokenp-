import random

print('#-' * 12)
print('Bem-Vindo caro Jogador!')
print('Hoje, jogaremos Jokenpô!')
print('#-' * 12)
jogador = str(input('Faça sua escolha!: ')).strip().title()

escolha = ['Pedra', 'Papel', 'Tesoura']

computador = random.choice(escolha)

if jogador == computador:
    print('Eu escolho: {}. \nEMPATE!'.format(computador))
elif jogador == 'Pedra' and computador == 'Papel':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Papel' and computador == 'Pedra':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Pedra' and computador == 'Tesoura':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Tesoura' and computador == 'Pedra':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Tesoura' and computador == 'Papel':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Papel' and computador == 'Tesoura':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Papel' and computador == 'Pedra':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Pedra' and computador == 'Papel':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Pedra' and computador == 'Tesoura':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Tesoura' and computador == 'Pedra':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Pedra' and computador == 'Tesoura':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
elif jogador == 'Papel' and computador == 'Tesoura':
    vencedor = computador
    print('Eu escolho: {}. Computador vence!'.format(vencedor.upper()))
elif jogador == 'Tesoura' and computador == 'Papel':
    vencedor = jogador
    print('Eu escolho: {}. Jogador vence!'.format(vencedor.upper()))
