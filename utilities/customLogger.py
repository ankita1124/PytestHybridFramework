import logging
import os


# lib for generating logs
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log", format="%(asctime)s: %(levelname)s: %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

        """log_dir = "./Logs"
        log_file = "automation.log"

        # Create the 'Logs' directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        # Get the absolute path for the log file
        log_file_path = os.path.join(log_dir, log_file)

        logging.basicConfig(filename=log_file_path, format="%(asctime)s:%(levelname)s:%(message)s",
                            datefmt='%m%d%Y %I:%M:%S %p')
        """
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger