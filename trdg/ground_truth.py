# This script creates separate ground truth txt files for every generated image

import os
from argparse import ArgumentParser

def main(args):
    # The labels.txt file contains all the ground truths along with the names of the images
    # Example of one line in the labels.txt file: 1.jpg intelligent machines
    file_name = "labels.txt"
    file_path = os.path.join(args.i, file_name)
    lines = []
    
    with open(file_path) as f:
        # reads every line and saves it into a list
        lines = f.readlines()
    
    for line in lines:
        image_no = line.split(".jpg ")[0]
        words = line.split(".jpg ")[1]
        directory = os.path.join(args.o)
        
        with open(f'{directory}/{image_no}.txt','a+') as f: 
            f.write(f"{words}")
            f.close()
    return

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input directory")
    parser.add_argument("-o", "--o", type=str, required=True, help="Output directory")
    args = parser.parse_args()
    os.makedirs(args.o, exist_ok=True)

    main(args)
    