import os
import argparse
from threading import local
from tqdm import tqdm
import logging
from src.utils.common_utils import read_config, create_dirs, copy_data


logging.basicConfig(
    filename= os.path.join('logs', 'running_logs.log'),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode= 'a'
)

def get_data(config_path: str) -> None:
    """this method gets the data from source to local dir by reading config.yaml file.

    Args:
        config_path (str): Path to the config.yaml file.
    """
    config = read_config(config_path)

    # get the data from source to local dir
    source_data_dirs= config['source_data_download_path']
    local_data_dirs= config['local_data_path']

    N= len(source_data_dirs)
    for source_data_dir, local_data_dir in tqdm(zip(source_data_dirs, local_data_dirs),
                         total=N,
                         desc= 'copying directory:',
                         colour= 'green'):
                         create_dirs([local_data_dir])
                         copy_data(source_data_dir, local_data_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Get and save data from the source.')
    parser.add_argument('--config', '-c', default='configs/config.yaml',help='Path to the config.yaml file.')
    parsed_args= parser.parse_args()

    try:
        logging.info('\n**********************************')
        logging.info(' >>>>>>> stage 1: get data  started <<<<<<< ')
        get_data(parsed_args.config)
        logging.info(' >>>>>>> stage 1: get data  completed sucessfully <<<<<<< \n')

    except Exception as e:
        logging.error(e)
        logging.error(' >>>>>>> stage 1: get data  failed <<<<<<< \n')
