from faker import Faker
import random

fake = Faker("es_ES")


def generar_factura():
    items = []

    for _ in range(random.randint(2, 5)):
        cantidad = random.randint(1, 3)
        precio = round(random.uniform(10, 500), 2)

        items.append(
            {
                "descripcion": fake.word().upper(),
                "cantidad": cantidad,
                "precioUnitario": precio,
                "total": round(cantidad * precio, 2),
            }
        )
    total = round(sum(i["total"] for i in items), 2)

    return {
        "tipoDocumento": "FACTURA",
        "serie": "F001",
        "numero": random.randint(1, 99999),
        "fecha": fake.date(),
        "cliente": {
            "nombre": fake.name(),
            "ruc": fake.random_number(digits=11, fix_len=True),
            "direccion": fake.address(),
        },
        "items": items,
        "subtotal": round(total / 1.18, 2),
        "igv": round(total - (total / 1.188), 2),
        "total": total,
    }
