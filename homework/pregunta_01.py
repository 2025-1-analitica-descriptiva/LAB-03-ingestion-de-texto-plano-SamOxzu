"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel



"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

import pandas as pd
import re

def pregunta_01():
    # Leer el archivo
    with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Procesar nombres de columnas
    headers = ' '.join(lines[0:2]).replace('\n', ' ').strip()
    column_names = [
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ]

    # Inicializar listas para datos
    data = {name: [] for name in column_names}
    
    # Procesar líneas relevantes (omitir encabezado y líneas vacías)
    current_text = ''
    for line in lines[4:]:
        if '---' in line or not line.strip():
            continue
            
        # Si la línea comienza con un número, es una nueva entrada
        if re.match(r'\s*\d+\s+\d+', line):
            if current_text:
                # Procesar el texto acumulado anterior
                data['principales_palabras_clave'].append(current_text.strip())
            current_text = ''
            
            # Extraer datos numéricos
            parts = line.split()
            data['cluster'].append(int(parts[0]))
            data['cantidad_de_palabras_clave'].append(int(parts[1]))
            data['porcentaje_de_palabras_clave'].append(float(parts[2].replace(',', '.')))
            current_text = ' '.join(parts[4:])
        else:
            # Continuar acumulando texto de palabras clave
            current_text += ' ' + line.strip()
    
    # Añadir el último grupo de palabras clave
    if current_text:
        data['principales_palabras_clave'].append(current_text.strip())

    # Procesar palabras clave
    cleaned_keywords = []
    for text in data['principales_palabras_clave']:
        # Limpiar y formatear el texto
        cleaned_text = re.sub(r'\s+', ' ', text).strip().rstrip('.')
        # Dividir por comas y limpiar cada palabra
        keywords = [word.strip() for word in cleaned_text.split(',')]
        # Unir con coma y espacio
        cleaned_keywords.append(', '.join(keywords))
    
    data['principales_palabras_clave'] = cleaned_keywords

    # Crear DataFrame
    df = pd.DataFrame(data)
    
    return df