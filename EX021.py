import pygame
import Cores
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('EX021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
print('{}Sua musica está tocando{}'.format(Cores.cores['vermelho'], Cores.cores['limpa']))
pygame.event.wait()


