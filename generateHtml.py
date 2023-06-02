import openpyxl

def generate(archivo_excel, columna, archivo_html):
    # Abrir el archivo Excel
    libro = openpyxl.load_workbook(archivo_excel)
    hoja = libro.active
    
    # Obtener los datos de la columna especificada
    datos_columna = [celda.value for celda in hoja[columna]]
    
    # Crear el archivo HTML
    with open(archivo_html, 'w') as archivo:
        archivo.write('<html>\n')
        archivo.write('<body>\n')
        
        # Generar los enlaces
        for dato in datos_columna:
            if dato is not None:
                archivo.write(f'<a href="{dato}">{dato}</a>\n')
        
        archivo.write('</body>\n')
        archivo.write('</html>\n')

# Ejemplo de uso
generate('datos.xlsx', 'A', 'enlaces.html')
