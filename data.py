import pandas as pd
from random import choice, randint, seed
from datetime import datetime, timedelta

# Estableciendo una semilla para reproducibilidad
seed(42)

# Generando datos de muestra
num_employees = 300
ids = list(range(1, num_employees + 1))


# Fechas aleatorias para contratación y salida
def random_date(start, end):
    return start + timedelta(days=randint(0, (end - start).days))


start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 10, 30)

# Generando fechas de contratación y salida
hiring_dates = [random_date(start_date, end_date).strftime("%d de %B de %Y") for _ in range(num_employees)]
leaving_dates = [
    random_date(datetime.strptime(date, "%d de %B de %Y"), end_date).strftime("%d de %B de %Y") if choice(
        [True, False]) else ""
    for date in hiring_dates
]

# Estado basado en fechas de salida
statuses = ["Inactivo" if date else "Activo" for date in leaving_dates]

# Creando el DataFrame
data_large = {
    "id_empleado": ids,
    "fecha_contratacion": hiring_dates,
    "fecha_salida": leaving_dates,
    "estado": statuses
}

# Convertir los datos en un DataFrame
df_large = pd.DataFrame(data_large)

# Guardar el DataFrame en un archivo CSV
csv_file_large_path = r'C:\Users\jrsv\PycharmProjects\nueva prueba alfredo\femsa_empleados_large.csv'
df_large.to_csv(csv_file_large_path, index=False, encoding='utf-8-sig')
