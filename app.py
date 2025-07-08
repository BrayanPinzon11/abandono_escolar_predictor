from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

# Cargar datos
df = pd.read_csv('data/Student_cleaned.csv', sep=';')

# Convertir booleanos tipo string a booleanos reales
df.replace({'True': True, 'False': False}, inplace=True)
df = df.dropna(subset=['abandona'])
df['abandona'] = df['abandona'].astype(int)

# Definir X y y
X = df.drop(columns=['abandona','G3','G2','G1'])  # Excluir columnas G3, G2, G1
y = df['abandona']

# Entrenar modelo
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    
    global df
    prediccion = None
    grafica = None
    grafica_importancia = None

    if request.method == 'POST':
        accion = request.form.get('accion')

        # Recolectar y procesar datos
        datos = {col: request.form[col] for col in X.columns}

        # Conversión de tipos
        for col in ['sex', 'address', 'Pstatus', 'guardian',
                    'age', 'Medu', 'Fedu', 'traveltime', 'studytime',
                    'failures', 'famrel', 'freetime', 'goout', 'Dalc',
                    'Walc', 'health', 'absences']:
            datos[col] = int(datos[col])

        for col in ['schoolsup', 'activities', 'higher', 'internet', 'romantic']:
            datos[col] = datos[col] == 'True'

        df_input = pd.DataFrame([datos])          # 1️⃣ sin 'abandona'

        if accion == 'predecir':
            prediccion = modelo.predict(df_input)[0]  # 2️⃣ predecir primero
            df_input['abandona'] = prediccion        # 3️⃣ añadir la columna objetivo

            # 4️⃣ guardar y unir
            df_input.to_csv('data/Student_cleaned1.csv',
                            sep=';', mode='a', header=False, index=False)
            df = pd.concat([df, df_input], ignore_index=True)

            # 5️⃣ reentrenar con X = df.drop('abandona', axis=1)
            modelo.fit(df.drop(columns=['abandona','G3','G2','G1']), df['abandona'])


        elif accion == 'ver_grafica':
            # Crear gráfica: porcentaje de abandono
            abandono = df['abandona'].value_counts(normalize=True) * 100
            etiquetas = ['No abandona', 'Abandona']
            colores = ['#4ade80', '#f87171']

            fig, ax = plt.subplots()
            ax.pie(abandono, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
            ax.axis('equal')

            # Convertir imagen a base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            buffer.close()
            grafica = imagen_base64

            importancias = modelo.feature_importances_
            nombres = X.columns
            indices = np.argsort(importancias)[::-1][:10]   # top‑10

            # 2. Graficar
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.barh(range(len(indices))[::-1],
                    importancias[indices][::-1], color='#60a5fa')
            ax.set_yticks(range(len(indices))[::-1])
            ax.set_yticklabels([nombres[i] for i in indices][::-1])
            ax.set_xlabel('Importancia')
            ax.set_title('Variables más influyentes')
            plt.tight_layout()

            # 3. Convertir a base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            grafica_importancia = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()

    return render_template('form.html',
                       prediccion=prediccion,
                       grafica=grafica,                # pastel abandono
                       grafica_importancia=grafica_importancia)

if __name__ == '__main__':
    app.run(debug=True)