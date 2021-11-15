import os
from argparse import ArgumentParser
  
# Function to rename multiple files
def main(args):
    for filename in os.listdir(args.i):
        src = args.i + '/' + filename
        dst = args.i + '/' + filename.split('.txt')[0] + '-random.txt'
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
    return
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input directory")
    args = parser.parse_args()
    main(args)