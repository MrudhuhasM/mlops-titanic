"""
Project configuration loader using Hydra and OmegaConf.
Loads directory paths and exposes them as constants.
"""

import os
from omegaconf import OmegaConf
import hydra

# Path to config.yaml (relative to project root)
_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "conf", "config.yaml")


_cfg = OmegaConf.load(_CONFIG_PATH)
DIR_PATHS = _cfg.dir_paths if hasattr(_cfg, "dir_paths") else {}

# Expose as constants (use getattr for fallback)
RAW_DATA_DIR = getattr(DIR_PATHS, "data_raw", "data/raw")
PROCESSED_DATA_DIR = getattr(DIR_PATHS, "data_processed", "data/processed")
EXTERNAL_DATA_DIR = getattr(DIR_PATHS, "data_external", "data/external")
INTERIM_DATA_DIR = getattr(DIR_PATHS, "data_interim", "data/interim")
ARTIFACTS_DIR = getattr(DIR_PATHS, "artifacts", "artifacts")
MODELS_DIR = getattr(DIR_PATHS, "models", "artifacts/models")
REPORTS_DIR = getattr(DIR_PATHS, "reports", "artifacts/reports")
NOTEBOOKS_DIR = getattr(DIR_PATHS, "notebooks", "notebooks")
LOGS_DIR = getattr(DIR_PATHS, "logs", "logs")

# Optionally, provide a function to reload config if needed
def reload_config():
    global _cfg, DIR_PATHS
    _cfg = OmegaConf.load(_CONFIG_PATH)
    DIR_PATHS = _cfg.dir_paths if hasattr(_cfg, "dir_paths") else {}
