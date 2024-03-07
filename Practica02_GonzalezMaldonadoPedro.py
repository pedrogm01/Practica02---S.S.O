import os
import random
import shutil
import string

def procesar_archivo(ruta):
    # Leer el contenido original del archivo
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido_original = archivo.read()

    # Cambiar letras por dígitos o dígitos por letras mayúsculas de forma aleatoria
    contenido_modificado = cambiar_letras_y_digitos(contenido_original)

    # Crear una copia del archivo con el contenido modificado
    ruta_destino = ruta + "_copia"
    with open(ruta_destino, 'w', encoding='utf-8') as archivo_destino:
        archivo_destino.write(contenido_modificado)

    # Opcional: Eliminar el archivo original si no se desea conservar
    os.remove(ruta)

def cambiar_letras_y_digitos(contenido):
    return ''.join(
        str(random.randint(0, 9)) if caracter.isalpha() else
        random.choice(string.ascii_uppercase) if caracter.isdigit() else caracter
        for caracter in contenido
    )

def copiar_y_procesar_archivos(ubicacion):
    # Crear una carpeta de destino para las copias
    carpeta_destino = ubicacion + "_copia"
    os.makedirs(carpeta_destino, exist_ok=True)

    # Recorrer la ubicación original y copiar/archivar los archivos y subcarpetas
    for carpeta_actual, subcarpetas, archivos in os.walk(ubicacion):
        carpeta_destino_actual = os.path.join(carpeta_destino, os.path.relpath(carpeta_actual, ubicacion + "\\"))

        # Crear subcarpetas en la carpeta de destino
        os.makedirs(carpeta_destino_actual, exist_ok=True)

        for archivo in archivos:
            ruta_original = os.path.join(carpeta_actual, archivo)
            ruta_destino = os.path.join(carpeta_destino_actual, archivo)

            # Copiar y procesar el archivo
            shutil.copy2(ruta_original, ruta_destino)
            procesar_archivo(ruta_destino)

# Prueba del programa con la ruta proporcionada
ubicacion_carpeta = r"E:\Respaldos a revisar\CUCEI\Semestre 9 - 2024 A\Sem Sistemas Operativos\Trabajo 02\Practica02\archivos_prod"
copiar_y_procesar_archivos(ubicacion_carpeta)
