
# JSON to CSV Converter

Herramienta de línea de comandos desarrollada en Python para convertir datos en formato JSON a CSV.

Proyecto realizado para el Trabajo Práctico N.º 11 de Ingeniería de Software II, enfocado en gestión y garantía de calidad del software.

## Autor

Matias Baissetto  
Universidad Autónoma de Entre Ríos (UADER)  
Año: 2026

## Características

- Conversión de JSON a CSV.
- Lectura desde archivos mediante `-i` o `--input`.
- Escritura en archivos mediante `-o` o `--output`.
- Delimitador configurable mediante `-d` o `--delimiter`.
- Soporte para entrada estándar (`stdin`) y salida estándar (`stdout`).
- Detección de errores en archivos y datos JSON inválidos.
- Soporte para registros con diferentes columnas.
- Interfaz de comandos implementada con Typer.

## Requisitos

- Python 3.12 o superior.
- pip.
- Dependencias definidas en `pyproject.toml`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/matibaissetto/json2csv.git
cd json2csv
```

Crear y activar un entorno virtual:

En Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instalar el proyecto:

```powershell
python -m pip install -e .
```

Nota: el repositorio debe existir en GitHub para poder clonarlo. Durante el desarrollo también puede utilizarse directamente la carpeta del proyecto.

## Uso

### Convertir un archivo JSON a CSV

```powershell
python -m json2csv -i ejemplo.json -o resultado.csv
```

### Utilizar un delimitador personalizado

```powershell
python -m json2csv -i ejemplo.json -o resultado.csv -d ";"
```

### Mostrar el resultado en la terminal

```powershell
python -m json2csv -i ejemplo.json
```

### Utilizar entrada y salida estándar

En PowerShell:

```powershell
Get-Content ejemplo.json -Raw | python -m json2csv
```

Redirigir el resultado a un archivo:

```powershell
Get-Content ejemplo.json -Raw | python -m json2csv | Out-File -Encoding utf8 resultado_pipe.csv
```

### Consultar la ayuda

```powershell
python -m json2csv --help
```

## Ejemplo

Archivo `ejemplo.json`:

```json
[
  {"nombre": "Juan", "edad": 25, "ciudad": "Parana"},
  {"nombre": "Pedro", "edad": 30, "ciudad": "Concepcion del Uruguay"},
  {"nombre": "Ana", "edad": 22, "ciudad": "Colon"}
]
```

Resultado CSV:

```csv
nombre,edad,ciudad
Juan,25,Parana
Pedro,30,Concepcion del Uruguay
Ana,22,Colon
```

## Manejo de errores

El conversor controla situaciones como:

- Archivo de entrada inexistente.
- Contenido JSON mal formado.
- JSON que no contiene una lista de objetos.
- Lista JSON vacía.
- Elementos que no son objetos JSON.
- Delimitadores de longitud inválida.
- Errores de lectura o escritura de archivos.

Ante estos problemas, muestra un mensaje descriptivo y finaliza con un código de error.

## Pruebas automatizadas

Las pruebas están implementadas utilizando Pytest.

Instalar las herramientas de prueba:

```powershell
python -m pip install pytest pytest-cov
```

Ejecutar las pruebas con cobertura:

```powershell
python -m pytest tests/test_json2csv.py --cov=json2csv --cov-report=term-missing
```

Resultado de la ejecución local del 14 de octubre de 2026:

- 13 pruebas aprobadas.
- Cobertura total: 88,33%.
- Cobertura mínima requerida: 85%.

## Controles de calidad

El proyecto utiliza las siguientes herramientas:

| Herramienta | Objetivo |
|---|---|
| Pytest | Pruebas automatizadas |
| pytest-cov | Medición de cobertura |
| Ruff | Análisis estático y estilo |
| Black | Formato del código |
| MyPy | Comprobación estática de tipos |
| Pyright | Análisis estático de tipos |
| Bandit | Análisis de seguridad |

Comandos de verificación:

```powershell
python -m ruff check src tests
python -m black --check src tests
python -m mypy src/json2csv
python -m pyright src/json2csv
python -m bandit -r src/json2csv
python -m pytest tests/test_json2csv.py --cov=json2csv --cov-report=term-missing
```

Todos estos controles se ejecutaron correctamente en el entorno de desarrollo local.

## Integración continua

Se incluye un workflow de GitHub Actions en:

`.github/workflows/calidad.yml`

El workflow está preparado para ejecutar los controles de calidad ante eventos `push` y `pull_request`.

Su ejecución en GitHub debe verificarse una vez publicado el repositorio.

## Estructura del proyecto

```text
json2csv/
├── .github/
│   └── workflows/
│       └── calidad.yml
├── src/
│   └── json2csv/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       └── utils.py
├── tests/
│   └── test_json2csv.py
├── ejemplo.json
├── README.md
├── LICENSE
└── pyproject.toml
```

## Licencia

Este proyecto utiliza la licencia MIT.

## Origen del proyecto

La estructura inicial fue generada con Cookiecutter utilizando la plantilla `audreyfeldroy/cookiecutter-pypackage`. La funcionalidad de conversión, las pruebas y las configuraciones de calidad fueron desarrolladas y adaptadas para este trabajo práctico.
