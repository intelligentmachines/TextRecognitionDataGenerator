import os
import re
from argparse import ArgumentParser

def remove_character(string):
    
    to_keep = [ 'ঁ', 'ং', 'ঃ', 'া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ৄ', '়', 'ে', 'ৈ', 'ো', 'ৌ', '্',  'ৗ',
                'অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ' ,'ঋ' ,'এ' ,'ঐ', 'ও', 'ঔ',
                'ক', 'খ', 'গ', 'ঘ', 'ঙ',
                'চ', 'ছ', 'জ', 'ঝ', 'ঞ',
                'ট', 'ঠ', 'ড', 'ঢ', 'ণ',
                'ত', 'থ', 'দ', 'ধ', 'ন',
                'প', 'ফ', 'ব', 'ভ', 'ম',
                'য', 'র', 'ল', 'শ', 'ৎ',
                'ষ', 'স', 'হ', 
                'ঽ', 'ড়', 'ঢ়', 'য়',
                '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', 
                '/', ':', '-', ' ']
    length = len(string)
    for i in range(length):
        #print(string[i])
        if string[i] not in to_keep:
            string = string.replace(string[i],'!')
    string = string.replace('!','')        
    return string

def main(args):
  
    for filename in os.listdir(args.i):
        file_path = args.i + '/' + filename
        new_filename = filename.split('.txt')[0] + '_mod.txt'
        new_file_path = args.o + '/' + new_filename
        with open(file_path, 'r') as f:
        # reads every line and saves it into a list
            lines = f.readlines()
            line = remove_character(str(lines))
        # print(line)
        words = line.split(' ')
        # print(words)
        with open(new_file_path, 'a+') as f:
            for word in words:
                f.write(word)
                f.write('\n')
    return
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input directory")
    parser.add_argument("-o", "--o", type=str, required=True, help="Output directory")
    args = parser.parse_args()
    main(args)