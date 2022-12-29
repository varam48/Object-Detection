import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    
    source = data_dir + str("/training_and_validation/")
    dest_train = data_dir + str("/train/")
    dest_val = data_dir + str("/val/")
    dest_test = data_dir + str("/test/")
        
    get_files = os.listdir(source)                     
    j=0  
    # 80% of the files will be placed in train, 10% in val and 10% in test
    for i in get_files:
        if j<10:
            shutil.move(source + i, dest_val) 
        elif j>=10 and j <20:
            shutil.move(source + i, dest_test)
        else:    
            shutil.move(source + i, dest_train) 
        j = j+1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
