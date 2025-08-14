from typing import Final
import os

DEBUG_DEFAULT: Final[bool] = False
STEPS_DEFAULT: Final[int] = 100
OUTPUT_DIR_DEFAULT: Final[str] = os.path.join(os.getcwd(), "output_dir")

def _to_bool(v: str | None, default: bool) -> bool:
    if v is None:
        return default
    return v.lower() in {"1", "true", "yes", "on"}

# Effective settings (env vars override defaults if present)
DEBUG: Final[bool] = _to_bool(os.getenv("MONA_DEBUG"), DEBUG_DEFAULT)
STEPS: Final[int] = int(os.getenv("MONA_STEPS", str(STEPS_DEFAULT)))
OUTPUT_DIR: Final[str] = os.getenv("MONA_OUTPUT_DIR", OUTPUT_DIR_DEFAULT)
