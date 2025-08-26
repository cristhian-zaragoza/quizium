# leaderboard.py
# Guarda y muestra la clasificación de jugadores de forma robusta
# Autor: Christian Zaragoza
# Fecha: 2025-08-26

import json
from pathlib import Path
from utils.helpers import print_color

# Archivo donde se guardan los puntajes
LEADERBOARD_FILE = Path("data/leaderboard.json")

def load_scores():
    """
    Carga el archivo de puntuaciones. Si no existe, crea uno vacío.
    """
    if not LEADERBOARD_FILE.exists():
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_score(player, aciertos, errores, tiempo, attempts):
    """
    Guarda la puntuación de un jugador.
    
    Parámetros:
        player (str): Nombre del jugador
        aciertos (int)
        errores (int)
        tiempo (float): Tiempo en segundos
        attempts (int): Número de intentos
    """
    scores = load_scores()
    scores.append({
        "player": player,
        "aciertos": aciertos,
        "errores": errores,
        "tiempo": tiempo,
        "intentos": attempts
    })
    LEADERBOARD_FILE.parent.mkdir(exist_ok=True)
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def show_leaderboard():
    """
    Muestra la tabla de puntuaciones de todos los jugadores de manera segura.
    """
    scores = load_scores()
    if not scores:
        print_color("No hay puntuaciones aún. ¡Sé el primero en jugar!", "red")
        return
    
    # Ordenar por aciertos descendente y luego por menor tiempo
    scores.sort(key=lambda x: (-x['aciertos'], x['tiempo']))
    
    print_color("\n--- CLASIFICACIÓN ---", "cyan")
    print(f"{'Jugador':<15}{'Aciertos':<10}{'Errores':<10}{'Tiempo(s)':<12}{'Intentos':<10}")
    print("-"*60)
    for s in scores:
        print(f"{s['player']:<15}{s['aciertos']:<10}{s['errores']:<10}{s['tiempo']:<12}{s['intentos']:<10}")
