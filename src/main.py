"""
Proyecto: LLM-Pattern-Analyzer-Local
Autor: Javier V.
GitHub: https://github.com/ojaviva
Descripción:
Pipeline simple para analizar texto no estructurado usando un LLM local
(Llama 3.1 en LM Studio) y convertirlo en información estructurada.
"""

import pandas as pd
import requests
import json
import re

# ======================================
# Configuración de LM Studio
# ======================================

URL = "http://localhost:1234/v1/chat/completions"
MODELO = "meta-llama-3.1-8b-instruct"

# ======================================
# Función para limpiar JSON del modelo
# ======================================

def extraer_json(texto):

    texto = texto.replace("```json", "").replace("```", "")

    patron = r"\{.*\}"
    coincidencia = re.search(patron, texto, re.DOTALL)

    if coincidencia:
        return coincidencia.group()
    
    return None

# ======================================
# Función que consulta el modelo
# ======================================

def analizar_texto(texto):

    prompt = f"""
Analiza el siguiente texto y responde ÚNICAMENTE en JSON válido con estas claves:

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

    json_limpio = extraer_json(respuesta_modelo)

    try:
        resultado = json.loads(json_limpio)
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

    df = pd.read_csv("data/sample_texts.csv")

    resultados = []

    for _, fila in df.iterrows():

        analisis = analizar_texto(fila["texto"])

        resultados.append({
            "id": fila["id"],
            "texto": fila["texto"],
            "categoria": analisis.get("categoria"),
            "nivel_riesgo": analisis.get("nivel_riesgo"),
            "resumen": analisis.get("resumen")
        })

    df_resultado = pd.DataFrame(resultados)

    df_resultado.to_csv("output/results.csv", index=False)

    print("✅ Proceso finalizado.")
    print("📂 Archivo generado en: output/results.csv")


if __name__ == "__main__":
    main()
