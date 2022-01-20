import pygame
import Cores
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('EX021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
print('{}Sua musica está tocando{}'.format(Cores.cores['vermelho'], Cores.cores['limpa']))

continuo = 'n'
while continuo in 'nNnaoNaonãoNão':
    pergunta = input('Deseja finalizar a musica?')
    continuo = pergunta
    if not continuo in 'nNnaoNaonãoNão':
        pygame.mixer.quit()
    pygame.event.wait()
