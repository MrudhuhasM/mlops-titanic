


import logging
import logging.handlers
import sys
from typing import Optional



def setup_logger(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    use_tqdm: bool = True,
) -> None:
    """
    Configure Python built-in logger for the project.
    Args:
        log_level (str): Logging level (e.g., 'INFO', 'DEBUG').
        log_file (Optional[str]): Optional path to a log file.
        use_tqdm (bool): If True, integrate with tqdm progress bars.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level.upper())
    # Remove all handlers
    while root_logger.handlers:
        root_logger.handlers.pop()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Rotating file handler
    if log_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    # TQDM integration
    if use_tqdm:
        try:
            global logging_redirect_tqdm
            from tqdm.contrib.logging import logging_redirect_tqdm
            root_logger.info("TQDM logging integration enabled.")
        except ImportError:
            root_logger.warning("tqdm.contrib.logging not available; tqdm integration skipped.")



def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Returns a logger instance with the given name (or root logger if None).
    """
    return logging.getLogger(name)


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
