from generators import generar_factura
from services import subir_json, enviar_cola
import uuid
import json


def main():
    print("1. Factura")
    print("2. Boleta")
    print("3. Guia Remision")

    opcion = input("Seleccione opcion:")

    if opcion == "1":
        data = generar_factura()
    else:
        print("Opcion no implementada")
        return

    nombre_archivo = f"{uuid.uuid4()}.json"

    subir_json(nombre_archivo, json.dumps(data, ensure_ascii=False, indent=2))
    enviar_cola(nombre_archivo)

    print("Proceso Completado")


if __name__ == "__main__":
    main()
