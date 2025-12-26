from datastore.static_data import config as datastore
from pathlib import Path
from config.directories import CONFIG_YAML_FOLDER_PATH
import os, yaml

file_suffix = "_config.yaml"
path = Path(CONFIG_YAML_FOLDER_PATH)

def load():
    for file in os.listdir(path):
        if file.endswith(file_suffix):
            file_path = path / file
            with open(file_path, "r", encoding="utf-8") as f:
                datastore[file[:-len(file_suffix)]] = yaml.safe_load(f)