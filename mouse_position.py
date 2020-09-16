import pygame
import sys
from pygame.locals import *

WIDTH,HEIGHT=600,700

WHITE = (255,255,255)

pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption(" Finding Mouse Position Window")




def draw_window():

	WIN.fill(WHITE)
	pygame.display.update()

def mouse_pos():
	x,y = pygame.mouse.get_pos()
	return x,y


def main():
	FPS =30
	clock = pygame.time.Clock()
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				run =False
				pygame.quit()
				sys.exit()

			elif event.type ==MOUSEBUTTONDOWN:
				draw_window()
				posx,posy = mouse_pos()
				print(posx,posy)
		
		clock.tick(FPS)

main()