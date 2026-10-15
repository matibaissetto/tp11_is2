
# Registro de cambios (CHANGELOG)

Este documento registra los cambios realizados en JSON to CSV Converter.

## [0.1.0] - 2026-10-14

### Agregado
- Conversión de listas de objetos JSON a archivos CSV.
- Parámetros `-i`, `-o` y `-d` para controlar entrada, salida y delimitador.
- Soporte para entrada estándar (`stdin`) y salida estándar (`stdout`).
- Manejo de errores para archivos inexistentes, JSON inválido y delimitadores incorrectos.
- Pruebas automatizadas mediante Pytest.
- Medición de cobertura mediante pytest-cov, con mínimo requerido del 85%.
- Controles de calidad con Ruff, Black, MyPy y Pyright.
- Análisis de seguridad mediante Bandit.
- Configuración de integración continua mediante GitHub Actions.
- Documentación de instalación y utilización en README.md.

### Verificado
- 13 pruebas automatizadas aprobadas.
- Cobertura total del 88,33%.
- Sin errores reportados por Ruff, Black, MyPy, Pyright ni Bandit en la revisión local.
