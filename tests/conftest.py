"""Pytest configuration for importing modules from numbered directories."""
import sys
import importlib.util
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def import_day_module(day_number: int, module_name: str = "main"):
    """Import a module from a numbered day directory.
    
    Args:
        day_number: The day number (e.g., 3 for directory "3")
        module_name: The module name to import (default: "main")
    
    Returns:
        The imported module
    """
    module_path = project_root / str(day_number) / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

