"""Organiza los pedidos recibidos por sede sin modificar los originales."""

import re
import shutil
import unicodedata
from pathlib import Path

from lectores import leer_csv, leer_json, leer_txt
from sedes import reconocer_sede


LECTORES = {
    ".txt": leer_txt,
    ".csv": leer_csv,
    ".json": leer_json,
}

SEDES = ("Itagüí", "Envigado", "Sabaneta", "Bello")
VARIANTES_SEDE = {
    "Itagüí": ("itagui", "itagüí", "itagui antioquia"),
    "Envigado": ("envigado", "env"),
    "Sabaneta": ("sabaneta",),
    "Bello": ("bello",),
}


def normalizar_sede(texto):
    """Normaliza el texto de sede para comparar tildes y mayúsculas."""
    texto = str(texto).strip().casefold()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )
    return re.sub(r"[^a-z0-9 ]", " ", texto)


def valor_valido(valor):
    """Acepta valores numéricos no negativos, incluidos importes como $1.000."""
    valor_normalizado = re.sub(r"[$.,\s]", "", str(valor))
    return valor_normalizado.isdigit()


def obtener_sede(pedido):
    """Identifica la sede usando el campo sede del pedido."""
    if not isinstance(pedido, dict):
        return reconocer_sede(pedido)

    texto_sede = normalizar_sede(pedido.get("sede", ""))
    if not texto_sede.strip():
        return None

    sedes_encontradas = []
    for sede, variantes in VARIANTES_SEDE.items():
        for variante in variantes:
            variante_normalizada = normalizar_sede(variante)
            if re.search(r"\b" + re.escape(variante_normalizada) + r"\b", texto_sede):
                sedes_encontradas.append(sede)
                break

    # Si el campo menciona más de una sede, no asigna el pedido arbitrariamente.
    if len(sedes_encontradas) != 1:
        return None

    return sedes_encontradas[0]


def organizar_pedidos():
    """Lee los pedidos de bandeja_entrada y copia cada uno a su carpeta."""
    base = Path(__file__).resolve().parent
    entrada = base / "bandeja_entrada"
    salida = base / "pedidos_ordenados"

    if not entrada.is_dir():
        print("No se encontró la carpeta bandeja_entrada/.")
        print("Ejecuta primero: python generar_pedidos.py")
        return

    # Los resultados se generan de nuevo para no conservar copias antiguas.
    if salida.exists():
        shutil.rmtree(salida)
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
        if pedido is None or not valor_valido(pedido.get("valor", "")):
            omitidos += 1
            continue

        sede = obtener_sede(pedido)
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
