import arcpy

def subdividir_arreglo_y_retornar(arr_unidimensional):
    longitud = len(arr_unidimensional)
    raiz_cuadrada = int(longitud ** 0.5)
    
    filas = raiz_cuadrada
    columnas = raiz_cuadrada
    
    #Ajusta las filas para dividir el arreglo
    while filas * columnas < longitud:
        columnas += 1
        if filas * columnas >= longitud:
            break
    
    # divide el arreglo
    arr_multidimensional = [arr_unidimensional[i:i+columnas] for i in range(0, len(arr_unidimensional), columnas)]
    
    #variable que almacena los datos
    resultado = ""
    
    #hace recorrido de todas las filas
    for i in range(filas):
        
        if i % 2 == 0:
            for j in range(min(columnas, len(arr_multidimensional[i]))):
                resultado += str(arr_multidimensional[i][j]) + " "
        
        else:
            for j in range(min(columnas, len(arr_multidimensional[i])) - 1, -1, -1): 
                resultado += str(arr_multidimensional[i][j]) + " "
    
    return resultado.rstrip()

# Define el arreglo unidimensional
arr_unidimensional = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Llama a la función para obtener el resultado


# Define la ruta de la capa de datos
capa = arcpy.GetParameterAsText(0)

# Define el campo donde deseas realizar el cálculo
campo_a_alinear = arcpy.GetParameterAsText(1)

campo_requerido = arcpy.GetParameterAsText(2)

arr = []

arr.append(campo_a_alinear)

resultado = subdividir_arreglo_y_retornar(arr)

# Usa Calculate Field para asignar el resultado al campo especificado
#arcpy.CalculateField_management(capa, campo_requerido, '"' + resultado + '"', "PYTHON")
