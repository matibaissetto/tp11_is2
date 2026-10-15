"""Punto de entrada del conversor JSON a CSV."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from json2csv.cli import app  # noqa: E402

if __name__ == "__main__":
    app()