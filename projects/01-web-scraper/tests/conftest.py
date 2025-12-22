from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project directory is importable for tests
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
