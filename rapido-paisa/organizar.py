"""Organiza los pedidos recibidos por sede sin modificar los originales."""

import shutil
from pathlib import Path

from lectores import leer_csv, leer_json, leer_txt
from sedes import reconocer_sede


LECTORES = {
    ".txt": leer_txt,
    ".csv": leer_csv,
    ".json": leer_json,
}

SEDES = ("Itagüí", "Envigado", "Sabaneta")


def organizar_pedidos():
    """Lee los pedidos de bandeja_entrada y copia cada uno a su carpeta."""
    base = Path(__file__).resolve().parent
    entrada = base / "bandeja_entrada"
    salida = base / "pedidos_ordenados"

    if not entrada.is_dir():
        print("No se encontró la carpeta bandeja_entrada/.")
        print("Ejecuta primero: python generar_pedidos.py")
        return

    salida.mkdir(parents=True, exist_ok=True)

    for sede in SEDES:
        (salida / sede).mkdir(exist_ok=True)

    sin_clasificar = salida / "Sin_clasificar"
    copiados = 0
    omitidos = 0

    for archivo in sorted(entrada.iterdir()):
        if not archivo.is_file():
            continue

        lector = LECTORES.get(archivo.suffix.lower())
        if lector is None:
            omitidos += 1
            continue

        pedido = lector(archivo)
        if pedido is None:
            omitidos += 1
            continue

        sede = reconocer_sede(pedido)
        if sede not in SEDES:
            # Conserva el archivo original y separa los pedidos no reconocidos.
            sin_clasificar.mkdir(exist_ok=True)
            destino = sin_clasificar
        else:
            destino = salida / sede

        shutil.copy2(archivo, destino / archivo.name)
        copiados += 1

    print("Organización finalizada.")
    print(f"Pedidos copiados: {copiados}")
    print(f"Archivos omitidos por formato o datos inválidos: {omitidos}")
    print(f"Carpeta de resultados: {salida}")


if __name__ == "__main__":
    organizar_pedidos()
