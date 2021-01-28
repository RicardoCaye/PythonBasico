#%%
# Instalar dependencias para poder leer los archivos
# !pip install pandas
#%%
!pip install xlrd
#%%
import pandas as pd
import os
#%%

rutaScript = os.path.dirname(__file__)
"""
Guarda el archivo Excel en una carpeta que diga data, y esa carpeta
ponla en la misma carpeta donde guardes este archivo o script
"""
carpetaDondeEstanBases = 'data'
# Escribe el nombre de tu archivo entre las comillas
nombreArchivoExcel = 'Indicadores20210127211551.xls'

rutaBasesDeDatos = os.path.join(rutaScript,carpetaDondeEstanBases)
rutaArchivoExcel = os.path.join(rutaBasesDeDatos, nombreArchivoExcel)

# %%
# Cambia archivoExcel por el nombre que quieras usar
archivoExcel = pd.read_excel(rutaArchivoExcel)
print('¡Listo! Leíste correctamente tu archivo, es el siguiente')
archivoExcel
# %%
