
from tsp.config.config import Config, set_config
from config.logger import setup_logger, get_logger
from omegaconf import DictConfig, OmegaConf
from tsp.utils.data_setup import download_data, upload_data
import hydra

@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    set_config(cfg)
    setup_logger()
    logger = get_logger(__name__)

    logger.info("Starting data download and upload process.")
    try:
        file_path = download_data()
        upload_data(file_path)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    else:
        logger.info("Data download and upload process completed successfully.")


if __name__ == "__main__":
    main()