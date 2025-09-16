import os
import sys
import dill
import logging
import numpy as np
import pandas as pd
from src.exception import CustomException


def save_object(file_path: str, obj: object) -> None:
    """
    Save a Python object to a file using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str) -> object:
    """
    Load a Python object from a file using dill.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
