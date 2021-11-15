import os
import shutil
import numpy as np
from argparse import ArgumentParser
import glob

def main(args):
  
    for i, filename in enumerate(os.listdir(args.i)):
        str_length = []
        file_path = args.i + '/' + filename
        with open(file_path) as f:
        # reads every line and saves it into a list
            lines = f.readlines()
            str_length.append(len(lines[0]))
    print(i)
    print(max(str_length))
    return
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input directory")
    args = parser.parse_args()
    main(args)