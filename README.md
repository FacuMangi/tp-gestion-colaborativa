# TP Gestión Colaborativa - Célula de Desarrollo Ágil

### Integrantes del Equipo
Facundo Mangioni

### Escenario Elegido
* **Escenario C**: Procesamiento Básico de Comentarios de Texto.

### Descripción del Dataset Utilizado
Se procesa un set de datos local en formato CSV (`dataset.csv`) que consolida reseñas y valoraciones de texto plano escritas por usuarios. El análisis extrae palabras clave y clasifica de forma heurística el sentido de la opinión.

### Instrucciones Básicas para Ejecutar el Script
1. Clonar el repositorio.
2. Incorporar el archivo de datos origen en la ruta relativa `datos/dataset.csv`.
3. Ejecutar el script analítico principal mediante:
   ```bash
   python scripts/analisis_datos.py
   ```
4. El reporte consolidado se imprimirá por consola y la métrica visual se exportará automáticamente a la ruta relativa `resultados/grafico_resultados.png`.
