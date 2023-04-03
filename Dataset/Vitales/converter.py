import os
import pandas as pd

# Establecer la ruta del directorio
directory_path = "./Dataset/Vitales"
archivos = ["Nacimientos", "DefuncionesFetales"]

# Iterar a través de cada carpeta de año
for year in range(2009, 2022):
    folder_name = str(year)
    folder_path = os.path.join(directory_path, folder_name)
    
    # Comprobar si la carpeta existe
    if os.path.exists(folder_path):

        # Iterar a través de cada archivo
        for archivo in archivos:

            # Obtener la ruta del archivo SPSS
            spss_file_path = os.path.join(folder_path, archivo+".sav")
            
            # Comprobar si el archivo SPSS existe
            if os.path.exists(spss_file_path):
                # Leer el archivo SPSS utilizando Pandas
                df = pd.read_spss(spss_file_path)
                
                # Convertir el archivo SPSS a CSV
                csv_file_path = os.path.join(folder_path, archivo+".csv")
                df.to_csv(csv_file_path, index=False)
