import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def ejecutar_analisis():
    # -------------------------------------------------------------------------
    # 1. CARGA DE DATOS MEDIANTE RUTAS RELATIVAS
    # Se define la ruta relativa para asegurar la portabilidad del script en Colab,
    # evitando dependencias de la estructura de directorios del sistema operativo local.
    # -------------------------------------------------------------------------
    ruta_entrada = os.path.join("datos", "dataset.csv")
    ruta_grafico = os.path.join("resultados", "grafico_resultados.png")
    
    if not os.path.exists(ruta_entrada):
        raise FileNotFoundError(f"Error crítico: No se encontró el archivo en {ruta_entrada}")
        
    df = pd.read_csv(ruta_entrada)
    df['texto_limpio'] = df['text'].astype(str).str.lower()

    # -------------------------------------------------------------------------
    # 2. CALCULO DE FRECUENCIA DE PALABRAS (PROCESAMIENTO DE TEXTO)
    # Excluimos palabras vacías comunes (stopwords) de forma manual y simple 
    # para evitar falsos positivos en palabras de alta frecuencia sin valor semántico.
    # -------------------------------------------------------------------------
    stopwords = {'the', 'and', 'a', 'to', 'of', 'is', 'i', 'in', 'it', 'this', 'for', 'with', 'was', 'but'}
    todas_las_palabras = []
    
    for texto in df['texto_limpio']:
        palabras = re.findall(r'\b\w+\b', texto)
        palabras_filtradas = [p for p in palabras if p not in stopwords and len(p) > 2]
        todas_las_palabras.extend(palabras_filtradas)
        
    frecuencia_palabras = Counter(todas_las_palabras)
    palabras_comunes = frecuencia_palabras.most_common(10)

    # -------------------------------------------------------------------------
    # 3. ANÁLISIS DE SENTIMIENTO SIMPLIFICADO POR PALABRAS CLAVE
    # Implementamos un clasificador heurístico basado en diccionarios explícitos.
    # Se justifica este enfoque debido a que no requiere dependencias pesadas de NLP,
    # optimizando el tiempo de cómputo en entornos distribuidos efímeros.
    # -------------------------------------------------------------------------
    palabras_positivas = {'good', 'great', 'excellent', 'love', 'best', 'nice', 'awesome', 'amazing'}
    palabras_negativas = {'bad', 'worst', 'poor', 'terrible', 'hate', 'disappointed', 'horrible', 'slow'}
    
    def clasificar_comentario(texto):
        palabras = set(re.findall(r'\b\w+\b', text=texto))
        score_pos = len(palabras.intersection(palabras_positivas))
        score_neg = len(palabras.intersection(palabras_negativas))
        
        if score_pos > score_neg:
            return "Positivo"
        elif score_neg > score_pos:
            return "Negativo"
        return "Neutral"
        
    df['sentimiento'] = df['texto_limpio'].apply(clasificar_comentario)
    conteo_sentimientos = df['sentimiento'].value_counts()

    # -------------------------------------------------------------------------
    # 4. GENERACIÓN DEL INFORME VISUAL Y GRÁFICO
    # El gráfico se exporta directamente a la carpeta local /resultados usando rutas relativas.
    # -------------------------------------------------------------------------
    plt.figure(figsize=(6, 4))
    conteo_sentimientos.plot(kind='bar', color=['#4CAF50', '#F44336', '#757575'])
    plt.title("Distribución de Sentimientos en Comentarios")
    plt.xlabel("Categoría de Sentimiento")
    plt.ylabel("Cantidad de Reseñas")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(ruta_grafico)
    plt.close()
    
    # -------------------------------------------------------------------------
    # 5. INFORME EN CONSOLA
    # -------------------------------------------------------------------------
    print("==================================================")
    print("         INFORME TÉCNICO DE RESULTADOS            ")
    print("==================================================")
    print(f"Total de registros procesados: {len(df)}")
    print("\nDistribución de Sentimientos:")
    print(conteo_sentimientos.to_string())
    print("\nPalabras más utilizadas (Top 5):")
    for palabra, frec in palabras_comunes[:5]:
        print(f" - {palabra}: {frec} veces")
    print("==================================================")

if __name__ == "__main__":
    ejecutar_analisis()
