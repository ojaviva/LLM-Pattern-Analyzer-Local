---

## 👤 Autor

**Javier V**  
Especialista en Inteligencia Artificial aplicada y análisis narrativo estructurado.  

🔗 GitHub: https://github.com/ojaviva  
🔗 LinkedIn: (agrega aquí tu enlace)

Interesado en:
- LLMs locales
- Procesamiento masivo de texto
- Automatización de análisis narrativo
- IA aplicada al sector público y toma de decisiones


# 🧠 LLM-Pattern-Analyzer-Local

Pipeline simple de análisis de texto usando un LLM local (Llama 3.1 en LM Studio) para convertir texto no estructurado en información estructurada lista para análisis.

---

## 🚀 ¿Qué hace este proyecto?

Este proyecto demuestra cómo utilizar un modelo de lenguaje grande (LLM) ejecutándose localmente para:

- Clasificar textos en categorías  
- Asignar un nivel de riesgo  
- Generar un resumen estructurado  
- Exportar los resultados a un nuevo archivo CSV  

Convierte lenguaje natural en datos analizables sin usar APIs externas.

---

## 🏗 Arquitectura

```
CSV (textos)
    ↓
Python (pandas + requests)
    ↓
LM Studio (localhost)
    ↓
Llama 3.1 8B Instruct
    ↓
CSV enriquecido (output/results.csv)
```

---

## 📂 Estructura del proyecto

```
LLM-Pattern-Analyzer-Local/
│
├── data/
│   └── sample_texts.csv
│
├── output/
│   └── results.csv
│
├── src/
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10 o superior  
- LM Studio instalado  
- Modelo cargado: `meta-llama-3.1-8b-instruct`

---

## ▶️ Cómo ejecutarlo

1️⃣ Clonar el repositorio:

```
git clone https://github.com/ojaviva/LLM-Pattern-Analyzer-Local.git
cd LLM-Pattern-Analyzer-Local
```

2️⃣ Instalar dependencias:

```
pip install -r requirements.txt
```

3️⃣ Iniciar LM Studio y cargar el modelo.

4️⃣ Ejecutar el script:

```
python src/main.py
```

El archivo generado quedará en:

```
output/results.csv
```

---

## 🎯 ¿Qué demuestra?

- Uso práctico de LLM local  
- Extracción estructurada desde texto libre  
- Automatización básica de análisis narrativo  
- Primer paso hacia pipelines productivos con modelos open-source  

---

## 📌 Próximos pasos posibles

- Integrar validación automática  
- Agregar logging  
- Procesamiento masivo por lotes  
- Integración con dashboards  

---

Proyecto educativo y demostrativo.
