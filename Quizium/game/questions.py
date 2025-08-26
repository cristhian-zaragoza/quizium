# questions.py
# Contiene todas las preguntas del quiz organizadas por categoría y dificultad
# Autor: Christian Zaragoza
# Fecha: 2025-08-26


QUESTIONS = {
    "Biología": {
        "Fácil": [
            {"question": "¿Cuál es la molécula que contiene la información genética?", "options": ["ARN", "ADN", "Proteína", "Lípido"], "answer": 2},
            {"question": "¿Cuál es el órgano principal del sistema circulatorio?", "options": ["Hígado", "Corazón", "Pulmón", "Riñón"], "answer": 2},
            {"question": "Las plantas realizan fotosíntesis en:", "options": ["Raíz", "Hoja", "Tallo", "Flor"], "answer": 2},
            {"question": "El ser humano tiene cuántos pares de cromosomas?", "options": ["23", "46", "22", "44"], "answer": 1},
            {"question": "El oxígeno se transporta en la sangre gracias a:", "options": ["Hemoglobina", "Plasma", "Plaquetas", "Glucosa"], "answer": 1},
            {"question": "La célula procariota no tiene:", "options": ["Membrana plasmática", "Núcleo", "Ribosomas", "ADN"], "answer": 2},
            {"question": "El sistema que controla hormonas es:", "options": ["Digestivo", "Endocrino", "Circulatorio", "Nervioso"], "answer": 2},
            {"question": "El órgano donde ocurre la digestión de proteínas es:", "options": ["Estómago", "Intestino delgado", "Hígado", "Páncreas"], "answer": 1},
            {"question": "El corazón tiene cuántas cavidades?", "options": ["2", "3", "4", "5"], "answer": 3},
            {"question": "La fotosíntesis produce:", "options": ["CO2", "O2", "Nitrógeno", "Metano"], "answer": 2}
        ],
        "Medio": [
            {"question": "Las mitocondrias son responsables de:", "options": ["Fotosíntesis", "Respiración celular", "Síntesis de proteínas", "Almacenamiento de agua"], "answer": 2},
            {"question": "El ADN se encuentra en:", "options": ["Mitocondria", "Ribosoma", "Núcleo", "Cloroplasto"], "answer": 3},
            {"question": "La meiosis produce células:", "options": ["Diploides", "Haploides", "Somáticas", "Neuronas"], "answer": 2},
            {"question": "El grupo sanguíneo AB se clasifica como:", "options": ["Universal donante", "Universal receptor", "RH negativo", "RH positivo"], "answer": 2},
            {"question": "Los vertebrados poseen:", "options": ["Columna vertebral", "Exoesqueleto", "Antenas", "Caparazón"], "answer": 1},
            {"question": "La homeostasis regula:", "options": ["Equilibrio interno", "Movimiento", "Reproducción", "Fotosíntesis"], "answer": 1},
            {"question": "La clorofila está en:", "options": ["Cloroplasto", "Mitocondria", "Núcleo", "Ribosoma"], "answer": 1},
            {"question": "El sistema inmune produce:", "options": ["Hormonas", "Anticuerpos", "Enzimas digestivas", "ATP"], "answer": 2},
            {"question": "El hueso más largo del cuerpo humano es:", "options": ["Fémur", "Húmero", "Tibia", "Peroné"], "answer": 1},
            {"question": "El intestino delgado mide aproximadamente:", "options": ["3 metros", "6 metros", "1 metro", "10 metros"], "answer": 2}
        ],
        "Difícil": [
            {"question": "La Ley de Hardy-Weinberg describe:", "options": ["Equilibrio genético poblacional", "Fotosíntesis", "Respiración anaerobia", "Homeostasis"], "answer": 1},
            {"question": "El principal pigmento fotosintético es:", "options": ["Caroteno", "Clorofila a", "Xantofila", "Antocianina"], "answer": 2},
            {"question": "La primera fase de la mitosis es:", "options": ["Metafase", "Profase", "Anafase", "Telofase"], "answer": 2},
            {"question": "Las enzimas son:", "options": ["Carbohidratos", "Catalizadores biológicos", "Lípidos", "Vitaminas"], "answer": 2},
            {"question": "La osmolaridad se refiere a:", "options": ["Concentración de solutos", "Volumen de agua", "pH sanguíneo", "Presión arterial"], "answer": 1},
            {"question": "El ADN bacteriano suele ser:", "options": ["Lineal", "Circular", "Doble hélice simple", "Fragmentado"], "answer": 2},
            {"question": "La teoría endosimbiótica explica:", "options": ["Origen de mitocondrias y cloroplastos", "Origen de la vida", "Evolución de mamíferos", "Fotosíntesis"], "answer": 1},
            {"question": "La velocidad de reacción depende de:", "options": ["Temperatura", "Presión", "Color de la solución", "Forma del envase"], "answer": 1},
            {"question": "El ARN mensajero se sintetiza en:", "options": ["Citoplasma", "Núcleo", "Mitocondria", "Ribosoma"], "answer": 2},
            {"question": "La teoría celular establece que:", "options": ["Todas las células provienen de otras células", "Las células son inertes", "Solo los animales tienen células", "Las células no tienen membrana"], "answer": 1}
        ]
    },
    "Matemática": {
        "Fácil": [
            {"question": "¿Cuánto es 7 x 8?", "options": ["54", "56", "49", "64"], "answer": 2},
            {"question": "¿Cuál es el valor de π aproximado?", "options": ["3.14", "2.71", "1.62", "4.13"], "answer": 1},
            {"question": "El resultado de 12 + 15 es:", "options": ["27", "25", "28", "30"], "answer": 1},
            {"question": "¿Cuánto es 100 ÷ 4?", "options": ["20", "25", "30", "24"], "answer": 2},
            {"question": "Si sumas 5 + 7 + 3, obtienes:", "options": ["13", "15", "12", "10"], "answer": 2},
            {"question": "La mitad de 80 es:", "options": ["30", "40", "50", "35"], "answer": 2},
            {"question": "El doble de 23 es:", "options": ["46", "45", "44", "48"], "answer": 1},
            {"question": "El triple de 10 es:", "options": ["20", "30", "25", "40"], "answer": 2},
            {"question": "¿Cuánto es 9 x 9?", "options": ["81", "72", "91", "79"], "answer": 1},
            {"question": "Si restas 15 - 7, obtienes:", "options": ["8", "9", "7", "10"], "answer": 1}
        ],
        "Medio": [
            {"question": "¿Cuánto es 12²?", "options": ["144", "124", "132", "142"], "answer": 1},
            {"question": "¿Cuál es la raíz cuadrada de 225?", "options": ["15", "14", "12", "13"], "answer": 1},
            {"question": "Si x + 5 = 12, ¿x vale?", "options": ["6", "7", "8", "5"], "answer": 2},
            {"question": "Resuelve: 3x - 4 = 11", "options": ["5", "3", "7", "6"], "answer": 4},
            {"question": "¿Cuánto es 7² + 24²?", "options": ["625", "625", "576", "625"], "answer": 1},
            {"question": "El área de un triángulo base 10 y altura 5 es:", "options": ["50", "25", "15", "30"], "answer": 2},
            {"question": "La pendiente de y = 2x + 3 es:", "options": ["2", "3", "1", "0"], "answer": 1},
            {"question": "El valor de 2³ x 3² es:", "options": ["72", "36", "24", "48"], "answer": 1},
            {"question": "Si 5x = 20, x =", "options": ["2", "3", "4", "5"], "answer": 3},
            {"question": "El perímetro de un cuadrado lado 6 es:", "options": ["12", "18", "24", "36"], "answer": 3}
        ],
        "Difícil": [
            {"question": "Resuelve: 2x² - 8x + 6 = 0", "options": ["x=1 o x=3", "x=2 o x=1.5", "x=3 o x=2", "x=0 o x=3"], "answer": 1},
            {"question": "El logaritmo base 10 de 1000 es:", "options": ["3", "2", "4", "1"], "answer": 1},
            {"question": "El factorial de 5 es:", "options": ["120", "60", "24", "720"], "answer": 1},
            {"question": "Si f(x)=2x+1, f(3) =", "options": ["7", "6", "5", "8"], "answer": 1},
            {"question": "Resuelve: 3x - 7 = 2x + 5", "options": ["x=12", "x=10", "x=-12", "x=-10"], "answer": 1},
            {"question": "¿Cuánto es 2⁵ x 2³?", "options": ["256", "32", "64", "128"], "answer": 4},
            {"question": "Área de un círculo radio 7:", "options": ["154", "49", "44", "100"], "answer": 1},
            {"question": "Si x²=49, x=", "options": ["7 o -7", "7", "-7", "14"], "answer": 1},
            {"question": "La media de 2,4,6,8,10 es:", "options": ["6", "5", "4", "7"], "answer": 1},
            {"question": "Resuelve: 5(x-2)=15", "options": ["x=5", "x=3", "x=4", "x=6"], "answer": 1}
        ]
    }
}
