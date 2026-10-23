
"""Funciones para leer pedidos en formatos TXT, CSV y JSON."""

import csv
import json


def validar_pedido(pedido):
    """Comprueba que el pedido tenga los datos necesarios."""
    campos = ["pedido", "sede", "fecha", "valor", "estado"]

    for campo in campos:
        if campo not in pedido or not str(pedido[campo]).strip():
            return None

    return {campo: str(pedido[campo]).strip() for campo in campos}


def leer_txt(ruta):
    """Lee un pedido en formato TXT."""
    try:
        pedido = {}

        with open(ruta, "r", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                if ":" in linea:
                    campo, valor = linea.split(":", 1)
                    pedido[campo.strip().lower()] = valor.strip()

        return validar_pedido(pedido)

    except (OSError, UnicodeDecodeError):
        return None


def leer_csv(ruta):
    """Lee un pedido en formato CSV."""
    try:
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            pedido = next(lector, None)

            if pedido is None:
                return None

            return validar_pedido({
                campo.strip().lower(): valor
                for campo, valor in pedido.items()
                if campo is not None and valor is not None
            })

    except (OSError, UnicodeDecodeError, csv.Error):
        return None


def leer_json(ruta):
    """Lee un pedido en formato JSON."""
    try:
        with open(ruta, "r", encoding="utf-8-sig") as archivo:
            pedido = json.load(archivo)

        if not isinstance(pedido, dict):
            return None

        pedido = {
            str(campo).strip().lower(): valor
            for campo, valor in pedido.items()
        }

        return validar_pedido(pedido)

    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None

