# main.py
# Archivo principal del juego Quizium
# Muestra el menú inicial y dirige a jugar, ver clasificación o salir
# Autor: Christian Zaragoza
# Fecha: 2025-08-26

from game.quiz import start_quiz
from game.leaderboard import show_leaderboard
from assets.ascii_art import logo
from utils.helpers import clear_screen, print_color

def main():
    """
    Función principal que muestra el menú del juego.
    """
    while True:
        clear_screen()
        print(logo())  # Muestra el logo en ASCII
        print_color("Bienvenido a Quizium - ¡El Quiz de Ciencias Definitivo!\n", "cyan")
        print("1. Jugar")
        print("2. Clasificación")
        print("3. Salir")
        
        choice = input("\nSelecciona una opción (1-3): ")
        
        if choice == "1":
            player_name = input("\nIngresa tu nombre: ")
            start_quiz(player_name)
        elif choice == "2":
            show_leaderboard()
            input("\nPresiona Enter para regresar al menú...")
        elif choice == "3":
            print_color("\n¡Gracias por jugar Quizium! 👋", "green")
            break
        else:
            print_color("Opción inválida. Intenta de nuevo.", "red")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
