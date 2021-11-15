import glob
import os
from argparse import ArgumentParser

words = ['ঠিকানা', 'বাসা', 'হোল্ডিং' , 'ডাকঘর', 'রক্তের', 'গ্রুপ', 'মেয়াদ', 'উত্তীর্ণের', 'তারিখ', 'প্রদানের', 'গ্রাম', 'রাস্তা']
numbers = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
special_characters = ['/',':',",",'-']

total_word_freq = {
            'ঠিকানা' : 0, 'বাসা': 0, 'হোল্ডিং' : 0, 'ডাকঘর': 0, 'রক্তের': 0, 'গ্রুপ': 0, 
            'মেয়াদ': 0, 'উত্তীর্ণের': 0, 'তারিখ': 0, 'প্রদানের': 0, 'গ্রাম': 0, 'রাস্তা': 0}

total_num_freq = {'০': 0, '১': 0, '২': 0, '৩': 0, '৪': 0, 
            '৫': 0, '৬': 0, '৭': 0, '৮': 0, '৯': 0}
            
total_special_char_freq = {'/': 0,':': 0,",": 0,'-': 0}

def freq_check(freq):
    keys = freq.keys()
    for key in keys:
        if freq[key] > 0:
            return True

def avg(freq):
    return int(sum(freq)/len(freq))

def main(args):
   
    for filename in os.listdir(args.i):
        word_freq = {
            'ঠিকানা' : 0, 'বাসা': 0, 'হোল্ডিং' : 0, 'ডাকঘর': 0, 'রক্তের': 0, 'গ্রুপ': 0, 
            'মেয়াদ': 0, 'উত্তীর্ণের': 0, 'তারিখ': 0, 'প্রদানের': 0, 'গ্রাম': 0, 'রাস্তা': 0}


        num_freq = {'০': 0, '১': 0, '২': 0, '৩': 0, '৪': 0, 
            '৫': 0, '৬': 0, '৭': 0, '৮': 0, '৯': 0}

        special_char_freq = {'/': 0,':': 0,",": 0,'-': 0}
        
        file_path = args.i + '/' + filename
        with open(file_path) as f:
            # reads the line
            line = f.readline().strip()
            # creates a list of words
            word_list = line.split(' ')
            for word in word_list:
                # checks every character of a word
                for i in range(len(word)):
                    if word[i] in special_characters:
                        special_char_freq[word[i]] += 1
            for word in special_characters:
                total_special_char_freq[word] += special_char_freq[word]
    #print(total_word_freq)
    #print(total_num_freq)
    print(total_special_char_freq)
            #if freq_check(word_freq):
            #    txt_file_path = '/home/arowa/work/porichoy/corpus_word_freq_list.txt'
            #    with open(txt_file_path, 'a+') as f:
            #        f.write(filename + ' ' + str(word_freq))
            #        f.write('\n')

# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input directory")
    args = parser.parse_args()
    main(args)