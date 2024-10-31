import pandas as pd
import matplotlib.pyplot as plt


# Función para convertir cadenas a fechas en el formato específico
def convertir_fecha(fecha_str):
    if isinstance(fecha_str, str):  # Verifica que la fecha sea una cadena
        # Reemplazar los nombres de meses en español a inglés
        meses_es = {
            'Enero': 'January', 'Febrero': 'February', 'Marzo': 'March',
            'Abril': 'April', 'Mayo': 'May', 'Junio': 'June',
            'Julio': 'July', 'Agosto': 'August', 'Septiembre': 'September',
            'Octubre': 'October', 'Noviembre': 'November', 'Diciembre': 'December'
        }

        for mes_es, mes_en in meses_es.items():
            fecha_str = fecha_str.replace(mes_es, mes_en)

        # Convertir la cadena a fecha
        return pd.to_datetime(fecha_str, format='%d de %B de %Y', errors='coerce')
    return pd.NaT  # Devuelve NaT si no es una cadena


# Cargar datos desde un archivo CSV
def cargar_datos():
    df = pd.read_csv(r'C:\Users\jrsv\PycharmProjects\nueva prueba alfredo\femsa_empleados_large.csv')

    # Imprimir las primeras filas del DataFrame
    print("Datos cargados:")
    print(df.head())

    # Convertir columnas a formato de fecha
    df['fecha_contratacion'] = df['fecha_contratacion'].apply(convertir_fecha)
    df['fecha_salida'] = df['fecha_salida'].apply(convertir_fecha)

    # Imprimir los datos de las fechas
    print("\nFechas después de la conversión:")
    print(df[['fecha_contratacion', 'fecha_salida']].head())

    return df


# Calcular tiempo promedio de contratación (en días)
def calcular_tiempo_promedio_contratacion(df):
    df_contratados = df.dropna(subset=['fecha_contratacion'])
    print(f"\nNúmero de fechas válidas de contratación: {len(df_contratados)}")

    if not df_contratados.empty:
        tiempos_contratacion = (
                    df_contratados['fecha_contratacion'] - df_contratados['fecha_contratacion'].min()).dt.days
        tiempo_promedio = tiempos_contratacion.mean()
        print(f"Tiempo promedio de contratación: {tiempo_promedio:.2f} días")
    else:
        tiempo_promedio = float('nan')
        print("No hay fechas válidas para calcular el tiempo promedio de contratación.")

    return tiempo_promedio


# Calcular tasa de rotación de empleados
def calcular_rotacion_empleados(df):
    total_empleados = len(df)
    empleados_inactivos = df[df['estado'] == 'Inactivo'].shape[0]
    tasa_rotacion = (empleados_inactivos / total_empleados) * 100
    print(f"Tasa de rotación de empleados: {tasa_rotacion:.2f}%")
    return tasa_rotacion


# Visualizar resultados en un gráfico de barras
def generar_grafico_kpis(tiempo_promedio, rotacion):
    plt.figure(figsize=(8, 5))
    kpis = ['Tiempo Promedio de Contratación', 'Tasa de Rotación']
    valores = [tiempo_promedio, rotacion]

    plt.bar(kpis, valores, color=['blue', 'orange'])
    plt.title('KPIs de Recursos Humanos')
    plt.ylabel('Valor')
    plt.xticks(rotation=15)
    plt.tight_layout()  # Ajustar el diseño para evitar solapamiento
    plt.show()


# Ejecutar la automatización de KPIs
def main():
    df = cargar_datos()  # Cargar datos
    tiempo_promedio_contratacion = calcular_tiempo_promedio_contratacion(df)  # Calcular tiempo promedio
    tasa_rotacion = calcular_rotacion_empleados(df)  # Calcular tasa de rotación
    generar_grafico_kpis(tiempo_promedio_contratacion, tasa_rotacion)  # Generar gráfico


if __name__ == "__main__":
    main()
