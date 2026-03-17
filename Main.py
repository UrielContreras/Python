import pygame
import pymunk
import sys

# --- Configuración de Ventana ---
pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

# --- Espacio de Física ---
espacio = pymunk.Space()
espacio.gravity = (0, 900)

# Suelo (Cuerpo estático)
suelo_body = espacio.static_body 
suelo_shape = pymunk.Segment(suelo_body, (0, alto - 50), (ancho, alto - 50), 5)
suelo_shape.elasticity = 0.8
suelo_shape.friction = 0.5
espacio.add(suelo_shape)

# Pelota (Cuerpo dinámico)
masa = 1
radio = 25
momento = pymunk.moment_for_circle(masa, 0, radio)
cuerpo_pelota = pymunk.Body(masa, momento)
cuerpo_pelota.position = (400, 100)
forma_pelota = pymunk.Circle(cuerpo_pelota, radio)
forma_pelota.elasticity = 0.8
forma_pelota.friction = 0.5
espacio.add(cuerpo_pelota, forma_pelota)

# --- Bucle Principal ---
while True:
    pos_mouse = pygame.mouse.get_pos() # Obtener posición (x, y) del mouse
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # INTERACCIÓN CON EL MOUSE
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # CLICK IZQUIERDO (Botón 1): Mover la pelota al mouse
            if evento.button == 1: 
                cuerpo_pelota.position = pos_mouse
                cuerpo_pelota.velocity = (0, 0) # Detener la caída actual
                cuerpo_pelota.angular_velocity = 0 # Detener la rotación
            
            # CLICK DERECHO (Botón 3): Dar un impulso hacia arriba
            if evento.button == 3:
                # apply_impulse_at_local_point(fuerza_x, fuerza_y)
                cuerpo_pelota.apply_impulse_at_local_point((0, -500))

    # --- Lógica de Dibujo ---
    pantalla.fill((240, 240, 240)) # Fondo claro

    # Dibujar Suelo
    pygame.draw.line(pantalla, (50, 50, 50), (0, alto - 50), (ancho, alto - 50), 5)

    # Dibujar Pelota
    pos_p = cuerpo_pelota.position
    # Usamos el ángulo del cuerpo para dibujar una línea de referencia y ver cómo rueda
    pygame.draw.circle(pantalla, (46, 204, 113), (int(pos_p.x), int(pos_p.y)), radio)
    
    # Línea decorativa para ver la rotación
    linea_fin = pos_p + pymunk.Vec2d(radio, 0).rotated(cuerpo_pelota.angle)
    pygame.draw.line(pantalla, (255, 255, 255), (pos_p.x, pos_p.y), (linea_fin.x, linea_fin.y), 3)

    # Actualizar Física
    espacio.step(1/60.0)
    pygame.display.flip()
    reloj.tick(60)