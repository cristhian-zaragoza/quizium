# 🤝 Guía para contribuir a Quizium

¡Gracias por tu interés en mejorar **Quizium**! 🎉  
Este proyecto busca ser una herramienta educativa y divertida, abierta a la comunidad.  
Tu ayuda es bienvenida, ya sea con **ideas, correcciones, nuevas preguntas o mejoras en el código**.

---

## 📌 Cómo contribuir
1. **Haz un fork** de este repositorio.  
2. **Crea una rama** para tu contribución:  
   ```bash
   git checkout -b mi-contribucion

    Realiza los cambios que desees:

        Mejorar o corregir el código.

        Añadir nuevas preguntas en las categorías existentes.

        Crear nuevas categorías o niveles de dificultad.

        Mejorar la documentación o traducirla.

    Haz commit de tus cambios con un mensaje claro:

    git commit -m "Añadida nueva categoría de astronomía con 30 preguntas"

    Envía un Pull Request explicando el propósito de tu contribución.

📚 Estilo de preguntas

Si deseas agregar preguntas nuevas, sigue estas reglas:

    Cada categoría debe tener preguntas en tres niveles de dificultad (fácil, medio, difícil).

    Formato recomendado en questions.py:

    {
        "question": "¿Cuál es la fórmula del agua?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "answer": "H2O",
        "difficulty": "Fácil",
        "category": "Química"
    }

    Las respuestas deben ser claras y correctas.

    Evita preguntas ambiguas o con más de una respuesta válida.

🧪 Buenas prácticas de código

    Usa Python 3.8+.

    Nombra las funciones y variables en inglés, salvo las preguntas y textos (que pueden estar en español).

    Comenta el código cuando sea necesario para facilitar la comprensión.

    Antes de subir cambios, asegúrate de que el juego funciona en terminal sin errores.

🙌 Ideas de contribuciones

    Nuevas preguntas y categorías (ejemplo: Astronomía, Geología, Informática).

    Mejoras en los gráficos ASCII.

    Animaciones más elaboradas para el menú inicial.

    Traducciones (más idiomas).

    Soporte para exportar resultados a un archivo.

📜 Licencia

Al contribuir a este proyecto, aceptas que tus aportes se publiquen bajo la misma licencia MIT.