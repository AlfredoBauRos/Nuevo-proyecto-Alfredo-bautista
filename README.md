# Nuevo-proyecto-Alfredo-bautista
KPIs automatizados de RH para rotación de personal.

Nuevo Proyecto Alfredo Bautista 🎉
Este proyecto genera, procesa, analiza y visualiza datos simulados de empleados para obtener KPIs clave de recursos humanos, tales como el tiempo promedio de contratación y la tasa de rotación de empleados. El proyecto se divide en dos etapas principales: la generación de datos simulados y el análisis y visualización de KPIs a partir de los datos generados. Este README explica cómo funciona el proyecto y cómo utilizar cada parte.

Tabla de Contenidos 📋
Descripción General
Requisitos Previos
Estructura del Proyecto
Explicación de Funcionalidades
Generación de Datos Simulados
Análisis y Visualización de KPIs
Uso
Ejemplo de Salida
Conclusión
Descripción General 🌟
"Nuevo Proyecto Alfredo Bautista" automatiza el análisis de datos de empleados para obtener métricas clave que apoyen la toma de decisiones en recursos humanos. El flujo de trabajo abarca desde la generación de un archivo CSV con datos simulados de empleados hasta el análisis de esos datos y la visualización de métricas en gráficos. Este enfoque permite explorar tendencias en la rotación de empleados y el tiempo promedio de contratación.

Requisitos Previos ⚙️
Para ejecutar el proyecto correctamente, se requiere tener instaladas las siguientes librerías:

Python 3.x
Pandas: Para la manipulación y análisis de datos.
Matplotlib: Para la visualización de datos.
Para instalar las dependencias, ejecutar el siguiente comando:

bash
Copiar código
pip install pandas matplotlib
Estructura del Proyecto 📁
graphql
Copiar código
nuevo_proyecto_alfredo_bautista/
│
├── generar_datos.py           # Script para generar el archivo CSV con datos simulados de empleados.
├── analizar_datos.py          # Script para cargar, analizar y visualizar los datos de empleados.
├── femsa_empleados_large.csv   # Archivo CSV generado (creado por generar_datos.py).
└── README.md                   # Documentación del proyecto.
generar_datos.py: Crea datos simulados de empleados con fechas de contratación, fechas de salida y estados (Activo/Inactivo) y guarda el resultado en femsa_empleados_large.csv.
analizar_datos.py: Carga el archivo CSV generado, convierte las fechas al formato adecuado, calcula KPIs de recursos humanos y visualiza los resultados en un gráfico de barras.
Explicación de Funcionalidades 🛠️
Generación de Datos Simulados
Establecimiento de Variables y Generación de Fechas Aleatorias:

Se generan 300 empleados con IDs únicos, fechas de contratación aleatorias entre 2020 y 2023, y, opcionalmente, fechas de salida para un subconjunto de empleados.
El estado de cada empleado se establece en "Activo" si no tiene fecha de salida, y en "Inactivo" si la tiene.
Exportación a CSV:

Los datos generados se guardan en el archivo femsa_empleados_large.csv en un formato listo para ser utilizado en el análisis.
Análisis y Visualización de KPIs
Carga y Conversión de Fechas:

Se lee el archivo femsa_empleados_large.csv, y se convierten las fechas de contratación y salida (en español) a un formato de fecha de pandas compatible.
Cálculo de KPIs:

Tiempo Promedio de Contratación: Calcula el tiempo promedio desde la primera contratación registrada hasta las contrataciones posteriores.
Tasa de Rotación: Calcula el porcentaje de empleados inactivos en comparación con el total de empleados.
Visualización:

Se genera un gráfico de barras con matplotlib para visualizar el tiempo promedio de contratación y la tasa de rotación de empleados.
Uso 🚀
Paso 1: Generar Datos Simulados
Ejecutar el script generar_datos.py para generar los datos simulados y guardarlos en el archivo CSV.

bash
Copiar código
python generar_datos.py
Este comando generará el archivo femsa_empleados_large.csv en la misma carpeta del proyecto.

Paso 2: Análisis y Visualización de los KPIs
Ejecutar el script analizar_datos.py para cargar el archivo CSV generado, calcular los KPIs y visualizar los resultados en un gráfico.

bash
Copiar código
python analizar_datos.py
El script imprimirá en la consola el tiempo promedio de contratación y la tasa de rotación, y mostrará un gráfico de barras con estos KPIs.

Ejemplo de Salida 💻
Salida en Consola
plaintext
Copiar código
Datos cargados:
   id_empleado fecha_contratacion fecha_salida     estado
0            1     01 de Enero de 2020  05 de Mayo de 2022  Inactivo
1            2     15 de Febrero de 2020                       
2            3     10 de Marzo de 2020  20 de Junio de 2021 Inactivo
...

Fechas después de la conversión:
   fecha_contratacion fecha_salida
0 2020-01-01 2022-05-05
1 2020-02-15 NaT
2 2020-03-10 2021-06-20
...

Número de fechas válidas de contratación: 300
Tiempo promedio de contratación: 250.33 días
Tasa de rotación de empleados: 42.00%
Gráfico de Barras
El gráfico de barras muestra los KPIs "Tiempo Promedio de Contratación" y "Tasa de Rotación" para los empleados.

Conclusión 📝
"Nuevo Proyecto Alfredo Bautista" es una herramienta útil para simular, analizar y visualizar datos de empleados en el contexto de recursos humanos. Los scripts ayudan a calcular métricas relevantes que pueden orientar la toma de decisiones en la gestión de talento, especialmente en lo que se refiere a la eficiencia de contratación y la retención de empleados.
