# quiz.py
# Contiene la lógica del juego: categorías, dificultad, preguntas y estadísticas
# Autor: Christian Zaragoza
# Fecha: 2025-08-26

import random
import time
from game.questions import QUESTIONS
from game.leaderboard import save_score
from utils.helpers import clear_screen, print_color

def start_quiz(player_name):
    """
    Inicia el quiz para el jugador.
    
    Parámetros:
        player_name (str): Nombre del jugador que está jugando.
    """
    try:
        while True:
            clear_screen()
            print_color(f"¡Hola {player_name}! Selecciona tu categoría:", "cyan")
            categories = list(QUESTIONS.keys())
            
            for idx, cat in enumerate(categories, 1):
                print(f"{idx}. {cat}")
            print(f"{len(categories)+1}. Salir")
            
            cat_choice = input("\nIngresa el número de la categoría: ")
            if not cat_choice.isdigit():
                print_color("Entrada inválida. Intenta de nuevo.", "red")
                input("Presiona Enter...")
                continue
            cat_choice = int(cat_choice)
            if cat_choice == len(categories)+1:
                break
            if cat_choice not in range(1, len(categories)+1):
                print_color("Categoría inválida.", "red")
                input("Presiona Enter...")
                continue
            
            category = categories[cat_choice-1]
            
            # Selección de dificultad
            print_color("\nSelecciona nivel de dificultad:", "cyan")
            difficulties = ["Fácil", "Medio", "Difícil"]
            for idx, diff in enumerate(difficulties, 1):
                print(f"{idx}. {diff}")
            print(f"{len(difficulties)+1}. Salir")
            
            diff_choice = input("\nIngresa el número del nivel: ")
            if not diff_choice.isdigit():
                print_color("Entrada inválida. Intenta de nuevo.", "red")
                input("Presiona Enter...")
                continue
            diff_choice = int(diff_choice)
            if diff_choice == len(difficulties)+1:
                break
            if diff_choice not in range(1, len(difficulties)+1):
                print_color("Dificultad inválida.", "red")
                input("Presiona Enter...")
                continue
            
            difficulty = difficulties[diff_choice-1]
            
            questions = QUESTIONS.get(category, {}).get(difficulty, [])
            if not questions:
                print_color("No hay preguntas disponibles en esta categoría/dificultad.", "red")
                input("Presiona Enter...")
                continue
            
            random.shuffle(questions)
            
            aciertos = 0
            errores = 0
            start_time = time.time()
            
            for idx, q in enumerate(questions, 1):
                clear_screen()
                print_color(f"{idx}. {q['question']}", "yellow")
                for i, opt in enumerate(q['options'], 1):
                    print(f"{i}. {opt}")
                
                ans = input("\nTu respuesta (1-4) o S para salir: ").strip()
                if ans.lower() == 's':
                    print_color("\nHas salido del quiz.", "magenta")
                    break
                if ans.isdigit() and int(ans) == q['answer']:
                    print_color("¡Correcto! ✅", "green")
                    aciertos += 1
                else:
                    correct_opt = q['options'][q['answer']-1]
                    print_color(f"Incorrecto ❌ La respuesta correcta era: {correct_opt}", "red")
                    errores += 1
                input("Presiona Enter para continuar...")
            
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            
            print_color(f"\nJuego terminado. Aciertos: {aciertos}, Errores: {errores}, Tiempo: {total_time} segundos", "magenta")
            
            # Guardar puntuación solo si respondió al menos una pregunta
            if aciertos + errores > 0:
                save_score(player_name, aciertos, errores, total_time, attempts=1)
            
            input("\nPresiona Enter para regresar al menú...")
            break  # Salir del loop del quiz después de completar o salir
    except KeyboardInterrupt:
        print_color("\nQuiz interrumpido. Regresando al menú...", "red")
        input("Presiona Enter...")
