import os
import json
import base64
import yaml
import joblib
from typing import List, Any, Union
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from cnnClassifier import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return its contents as a ConfigBox."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty.")
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"YAML file is empty: {path_to_yaml}")
        raise ValueError("YAML file is empty") from e
    except Exception as e:
        logger.error(f"Error loading YAML file {path_to_yaml}: {e}")
        raise


def create_directories(path_to_directories: List[Union[str, Path]], verbose: bool = True):
    """Create a list of directories."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict) -> None:
    """Save a dictionary as a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """Load JSON file content as a ConfigBox."""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path) -> None:
    """Save data as a binary file using joblib."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """Load a binary file using joblib."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def get_size(path: Path) -> str:
    """Get the file size in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(imgstring: str, file_path: Union[str, Path]) -> None:
    """Decode a base64-encoded image and save it to a file."""
    img_data = base64.b64decode(imgstring)
    with open(file_path, 'wb') as f:
        f.write(img_data)
    logger.info(f"Image decoded and saved to: {file_path}")


def encode_image_to_base64(image_path: Union[str, Path]) -> bytes:
    """Encode an image file into a base64 string."""
    with open(image_path, "rb") as f:
        encoded_data = base64.b64encode(f.read())
    logger.info(f"Image at {image_path} encoded to base64")
    return encoded_data
