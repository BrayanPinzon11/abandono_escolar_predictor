
# Predicción de Abandono Escolar con Flask y Machine Learning

Este proyecto es una aplicación web construida con **Flask** que permite predecir si un estudiante abandonará la escuela o no, utilizando técnicas de aprendizaje automático (árbol de decisión) y un formulario amigable para el ingreso de datos.

## Descripción

La aplicación recibe datos personales, académicos y sociales del estudiante a través de un formulario. Luego, utiliza un modelo entrenado con un dataset real para predecir el riesgo de abandono escolar. Además, incluye visualizaciones gráficas para entender mejor las variables más influyentes.

## Tecnologías Usadas

- Python 3.x
- Flask
- Scikit-learn
- Matplotlib, Pandas
- TailwindCSS (interfaz web)
- CSV (para guardar y leer el dataset)

## Variables del Modelo

Algunas variables usadas para la predicción:

- Sexo, Edad, Dirección
- Educación de los padres
- Apoyo escolar, Actividades extracurriculares
- Notas G1, G2, G3
- Tiempo libre, Salidas, Salud
- Acceso a internet, Relaciones amorosas, etc.


## Instalación

1. Clona el repositorio:
   \`\`\`bash
   git clone https://github.com/tu_usuario/abandono_escolar_predictor.git
   cd abandono_escolar_predictor
   \`\`\`

2. Crea un entorno virtual (opcional pero recomendado):
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate   # En Linux/macOS
   venv\Scripts\activate    # En Windows
   \`\`\`

3. Instala las dependencias:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Ejecuta la aplicación:
   \`\`\`bash
   python app.py
   \`\`\`

5. Abre tu navegador en \`http://127.0.0.1:8080\`

## Visualizaciones

- Gráfico de distribución de abandono escolar
- Importancia de características para el modelo de predicción
- Modal emergente con resultados

## Licencia

MIT License - libre para usar y modificar.

---

Hecho con Python y Flask por Brayan Pinzon.
