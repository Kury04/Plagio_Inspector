from .models import Archivo

def guardar_archivo(nombre):
    archivo = Archivo(NOMBRE=nombre)
    archivo.save()
    return f"Archivo '{nombre}' guardado con éxito."

def obtener_archivos():
    archivos = Archivo.objects.all()
    for archivo in archivos:
        print(archivo.NOMBRE, archivo.FECHA_SUBIDA)