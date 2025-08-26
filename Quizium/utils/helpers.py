# helpers.py
# Funciones de utilidad: limpiar pantalla, colores, temporizador, etc
# Autor: Christian Zaragoza
# Fecha: 2025-08-26

import os

# Colores simples para terminal
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m"
}

def clear_screen():
    """
    Limpia la pantalla de la terminal según el sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_color(text, color):
    """
    Imprime texto en un color específico en la terminal.
    
    Parámetros:
        text (str): Texto a imprimir
        color (str): Nombre del color (red, green, yellow, blue, magenta, cyan)
    """
    print(f"{COLORS.get(color,'')}{text}{COLORS['reset']}")
