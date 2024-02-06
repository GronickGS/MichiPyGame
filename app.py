import pygame
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO, ALTO = 300, 300
GROSOR_LINEA = 15
FILAS_TABLERO, COLUMNAS_TABLERO = 3, 3
TAMANO_CASILLA = ANCHO // COLUMNAS_TABLERO

# Colores
BLANCO = (255, 255, 255)
COLOR_LINEA = (23, 145, 135)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configurar la ventana del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Michi")
pantalla.fill(BLANCO)

# Tablero
tablero = [['' for _ in range(COLUMNAS_TABLERO)] for _ in range(FILAS_TABLERO)]


# Dibujar las líneas del tablero
def dibujar_lineas():
    # Líneas horizontales
    pygame.draw.line(pantalla, COLOR_LINEA, (0, TAMANO_CASILLA), (ANCHO, TAMANO_CASILLA), GROSOR_LINEA)
    pygame.draw.line(pantalla, COLOR_LINEA, (0, 2 * TAMANO_CASILLA), (ANCHO, 2 * TAMANO_CASILLA), GROSOR_LINEA)
    # Líneas verticales
    pygame.draw.line(pantalla, COLOR_LINEA, (TAMANO_CASILLA, 0), (TAMANO_CASILLA, ALTO), GROSOR_LINEA)
    pygame.draw.line(pantalla, COLOR_LINEA, (2 * TAMANO_CASILLA, 0), (2 * TAMANO_CASILLA, ALTO), GROSOR_LINEA)

# Dibujar el símbolo en el tablero
def dibujar_simbolos():
    for fila in range(FILAS_TABLERO):
        for columna in range(COLUMNAS_TABLERO):
            if tablero[fila][columna] == 'O':
                pygame.draw.circle(pantalla, ROJO, (int(columna * TAMANO_CASILLA + TAMANO_CASILLA / 2), int(fila * TAMANO_CASILLA + TAMANO_CASILLA / 2)), TAMANO_CASILLA // 4, 3)
            elif tablero[fila][columna] == 'X':
                pygame.draw.line(pantalla, VERDE, (columna * TAMANO_CASILLA + TAMANO_CASILLA // 4, fila * TAMANO_CASILLA + TAMANO_CASILLA // 4), 
                                                (columna * TAMANO_CASILLA + 3 * TAMANO_CASILLA // 4, fila * TAMANO_CASILLA + 3 * TAMANO_CASILLA // 4), 3)
                pygame.draw.line(pantalla, VERDE, (columna * TAMANO_CASILLA + TAMANO_CASILLA // 4, fila * TAMANO_CASILLA + 3 * TAMANO_CASILLA // 4), 
                                                (columna * TAMANO_CASILLA + 3 * TAMANO_CASILLA // 4, fila * TAMANO_CASILLA + TAMANO_CASILLA // 4), 3)

# Verificar si hay un ganador
def verificar_ganador():
    # Verificar filas
    for fila in range(FILAS_TABLERO):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != '':
            return tablero[fila][0]
    
    # Verificar columnas
    for columna in range(COLUMNAS_TABLERO):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != '':
            return tablero[0][columna]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]

    # Verificar empate
    if all(tablero[i][j] != '' for i in range(FILAS_TABLERO) for j in range(COLUMNAS_TABLERO)):
        return 'Empate'

    return None

# Dibujar el tablero
def dibujar_tablero():
    dibujar_lineas()
    dibujar_simbolos()
    pygame.display.update()

# Alternar entre jugadores
def cambiar_jugador(jugador):
    return 'X' if jugador == 'O' else 'O'

# Mostrar ventana de resultado
def mostrar_resultado(resultado):
    # Crear una nueva ventana para mostrar el resultado
    ventana_resultado = pygame.display.set_mode((ANCHO, ALTO))
    ventana_resultado.fill(BLANCO)

    fuente_resultado = pygame.font.Font(None, 36)
    texto_resultado = fuente_resultado.render(resultado, True, (0, 0, 0))
    rectangulo_resultado = texto_resultado.get_rect(center=(ANCHO // 2, ALTO // 2))

    fuente_boton = pygame.font.Font(None, 24)
    texto_jugar_otra_vez = fuente_boton.render('Jugar otra vez', True, (0, 0, 0))
    rectangulo_jugar_otra_vez = texto_jugar_otra_vez.get_rect(center=(ANCHO // 2, ALTO // 2 + 50))

    texto_salir = fuente_boton.render('Salir', True, (0, 0, 0))
    rectangulo_salir = texto_salir.get_rect(center=(ANCHO // 2, ALTO // 2 + 100))

    ventana_resultado.blit(texto_resultado, rectangulo_resultado)
    ventana_resultado.blit(texto_jugar_otra_vez, rectangulo_jugar_otra_vez)
    ventana_resultado.blit(texto_salir, rectangulo_salir)

    pygame.display.update()

    return rectangulo_jugar_otra_vez, rectangulo_salir

# Bucle principal
def main():
    jugador = 'O'
    corriendo = True
    resultado = None

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and resultado is None:
                mouseX = evento.pos[0] // TAMANO_CASILLA
                mouseY = evento.pos[1] // TAMANO_CASILLA

                if tablero[mouseY][mouseX] == '':
                    tablero[mouseY][mouseX] = jugador
                    jugador = cambiar_jugador(jugador)
        
        pantalla.fill(BLANCO)
        dibujar_tablero()
        resultado = verificar_ganador()

        if resultado is not None:
            if resultado == 'Empate':
                resultado = '¡Empate!'
            else:
                resultado = f'¡Ganó {resultado}!'
            jugar_otra_vez_rect, salir_rect = mostrar_resultado(resultado)
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if jugar_otra_vez_rect.collidepoint(evento.pos):
                            tablero.clear()
                            tablero.extend([['' for _ in range(COLUMNAS_TABLERO)] for _ in range(FILAS_TABLERO)])
                            main()
                        elif salir_rect.collidepoint(evento.pos):
                            pygame.quit()
                            sys.exit()
                    # Cambiar cursor al pasar por encima de los botones
                    if evento.type == pygame.MOUSEMOTION:
                        if jugar_otra_vez_rect.collidepoint(evento.pos) or salir_rect.collidepoint(evento.pos):
                            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                        else:
                            pygame.mouse.set_cursor(*pygame.cursors.arrow)

if __name__ == "__main__":
    main()
