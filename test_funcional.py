
import subprocess
import sys

import pytest


def ejecutar_programa(entrada):
    return subprocess.run(
        [sys.executable, "collatz.py"],
        input=str(entrada),
        capture_output=True,
        text=True,
        timeout=5,
    )


@pytest.mark.parametrize(
    "entrada",
    ["0", "-5", "2000", "3.5", "abc"],
)
def test_entradas_invalidas(entrada):
    resultado = ejecutar_programa(entrada)

    assert resultado.returncode == 0
    assert "inválido" in resultado.stdout.lower()


@pytest.mark.parametrize(
    "entrada,iteraciones",
    [
        ("1", 0),
        ("10", 6),
    ],
)
def test_resultados(entrada, iteraciones):
    resultado = ejecutar_programa(entrada)

    assert resultado.returncode == 0
    assert entrada in resultado.stdout
    assert str(iteraciones) in resultado.stdout


def test_entrada_por_teclado():
    resultado = ejecutar_programa("1999")

    assert resultado.returncode == 0
    assert "1999" in resultado.stdout



def test_t10_limite_superior():
    resultado = ejecutar_programa("1999")

    assert resultado.returncode == 0
    assert "para 1999 es 50" in resultado.stdout


def test_t15_valor_1998():
    resultado = ejecutar_programa("1998")

    assert resultado.returncode == 0
    assert "para 1998 es 50" in resultado.stdout
