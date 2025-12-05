"""Pytest configuration."""
import importlib.util
from pathlib import Path

def import_day(day_number: int):
    """Import main module from a day directory."""
    project_root = Path(__file__).parent.parent
    module_path = project_root / str(day_number) / "main.py"
    spec = importlib.util.spec_from_file_location(f"day{day_number}_main", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
