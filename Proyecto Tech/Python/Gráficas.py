#   CÓDIGOS USADOS PARA LA GENERACIÓN DE LAS GRÁFICAS. 

# GRÁFICA DE ÁREA

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos de Colombia
df = pd.read_excel('02.xlsx', sheet_name='02 modern-renewable-energy-cons')
colombia = df[df['Entity'] == 'Colombia'].copy()

# Convertir la columna Year a numérico
colombia['Year'] = pd.to_numeric(colombia['Year'], errors='coerce')
colombia.dropna(subset=['Year'], inplace=True)

# Gráfico de área - Contribución acumulada
plt.figure(figsize=(10, 6))
plt.stackplot(colombia['Year'],
              colombia['Geo Biomass Other - TWh'],
              colombia['Solar Generation - TWh'],
              colombia['Wind Generation - TWh'],
              colombia['Hydro Generation - TWh'],
              labels=['Biomasa', 'Solar', 'Eólica', 'Hidroeléctrica'])
plt.title('Generación de energías renovables modernas en Colombia')
plt.xlabel('Año')
plt.ylabel('Generación (TWh)')
plt.legend(loc='upper left')
plt.show()





# GRÁFICO DE LÍNEAS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos completos
data = {
    'Año': [1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974,
            1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984,
            1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,
            1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
            2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
            2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Energía (TWh)': [3.54, 3.94, 4.39, 4.89, 5.44, 6.05, 6.42, 7.12, 7.74, 8.79,
                      9.73, 10.23, 10.45, 12.07, 13.26, 14.45, 14.27, 15.24, 15.37, 17.14,
                      18.44, 21.33, 23.25, 24.52, 26.78, 27.50, 27.73, 22.28, 27.86, 32.06,
                      31.99, 35.29, 31.48, 30.78, 33.70, 31.75, 31.48, 33.63, 35.81, 39.68,
                      39.40, 42.31, 44.00, 45.94, 40.64, 40.00, 48.39, 47.11, 49.76, 47.25,
                      47.94, 48.46, 60.64, 59.16, 52.98, 48.44, 58.19]
}

df = pd.DataFrame(data)

# Configuración del gráfico
plt.figure(figsize=(14, 7))

# Gráfico de LÍNEAS (cambio principal)
plt.plot(df['Año'], df['Energía (TWh)'],
         color='red',
         marker='o',
         linestyle='-',
         linewidth=2,
         markersize=6,
         markerfacecolor='white',
         markeredgecolor='black')

# Línea de tendencia (se mantiene igual)
z = np.polyfit(df['Año'], df['Energía (TWh)'], 1)
p = np.poly1d(z)
plt.plot(df['Año'], p(df['Año']), color='red', linewidth=2, linestyle='--',
         label=f'Tendencia: y = {z[0]:.3f}x + {z[1]:.1f}')

# Personalización (se mantiene igual)
plt.title('Consumo hidroeléctrico en Colombia (1965-2021).', fontsize=14, pad=20)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Electricidad (TWh)', fontsize=12)
plt.xticks(df['Año'][::5], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Destacar el valor máximo (adaptado para línea)
max_idx = df['Energía (TWh)'].idxmax()
plt.scatter(df['Año'][max_idx], df['Energía (TWh)'][max_idx],
            color='green',
            s=200,
            zorder=3,
            edgecolor='black',
            label='Máximo histórico')

plt.legend()  # Actualizar leyenda con el máximo
plt.tight_layout()
plt.show()




# GRÁFICO DE BARRAS / Solo se cambia el documento fuente de cada energía

import pandas as pd
import matplotlib.pyplot as plt

# Leer datos de Colombia
df = pd.read_excel('08 generación elóica.xlsx', sheet_name='08 wind-generation')
colombia = df[df['Entity'] == 'Colombia']

# Crear gráfica
plt.figure(figsize=(10, 5))
plt.bar(colombia['Year'], colombia['Electricity from wind (TWh)'], color='green')

# Personalizar
plt.title('Generación Eólica en Colombia (TWh)')
plt.xlabel('Año')
plt.ylabel('Electricidad Eólica (TWh)')
plt.grid(axis='y', linestyle='--')

plt.show()




#   GRÁFICO DE TORTA / Solo se cambia el documento fuente de cada energía

import pandas as pd
import matplotlib.pyplot as plt

# Leer datos y filtrar Colombia
df = pd.read_excel('04.xlsx')
colombia = df[df['Entity'] == 'Colombia']

# Configurar datos
years = colombia['Year'].astype(str)
porcentajes = colombia['Energías renovables (% electricidad)']

# Crear gráfico
plt.figure(figsize=(12, 8))
patches, texts, autotexts = plt.pie(porcentajes,
                                    labels=years,
                                    autopct='%1.1f%%',
                                    startangle=90,
                                    pctdistance=0.85,
                                    labeldistance=1.05)

# Mejorar legibilidad
plt.title('Distribución de Energías Renovables en Colombia por Año', pad=20)
plt.axis('equal')

# Ajustar etiquetas
[text.set_fontsize(8) for text in texts]
[autotext.set_fontsize(8) for autotext in autotexts]
plt.legend(patches, years,
           title='Años',
           loc='center left',
           bbox_to_anchor=(1, 0.5),
           fontsize=8)

plt.tight_layout()
plt.show()