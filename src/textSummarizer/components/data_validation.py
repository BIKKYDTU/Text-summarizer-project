import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True

            # Loop through required files
            for file in self.config.ALL_REQUIRED_FILES:
                file_path = os.path.join(self.config.root_dir, file)
                if not os.path.exists(file_path):
                    validation_status = False
                    logger.error(f"Missing required file: {file}")
                    break  # no need to continue if one is missing

            # Write status file
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
