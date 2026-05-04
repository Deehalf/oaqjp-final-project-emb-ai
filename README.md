# Final project

Este proyecto implementa un servicio de detección de emociones basado en el modelo EmotionPredict de IBM Watson, utilizando una arquitectura simple en Python. El sistema recibe un texto como entrada, lo envía a la API de análisis emocional y devuelve los puntajes asociados a cinco emociones principales:

Anger

Disgust

Fear

Joy

Sadness

El proyecto incluye:

Una función principal emotion_detector() que:

Envía solicitudes a la API de IBM Watson.

Procesa la respuesta JSON.

Extrae los valores de cada emoción.

Determina la emoción dominante.

Maneja errores HTTP (400, 500 y otros) devolviendo valores por defecto.

Un servidor Flask (server.py) que expone un endpoint /emotionDetector para consumir el servicio desde un navegador o cliente HTTP.

Manejo robusto de errores para asegurar que el servicio siempre responda con una estructura válida, incluso cuando la API externa falle.

Este proyecto demuestra el uso de procesamiento de lenguaje natural, consumo de APIs externas, manejo de JSON, y construcción de un servicio web básico en Python.
