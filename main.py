import pygame
import sys

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 600))
BLUE = (100, 100, 240)
GREEN = (100, 240, 100)
input_filed = pygame.Rect(20, 20, 300, 50)
input_filed2 = pygame.Rect(20, 100, 300, 50)
font = pygame.font.Font(None, 32)
color = color2 = BLUE
text = ''
text2 = ''
active = False
active2 = False

class FlashCard:
    def __init__(self, term, meaning):
        self.term = term
        self.meaning = meaning


'''term = input('Введите термин')
meaning = input('Введите перевод')
new_par = FlashCard(term, meaning)
library = dict()
library[new_par.term] = new_par.meaning
print(library)'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_filed.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = GREEN if active else BLUE

            if input_filed2.collidepoint(event.pos):
                active2 = not active2
            else:
                active2 = False
            color2 = GREEN if active2 else BLUE

        if event.type == pygame.KEYDOWN:
            if active:
                '''if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:'''
                text += event.unicode
            if active2:
                '''if event.key == pygame.K_RETURN:
                    print(text2)
                    text2 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text2 = text2[:-1]
                else:'''
                text2 += event.unicode

    txt_surface = font.render(text, True, color)
    txt_surface2 = font.render(text2, True, color2)
    pygame.draw.rect(screen, color, input_filed, 2)
    pygame.draw.rect(screen, color2, input_filed2, 2)
    screen.fill((30, 30, 30))
    width = max(200, txt_surface.get_width() + 10)
    width2 = max(200, txt_surface2.get_width() + 10)
    input_filed.w = width
    input_filed2.w = width2
    screen.blit(txt_surface, (input_filed.x + 5, input_filed.y + 5))
    screen.blit(txt_surface2, (input_filed2.x + 5, input_filed2.y + 5))
    pygame.draw.rect(screen, color, input_filed, 2)
    pygame.draw.rect(screen, color2, input_filed2, 2)
    pygame.display.flip()
    clock.tick(30)
