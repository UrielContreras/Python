import sys
import pygame

from .settings import WIDTH, HEIGHT, FPS, title


class Menu:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption(title)
		self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
		self.reloj = pygame.time.Clock()

		self.font_titulo = pygame.font.SysFont("arial", 52, bold=True)
		self.font_texto = pygame.font.SysFont("arial", 28)

		self.bg_color = (28, 30, 38)
		self.panel_color = (41, 45, 57)
		self.play_color = (46, 204, 113)
		self.exit_color = (231, 76, 60)
		self.text_color = (245, 245, 245)

		self.play_rect = pygame.Rect(0, 0, 230, 60)
		self.exit_rect = pygame.Rect(0, 0, 230, 60)
		self.play_rect.center = (WIDTH // 2, HEIGHT // 2 + 15)
		self.exit_rect.center = (WIDTH // 2, HEIGHT // 2 + 95)

	def _draw(self):
		self.pantalla.fill(self.bg_color)

		panel = pygame.Rect(0, 0, 520, 360)
		panel.center = (WIDTH // 2, HEIGHT // 2)
		pygame.draw.rect(self.pantalla, self.panel_color, panel, border_radius=18)

		titulo = self.font_titulo.render("Simulacion Fisica", True, self.text_color)
		titulo_rect = titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 95))
		self.pantalla.blit(titulo, titulo_rect)

		subtitulo = self.font_texto.render("Click para seleccionar una opcion", True, self.text_color)
		subtitulo_rect = subtitulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 45))
		self.pantalla.blit(subtitulo, subtitulo_rect)

		pygame.draw.rect(self.pantalla, self.play_color, self.play_rect, border_radius=12)
		pygame.draw.rect(self.pantalla, self.exit_color, self.exit_rect, border_radius=12)

		play_text = self.font_texto.render("Jugar", True, (20, 20, 20))
		exit_text = self.font_texto.render("Salir", True, self.text_color)
		self.pantalla.blit(play_text, play_text.get_rect(center=self.play_rect.center))
		self.pantalla.blit(exit_text, exit_text.get_rect(center=self.exit_rect.center))

	def run(self):
		while True:
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_RETURN:
						return "play"
					if evento.key == pygame.K_ESCAPE:
						return "quit"

				if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
					if self.play_rect.collidepoint(evento.pos):
						return "play"
					if self.exit_rect.collidepoint(evento.pos):
						return "quit"

			self._draw()
			pygame.display.flip()
			self.reloj.tick(FPS)
