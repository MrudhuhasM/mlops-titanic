

from dataclasses import dataclass
from typing import Optional
import hydra
from omegaconf import DictConfig

@dataclass
class Config:
    RAW_DATA_DIR = None
    PROCESSED_DATA_DIR = None
    INTERIM_DATA_DIR = None
    MODEL_DIR = None
    LOG_DIR = None
    ARTIFACTS_DIR = None
    LOG_LEVEL = "INFO"
    LOG_FILE = None
    LOG_ROTATION = "10 MB"
    LOG_RETENTION = 5
    BUCKET_NAME = None

def build_config(cfg: DictConfig):
    """
    Build a Config object from Hydra DictConfig.
    Call this in your CLI entrypoint and pass the result to other modules.
    """
    Config.RAW_DATA_DIR = cfg.dir_paths.data_raw
    Config.PROCESSED_DATA_DIR = cfg.dir_paths.data_processed
    Config.INTERIM_DATA_DIR = cfg.dir_paths.data_interim
    Config.MODEL_DIR = cfg.dir_paths.models
    Config.LOG_DIR = cfg.logging.log_file 
    Config.ARTIFACTS_DIR = cfg.dir_paths.artifacts
    Config.LOG_LEVEL = cfg.logging.level
    Config.LOG_ROTATION = cfg.logging.rotation
    Config.LOG_RETENTION = cfg.logging.retention
    Config.BUCKET_NAME = cfg.env.storage.bucket_name


def set_config(cfg: DictConfig):
    """
    Hydra entrypoint for config. Returns a Config object.
    """
    config = build_config(cfg)
    print("Configuration set up successfully.")
    

