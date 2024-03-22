from osgeo import gdal
import os
def convertir_geotiff_a_ecw(archivos_entrada, carpeta_salida):
    try:
        for entrada in archivos_entrada:
            # Abrir el archivo Geotiff
            dataset = gdal.Open(entrada)

            if dataset is None:
                print("No se pudo abrir el archivo Geotiff:", entrada)
                continue

            #Ruta del archivo ecw
            nombre_archivo = os.path.splitext(os.path.basename(entrada))[0]
            salida = os.path.join(carpeta_salida, f"{nombre_archivo}.ecw")

            # Crear el archivo ECW
            driver = gdal.GetDriverByName("ECW")
            #print("Prueba")
            if driver is None:
                print("El driver ECW no esta disponible.")
                continue

            # Copiar el geotiff al archivo ECW
            driver.CreateCopy(salida, dataset)

            print(f"ECW convertidos con exito!!: {entrada} a {salida}")

    except Exception as e:
        print("Error:", str(e))

# Lista de archivos Geotiff de entrada
archivos_geotiff = []
while True:
    archivo = input("Ingrese el nombre del archivo Geotiff (deje en blanco para finalizar): ").strip()
    if not archivo:
        break
    archivos_geotiff.append(archivo)

if not archivos_geotiff:
    print("No se proporcionaron archivos Geotiff.")
    exit()

# Carpeta de salida para los archivos ECW
carpeta_salida = input("Ingrese la carpeta de salida para los archivos ECW: ").strip()

# Verificar si la carpeta de salida existe, si no, crearla
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

convertir_geotiff_a_ecw(archivos_geotiff, carpeta_salida)
