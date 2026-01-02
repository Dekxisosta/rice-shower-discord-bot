from datastore.static_data import config as datastore
from pathlib import Path
from utils.console_logger import log
from config.directories import CONFIG_YAML_FOLDER_PATH
import os, yaml

file_suffix = "_config.yaml"
path = Path(CONFIG_YAML_FOLDER_PATH)

def load():
    success_count = 0
    failed_count = 0
    for file in os.listdir(path):
        if file.endswith(file_suffix):
            file_path = path / file
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    datastore[file[:-len(file_suffix)]] = yaml.safe_load(f)
                log(f"Loaded {file}", module_name="YAML_LOADER", success=True)
                success_count += 1
            except Exception as e:
                log(f"Failed to load {file}: {e}", module_name="YAML_LOADER", success=False)
                failed_count += 1
    log(
        f"Finished loading YAML files: {success_count} succeeded, {failed_count} failed.",
        module_name="YAML_LOADER",
        success=True
    )

