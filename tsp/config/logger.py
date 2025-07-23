



from loguru import logger
import sys
import os
from typing import Optional
from tsp.config.config import LOGS_DIR, LOG_LEVEL,ENV

def setup_logger(
    log_level: str = LOG_LEVEL,
    log_file: Optional[str] = os.path.join(LOGS_DIR, "app.log"),
    use_tqdm: bool = True,
) -> None:
    """
    Configure loguru logger for the project.
    Args:
        log_level (str): Logging level (e.g., 'INFO', 'DEBUG').
        log_file (Optional[str]): Optional path to a log file.
        use_tqdm (bool): If True, integrate with tqdm progress bars.
    """
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logger.add(
            log_file,
            rotation="10 MB",
            retention=5,
            encoding="utf-8",
            level=log_level.upper(),
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
    if use_tqdm:
        try:
            from tqdm.contrib.logging import logging_redirect_tqdm
            logger.info("TQDM logging integration enabled.")
        except ImportError:
            logger.warning("tqdm.contrib.logging not available; tqdm integration skipped.")




# For compatibility with previous code
def get_logger(name: Optional[str] = None):
    """
    Returns the loguru logger (ignores name, for compatibility).
    """
    return logger


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
    

if __name__ == "__main__":
    setup_logger(log_file="logs/app.log")
    logger.info("Logger setup complete.")
    logger.info(f"Log level set to {LOG_LEVEL}.")
    logger.info(f"Environment: {ENV}.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
