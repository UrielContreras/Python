# src/main_game.py
import pygame
import pymunk
import sys

from .settings import *


class MainGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        self.reloj = pygame.time.Clock()

        self.espacio = pymunk.Space()
        self.espacio.gravity = GRAVITY

        suelo_body = self.espacio.static_body
        self.suelo_shape = pymunk.Segment(suelo_body, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 5)
        self.suelo_shape.elasticity = 0.8
        self.suelo_shape.friction = 0.5
        self.espacio.add(self.suelo_shape)

        momento = pymunk.moment_for_circle(BALL_MASS, 0, BALL_RADIUS)
        self.cuerpo_pelota = pymunk.Body(BALL_MASS, momento)
        self.cuerpo_pelota.position = (WIDTH // 2, 100)
        self.forma_pelota = pymunk.Circle(self.cuerpo_pelota, BALL_RADIUS)
        self.forma_pelota.elasticity = 0.8
        self.forma_pelota.friction = 0.5
        self.espacio.add(self.cuerpo_pelota, self.forma_pelota)

    def _handle_events(self):
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    self.cuerpo_pelota.position = pos_mouse
                    self.cuerpo_pelota.velocity = (0, 0)
                    self.cuerpo_pelota.angular_velocity = 0

                if evento.button == 3:
                    self.cuerpo_pelota.apply_impulse_at_local_point((0, -500))

    def _draw(self):
        self.pantalla.fill(BG_COLOR)
        pygame.draw.line(self.pantalla, GROUND_COLOR, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 5)

        pos_p = self.cuerpo_pelota.position
        pygame.draw.circle(self.pantalla, BALL_COLOR, (int(pos_p.x), int(pos_p.y)), BALL_RADIUS)

        linea_fin = pos_p + pymunk.Vec2d(BALL_RADIUS, 0).rotated(self.cuerpo_pelota.angle)
        pygame.draw.line(self.pantalla, LINE_COLOR, (pos_p.x, pos_p.y), (linea_fin.x, linea_fin.y), 3)

    def run(self):
        while True:
            self._handle_events()
            self._draw()

            self.espacio.step(1 / FPS)
            pygame.display.flip()
            self.reloj.tick(FPS)