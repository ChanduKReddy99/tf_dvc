import yaml
import logging
import shutil
import os
from tqdm import tqdm


def read_config(path_to_config_yaml:str) -> dict:
    """Reads the config.yaml file and returns a dictionary of the config.yaml contents.
    
    Args:
        config_path (str): Path to the config.yaml file.
    
    Returns:
        dict: Dictionary of the config.yaml contents.
    """
    with open(path_to_config_yaml, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f'content read from {path_to_config_yaml} successfully..!')
    return content


def create_dirs(dir_paths:list) -> None:
    """this method Creates the directories whenever required if they do not exist.

    Args:
        list of directories(list): directories to be created.
    """
    for dir_path in dir_paths:
        os.makedirs(dir_path, exist_ok=True)
    logging.info(f'created directories at {dir_paths} successfully..!')

def copy_data(source_data_dir: str, local_data_dir: str) -> None:
    """ this method Copies the files from source to local dir.

    Args:
        source_data_dir (str): Path to the source data directory(source_data).
        local_data_dir (str): Path to the local data directory(data).
    """
    list_of_files = os.listdir(source_data_dir)
    N= len(list_of_files)

    for file_name in tqdm(list_of_files, total= N, 
        desc= f'copying files from {source_data_dir} to {local_data_dir}', 
        colour= 'green'):

        source = os.path.join(source_data_dir, file_name)
        dest = os.path.join(local_data_dir, file_name)
        shutil.copy(source, dest)
    logging.info(f'all files have been copied from {source_data_dir} to {local_data_dir} successfully..!')

    



