import pygame
import os
import sys

pygame.init()

clock = pygame.time.Clock()
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snail Race')

TITLE = pygame.font.SysFont('Courier', 50)
WINNER_FONT = pygame.font.SysFont('Courier', 70)

VELOCITY = 10

SNAIL1_WON = pygame.USEREVENT + 1
SNAIL2_WON = pygame.USEREVENT + 2
SNAIL3_WON = pygame.USEREVENT + 3
SNAIL4_WON = pygame.USEREVENT + 4

RACE_BG_WIDTH, RACE_BG_HEIGHT = 700, 400
FINISH_LINE_WIDTH, FINISH_LINE_HEIGHT = 400, 400
SNAIL_WIDTH, SNAIL_HEIGHT = 75, 75

RACE_BG_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\green bg.jpg'))
RACE_BG = pygame.transform.scale(
    RACE_BG_IMAGE, (RACE_BG_WIDTH, RACE_BG_HEIGHT))

FINISH_LINE_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\finish line.png'))
FINISH_LINE = pygame.transform.rotate(pygame.transform.scale(
    FINISH_LINE_IMAGE, (FINISH_LINE_WIDTH, FINISH_LINE_HEIGHT)), 90)

SNAIL1_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\snail1.png'))
SNAIL1 = pygame.transform.scale(SNAIL1_IMAGE, (SNAIL_WIDTH, SNAIL_HEIGHT))

SNAIL2_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\snail2.png'))
SNAIL2 = pygame.transform.scale(SNAIL2_IMAGE, (SNAIL_WIDTH, SNAIL_HEIGHT))

SNAIL3_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\snail3.png'))
SNAIL3 = pygame.transform.scale(SNAIL3_IMAGE, (SNAIL_WIDTH, SNAIL_HEIGHT))

SNAIL4_IMAGE = pygame.image.load(os.path.join(
    r'C:\Users\bayar\OneDrive\Desktop\Techne club\Neelttei haalga\Games\Snail game\Assets\snail4.png'))
SNAIL4 = pygame.transform.scale(SNAIL4_IMAGE, (SNAIL_WIDTH, SNAIL_HEIGHT))


FPS = 60
PINK = (255, 192, 203)
ORANGE = (255, 69, 0)
BLACK = (0, 0, 0)


def draw_window(snail1, snail2, snail3, snail4):
    WIN.fill(PINK)
    WIN.blit(TITLE.render('Snail Race', 1, ORANGE), (320, 30))

    WIN.blit(RACE_BG, (100, 100))
    WIN.blit(FINISH_LINE, (575, 100))
    WIN.blit(SNAIL1, (snail1.x, snail1.y))
    WIN.blit(SNAIL2, (snail2.x, snail2.y))
    WIN.blit(SNAIL3, (snail3.x, snail3.y))
    WIN.blit(SNAIL4, (snail4.x, snail4.y))

    pygame.draw.line(WIN, BLACK, (200, 100), (200, 500), width=2)
    pygame.draw.line(WIN, BLACK, (100, 200), (750, 200), width=2)
    pygame.draw.line(WIN, BLACK, (100, 300), (750, 300), width=2)
    pygame.draw.line(WIN, BLACK, (100, 400), (750, 400), width=2)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, ORANGE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
             2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    snail1 = pygame.Rect(110, 110, SNAIL_WIDTH, SNAIL_HEIGHT)
    snail2 = pygame.Rect(110, 210, SNAIL_WIDTH, SNAIL_HEIGHT)
    snail3 = pygame.Rect(110, 310, SNAIL_WIDTH, SNAIL_HEIGHT)
    snail4 = pygame.Rect(110, 410, SNAIL_WIDTH, SNAIL_HEIGHT)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and snail1.x + VELOCITY < 710:
                    snail1.x += VELOCITY
                    if snail1.x >= 700:
                        pygame.event.post(pygame.event.Event(SNAIL1_WON))
                elif event.key == pygame.K_f and snail2.x + VELOCITY < 710:
                    snail2.x += VELOCITY
                    if snail2.x >= 700:
                        pygame.event.post(pygame.event.Event(SNAIL2_WON))
                elif event.key == pygame.K_j and snail3.x + VELOCITY < 710:
                    snail3.x += VELOCITY
                    if snail3.x >= 700:
                        pygame.event.post(pygame.event.Event(SNAIL3_WON))
                elif event.key == pygame.K_l and snail4.x + VELOCITY < 710:
                    snail4.x += VELOCITY
                    if snail4.x >= 700:
                        pygame.event.post(pygame.event.Event(SNAIL4_WON))

            winner_text = ''
            if event.type == SNAIL1_WON:
                winner_text = 'Yellow Snail Won!'
                snail1.x, snail1.y = 110, 110
                snail2.x, snail2.y = 110, 210
                snail3.x, snail3.y = 110, 310
                snail4.x, snail4.y = 110, 410
            if event.type == SNAIL2_WON:
                winner_text = 'Blue Snail Won!'
                snail1.x, snail1.y = 110, 110
                snail2.x, snail2.y = 110, 210
                snail3.x, snail3.y = 110, 310
                snail4.x, snail4.y = 110, 410
            if event.type == SNAIL3_WON:
                winner_text = 'Green Snail Won!'
                snail1.x, snail1.y = 110, 110
                snail2.x, snail2.y = 110, 210
                snail3.x, snail3.y = 110, 310
                snail4.x, snail4.y = 110, 410
            if event.type == SNAIL4_WON:
                winner_text = 'Red Snail Won!'
                snail1.x, snail1.y = 110, 110
                snail2.x, snail2.y = 110, 210
                snail3.x, snail3.y = 110, 310
                snail4.x, snail4.y = 110, 410

            if winner_text != '':
                draw_winner(winner_text)

        draw_window(snail1, snail2, snail3, snail4)
    main()


if __name__ == '__main__':
    main()
