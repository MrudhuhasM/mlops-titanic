


from loguru import logger
import sys
import os
from typing import Optional
from tsp.config.config import Config



LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level:<8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


def setup_logger(log_level=None, log_file=None, use_tqdm=True):
    """
    Configure loguru logger for the project using a config object.
    Args:
        config (Config): Config object with logging settings.
        log_level (str): Optional override for logging level.
        log_file (str): Optional override for log file path.
        use_tqdm (bool): If True, integrate with tqdm progress bars.
    """
    log_level = log_level or Config.LOG_LEVEL or "INFO"
    log_file = log_file or Config.LOG_FILE

    logger.remove()
    logger.add(sys.stdout, level=log_level.upper(), format=LOG_FORMAT, enqueue=True, backtrace=True, diagnose=True)

    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logger.add(
            log_file,
            rotation=Config.LOG_ROTATION,
            retention=Config.LOG_RETENTION,
            level=log_level.upper(),
            format=LOG_FORMAT,
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        logger.debug(f"Logging to file: {log_file}")

    if use_tqdm:
        try:
            from tqdm.contrib.logging import logging_redirect_tqdm
            logger.info("TQDM logging integration enabled.")
        except ImportError:
            logger.warning("tqdm.contrib.logging not available.")

    logger.info("Logger setup complete.")
    logger.debug(f"Log level set to: {log_level}")
    logger.debug(f"Log file set to: {log_file}")
    logger.debug("TQDM integration enabled." if use_tqdm else "TQDM integration not enabled.")

    return logger

def get_logger(name: Optional[str] = None):
    """
    Get a logger instance with the specified name.
    If no name is provided, use the root logger.
    """
    return logger.bind(name=name) if name else logger



def tqdm_logging():
    """
    Context manager for redirecting logging to tqdm progress bars if available.
    Usage:
        with tqdm_logging():
            ...
    """
    try:
        from tqdm.contrib.logging import logging_redirect_tqdm
        return logging_redirect_tqdm()
    except ImportError:
        class DummyContext:
            def __enter__(self): return None
            def __exit__(self, exc_type, exc_val, exc_tb): return False
        return DummyContext()



