import pandas as pd
import requests
import json

# ======================================
# Configuración de LM Studio
# ======================================

URL = "http://localhost:1234/v1/chat/completions"
MODELO = "meta-llama-3.1-8b-instruct"

# ======================================
# Función que consulta el modelo local
# ======================================

def analizar_texto(texto):

    prompt = f"""
Analiza el siguiente texto y responde SOLO en formato JSON válido con estas claves:

- categoria (Soporte, Seguridad, Información, Facturación, Otro)
- nivel_riesgo (Bajo, Medio, Alto)
- resumen (máximo 20 palabras)

Texto:
{texto}
"""

    payload = {
        "model": MODELO,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(URL, json=payload)
    respuesta_modelo = response.json()["choices"][0]["message"]["content"]

    try:
        resultado = json.loads(respuesta_modelo)
    except:
        resultado = {
            "categoria": "Error",
            "nivel_riesgo": "Error",
            "resumen": "No se pudo procesar"
        }

    return resultado

# ======================================
# Proceso principal
# ======================================

def main():

    # Cargar archivo de entrada
    df = pd.read_csv("data/sample_texts.csv")

    resultados = []

    # Iterar cada texto
    for _, fila in df.iterrows():

        analisis = analizar_texto(fila["texto"])

        resultados.append({
            "id": fila["id"],
            "texto": fila["texto"],
            "categoria": analisis["categoria"],
            "nivel_riesgo": analisis["nivel_riesgo"],
            "resumen": analisis["resumen"]
        })

    # Crear DataFrame de salida
    df_resultado = pd.DataFrame(resultados)

    # Guardar resultado
    df_resultado.to_csv("output/results.csv", index=False)

    print("✅ Proceso finalizado.")
    print("📂 Archivo generado en: output/results.csv")


if __name__ == "__main__":
    main()

