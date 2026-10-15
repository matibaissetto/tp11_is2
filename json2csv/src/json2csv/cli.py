"""Interfaz de consola del conversor JSON a CSV."""

import sys
from pathlib import Path
from typing import Annotated

import typer

from json2csv.utils import convertir_json_a_csv

app = typer.Typer()


@app.command()
def main(
    entrada: Annotated[
        Path | None,
        typer.Option("--input", "-i", help="Archivo JSON de entrada"),
    ] = None,
    salida: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Archivo CSV de salida"),
    ] = None,
    delimitador: Annotated[
        str,
        typer.Option("--delimiter", "-d", help="Delimitador CSV"),
    ] = ",",
) -> None:
    """Convertir JSON a CSV con archivos o entrada/salida estándar."""
    try:
        if entrada is None:
            contenido = sys.stdin.read()
        else:
            contenido = entrada.read_text(encoding="utf-8")

        resultado = convertir_json_a_csv(contenido, delimitador)

        if salida is None:
            sys.stdout.write(resultado)
        else:
            salida.write_text(resultado, encoding="utf-8")

    except (OSError, ValueError) as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=1) from error


if __name__ == "__main__":
    app()
