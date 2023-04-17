import pygame, sys
import level_construct
import time

pygame.init()
# basic settings
WHITE = (255, 255, 255)
window = pygame.display.set_mode((1280,720))
window.fill(WHITE)
pygame.display.set_caption("Wake up, pp2ease!")

pygame.mixer.music.load(r"assets/mp3/lullaby.mp3")
pygame.mixer.music.play(-1)

button = pygame.image.load(f"assets/button.png")
bg = pygame.image.load(f"assets/menu.png")
end = pygame.image.load(f"assets/thank_u.png")
photo_rect = button.get_rect()
photo_rect.center = (1280 // 2, 720 // 3)

window.blit(bg, (0,0))
window.blit(button, photo_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and photo_rect.collidepoint(event.pos):
         pygame.mixer.music.fadeout(500)
         time.sleep(0.5)
         LEVEL = [{  # design of each level, i - student row, j - student column, a - minimum speed, b - maximum speed
          "level": 1,
          "i": 4,
          "j": 6,
          "a": 9000,
          "b": 27000,
          "title": 'week 1'
         }, {
          "level": 2,
          "i": 2,
          "j": 6,
          "a": 6000,
          "b": 21000,
          "title": 'midterm'
         }, {
          "level": 3,
          "i": 1,
          "j": 6,
          "a": 6000,
          "b": 12000,
          "title": 'endterm'
         }
         ]

         lv1 = level_construct.main(LEVEL[0]["i"], LEVEL[0]["j"], LEVEL[0]["a"], LEVEL[0]["b"], LEVEL[0]["title"])
         time.sleep(3)
         lv2 = level_construct.main(LEVEL[1]["i"], LEVEL[1]["j"], LEVEL[1]["a"], LEVEL[1]["b"], LEVEL[1]["title"])
         time.sleep(3)
         lv3 = level_construct.main(LEVEL[2]["i"], LEVEL[2]["j"], LEVEL[2]["a"], LEVEL[2]["b"], LEVEL[2]["title"])
         window.blit(end, (0,0))
    pygame.display.update()

    