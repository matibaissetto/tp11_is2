"""Funciones para convertir datos JSON a CSV."""

import csv
import io
import json
from typing import Any


def convertir_json_a_csv(contenido: str, delimitador: str = ",") -> str:
    """Convertir una lista de objetos JSON a texto CSV."""
    if len(delimitador) != 1:
        raise ValueError("El delimitador debe tener un solo carácter")

    datos: Any = json.loads(contenido)

    if not isinstance(datos, list):
        raise ValueError("El JSON debe contener una lista de objetos")

    if not datos:
        raise ValueError("La lista JSON no puede estar vacía")

    if not all(isinstance(elemento, dict) for elemento in datos):
        raise ValueError("Todos los elementos deben ser objetos JSON")

    columnas = list(dict.fromkeys(clave for elemento in datos for clave in elemento))

    salida = io.StringIO(newline="")
    escritor = csv.DictWriter(
        salida,
        fieldnames=columnas,
        delimiter=delimitador,
        extrasaction="ignore",
        lineterminator="\n",
    )

    escritor.writeheader()
    escritor.writerows(datos)

    return salida.getvalue()
