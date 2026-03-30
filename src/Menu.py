import sys
import os
import pygame
import pygame_gui

from .settings import WIDTH, HEIGHT, FPS, title


class Menu:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption(title)
		self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
		self.reloj = pygame.time.Clock()
		theme_path = os.path.abspath(
			os.path.join(os.path.dirname(__file__), "..", "Assets", "Fonts", "temas", "tema.json")
		)
		self.ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))
		font_path = os.path.abspath(
			os.path.join(os.path.dirname(__file__), "..", "Assets", "Fonts", "PressStart2P-Regular.ttf")
		)
		self.ui_manager.add_font_paths("Fuente_Principal", font_path)
		self.ui_manager.preload_fonts([
			{"name": "Fuente_Principal", "point_size": 20, "style": "regular", "antialiased": "1"}
		])
		self.ui_manager.get_theme().load_theme(theme_path)
		self.bg_color = (28, 30, 38)

		panel_rect = pygame.Rect(0, 0, 520, 360)
		panel_rect.center = (WIDTH // 2, HEIGHT // 2)

		self.panel = pygame_gui.elements.UIPanel(
			relative_rect=panel_rect,
			manager=self.ui_manager
		)

		self.title_label = pygame_gui.elements.UILabel(
			relative_rect=pygame.Rect((60, 42), (400, 56)),
			text="Simulacion Fisica",
			manager=self.ui_manager,
			container=self.panel
		)

		self.subtitle_label = pygame_gui.elements.UILabel(
			relative_rect=pygame.Rect((60, 98), (400, 36)),
			text="Click para seleccionar una opcion",
			manager=self.ui_manager,
			container=self.panel
		)

		self.play_button = pygame_gui.elements.UIButton(
			object_id="#play_button",
			relative_rect=pygame.Rect((145, 172), (230, 60)),
			text="Jugar",
			manager=self.ui_manager,
			container=self.panel
		)

		self.exit_button = pygame_gui.elements.UIButton(
			relative_rect=pygame.Rect((145, 252), (230, 60)),
			text="Salir",
			manager=self.ui_manager,
			container=self.panel
		)

	def run(self):
		while True:
			delta_time = self.reloj.tick(FPS) / 1000.0

			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_RETURN:
						return "play"
					if evento.key == pygame.K_ESCAPE:
						return "quit"

				if evento.type == pygame_gui.UI_BUTTON_PRESSED:
					if evento.ui_element == self.play_button:
						return "play"
					if evento.ui_element == self.exit_button:
						return "quit"

				self.ui_manager.process_events(evento)

			self.ui_manager.update(delta_time)

			self.pantalla.fill(self.bg_color)
			self.ui_manager.draw_ui(self.pantalla)
			pygame.display.flip()
