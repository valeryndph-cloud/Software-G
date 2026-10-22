"""Funciones para reconocer la sede de cada pedido."""

import re
import unicodedata


SEDES = {
    "itagui": ["itagui", "itagüí", "itagui antioquia"],
    "envigado": ["envigado"],
    "sabaneta": ["sabaneta"],
}


def normalizar_texto(texto):
    """Pasa el texto a minúsculas y quita tildes y signos innecesarios."""
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(letra for letra in texto if unicodedata.category(letra) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", texto)


def reconocer_sede(pedido):
    """Devuelve 'Itagüí', 'Envigado' o 'Sabaneta'; si no la reconoce, devuelve None.

    Acepta un texto o un diccionario con datos del pedido.
    """
    if isinstance(pedido, dict):
        texto = " ".join(str(valor) for valor in pedido.values() if valor is not None)
    elif pedido is None:
        return None
    else:
        texto = str(pedido)

    texto = normalizar_texto(texto)
    for sede, variantes in SEDES.items():
        for variante in variantes:
            variante_normalizada = normalizar_texto(variante)
            if re.search(r"\b" + re.escape(variante_normalizada) + r"\b", texto):
                return {"itagui": "Itagüí", "envigado": "Envigado", "sabaneta": "Sabaneta"}[sede]

    return None
