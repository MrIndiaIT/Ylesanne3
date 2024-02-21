import pygame
import sys 

#Pygame'i alustamine
pygame.init()

#Ekraani suurus
ekraani_laius = 640
ekraani_korgus = 480

#Ruudu suurus
ruudu_suurus = 20

#Ridade ja veergude arvud
read_arv = 24
veergude_arv = 32

#Ekraani seadistamine
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Ülesanne 3")

#Ruudu joone värv
joone_varv = (212, 51, 0)

#Ruudustiku joonistamise funktsioon
def joonista_ruudustik():
    for rida in range(read_arv):
        for veerg in range(veergude_arv):
            ruudu_x = veerg * ruudu_suurus
            ruudu_y = rida * ruudu_suurus
            pygame.draw.rect(ekraan, joone_varv, (ruudu_x, ruudu_y, ruudu_suurus, ruudu_suurus), 1)

#Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Ekraani täite värv
    ekraan.fill((161, 248, 153))
    
    #Ruudustiku joonistamine
    joonista_ruudustik()

    #Ekraani värskendamine
    pygame.display.flip()

# Pygame sulgemine
pygame.quit()
sys.exit()
