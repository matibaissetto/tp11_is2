"""Pruebas automatizadas del conversor JSON a CSV."""

import json

import pytest
from typer.testing import CliRunner

from json2csv.cli import app
from json2csv.utils import convertir_json_a_csv

runner = CliRunner()


def test_conversion_basica():
    """Verificar la conversión de JSON a CSV."""
    contenido = '[{"nombre": "Juan", "edad": 25}]'

    resultado = convertir_json_a_csv(contenido)

    assert resultado == "nombre,edad\nJuan,25\n"


def test_varios_registros():
    """Verificar la conversión de varios registros."""
    contenido = '[{"nombre": "Juan"}, {"nombre": "Ana"}]'

    resultado = convertir_json_a_csv(contenido)

    assert resultado == "nombre\nJuan\nAna\n"


def test_delimitador_personalizado():
    """Verificar el delimitador de punto y coma."""
    contenido = '[{"nombre": "Juan", "edad": 25}]'

    resultado = convertir_json_a_csv(contenido, ";")

    assert resultado == "nombre;edad\nJuan;25\n"


def test_columnas_diferentes():
    """Verificar registros con diferentes columnas."""
    contenido = '[{"nombre": "Juan"}, {"edad": 30}]'

    resultado = convertir_json_a_csv(contenido)

    assert resultado == "nombre,edad\nJuan,\n,30\n"


def test_json_invalido():
    """Rechazar contenido que no sea JSON válido."""
    with pytest.raises(json.JSONDecodeError):
        convertir_json_a_csv('{"nombre":')


def test_json_no_es_lista():
    """Rechazar un objeto JSON que no sea una lista."""
    with pytest.raises(ValueError, match="lista de objetos"):
        convertir_json_a_csv('{"nombre": "Juan"}')


def test_lista_vacia():
    """Rechazar una lista JSON vacía."""
    with pytest.raises(ValueError, match="vacía"):
        convertir_json_a_csv("[]")


def test_elementos_no_son_objetos():
    """Rechazar listas cuyos elementos no sean objetos."""
    with pytest.raises(ValueError, match="objetos JSON"):
        convertir_json_a_csv("[1, 2, 3]")


def test_delimitador_invalido():
    """Rechazar delimitadores de más de un carácter."""
    with pytest.raises(ValueError, match="delimitador"):
        convertir_json_a_csv('[{"nombre": "Juan"}]', ";;")


def test_cli_archivos(tmp_path):
    """Verificar lectura y escritura mediante archivos."""
    entrada = tmp_path / "entrada.json"
    salida = tmp_path / "salida.csv"

    entrada.write_text('[{"nombre": "Ana"}]', encoding="utf-8")

    resultado = runner.invoke(
        app,
        ["-i", str(entrada), "-o", str(salida)],
    )

    assert resultado.exit_code == 0
    assert salida.read_text(encoding="utf-8") == "nombre\nAna\n"


def test_cli_entrada_salida_estandar():
    """Verificar entrada y salida estándar."""
    resultado = runner.invoke(
        app,
        input='[{"nombre": "Pedro"}]',
    )

    assert resultado.exit_code == 0
    assert resultado.stdout == "nombre\nPedro\n"


def test_cli_archivo_inexistente(tmp_path):
    """Verificar el error cuando no existe la entrada."""
    entrada = tmp_path / "inexistente.json"

    resultado = runner.invoke(app, ["-i", str(entrada)])

    assert resultado.exit_code == 1
    assert "Error:" in resultado.output


def test_cli_delimitador_invalido():
    """Verificar el manejo de delimitadores inválidos."""
    resultado = runner.invoke(
        app,
        ["-d", ";;"],
        input='[{"nombre": "Juan"}]',
    )

    assert resultado.exit_code == 1
    assert "Error:" in resultado.output
