import glob
import os
from argparse import ArgumentParser
from tqdm import tqdm

# words = ['ঠিকানা', 'বাসা', 'হোল্ডিং' , 'ডাকঘর', 'রক্তের', 'গ্রুপ', 'মেয়াদ', 'উত্তীর্ণের', 'তারিখ', 'প্রদানের', 'গ্রাম', 'রাস্তা']
chars = [ 'ঁ', 'ং', 'ঃ', 'া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ৄ', '়', 'ে', 'ৈ', 'ো', 'ৌ', '্',  'ৗ',
                'অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ' ,'ঋ' ,'এ' ,'ঐ', 'ও', 'ঔ',
                'ক', 'খ', 'গ', 'ঘ', 'ঙ',
                'চ', 'ছ', 'জ', 'ঝ', 'ঞ',
                'ট', 'ঠ', 'ড', 'ঢ', 'ণ',
                'ত', 'থ', 'দ', 'ধ', 'ন',
                'প', 'ফ', 'ব', 'ভ', 'ম',
                'য', 'র', 'ল', 'শ', 'ৎ',
                'ষ', 'স', 'হ',
                'ঽ', 'ড়', 'ঢ়', 'য়']

numbers = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']

special_characters = ['/',':',",",'-', '+', ' ']

total_word_freq = {
            'ঠিকানা' : 0, 'বাসা': 0, 'হোল্ডিং' : 0, 'ডাকঘর': 0, 'রক্তের': 0, 'গ্রুপ': 0, 
            'মেয়াদ': 0, 'উত্তীর্ণের': 0, 'তারিখ': 0, 'প্রদানের': 0, 'গ্রাম': 0, 'রাস্তা': 0}

total_char_freq = {
            'ঁ': 0 , 'ং': 0, 'ঃ': 0, 'া': 0, 'ি': 0, 'ী': 0, 'ু': 0, 'ূ': 0, 'ৃ': 0, 'ৄ':0,'়':0, 'ে': 0, 'ৈ': 0, 'ো': 0, 'ৌ': 0, '্': 0,  'ৗ': 0,
            'অ': 0, 'আ': 0, 'ই': 0, 'ঈ': 0, 'উ': 0, 'ঊ': 0 ,'ঋ': 0 ,'এ': 0 ,'ঐ': 0, 'ও': 0, 'ঔ': 0,
            'ক': 0, 'খ': 0, 'গ': 0, 'ঘ': 0, 'ঙ': 0,
            'চ': 0, 'ছ': 0, 'জ': 0, 'ঝ': 0, 'ঞ': 0,
            'ট': 0, 'ঠ': 0, 'ড': 0, 'ঢ': 0, 'ণ': 0,
            'ত': 0, 'থ': 0, 'দ': 0, 'ধ': 0, 'ন': 0,
            'প': 0, 'ফ': 0, 'ব': 0, 'ভ': 0, 'ম': 0,
            'য': 0, 'র': 0, 'ল': 0, 'শ': 0, 'ৎ': 0,
            'ষ': 0, 'স': 0, 'হ': 0, 
            'ঽ': 0, 'ড়': 0, 'ঢ়': 0, 'য়': 0
        }

total_num_freq = {'০': 0, '১': 0, '২': 0, '৩': 0, '৪': 0, 
            '৫': 0, '৬': 0, '৭': 0, '৮': 0, '৯': 0}
            
total_special_char_freq = {'/': 0,':': 0,",": 0,'-': 0, '+':0, ' ':0}

def freq_check(freq):
    keys = freq.keys()
    for key in keys:
        if freq[key] > 0:
            return True

def avg(freq):
    return int(sum(freq)/len(freq))

def main(args):
   
    for filename in tqdm(os.listdir(args.i)):
        # word_freq = {
        #     'ঠিকানা' : 0, 'বাসা': 0, 'হোল্ডিং' : 0, 'ডাকঘর': 0, 'রক্তের': 0, 'গ্রুপ': 0, 
        #     'মেয়াদ': 0, 'উত্তীর্ণের': 0, 'তারিখ': 0, 'প্রদানের': 0, 'গ্রাম': 0, 'রাস্তা': 0}

        char_freq = {
            'ঁ': 0 , 'ং': 0, 'ঃ': 0, 'া': 0, 'ি': 0, 'ী': 0, 'ু': 0, 'ূ': 0, 'ৃ': 0, 'ৄ':0, '়':0, 'ে': 0, 'ৈ': 0, 'ো': 0, 'ৌ': 0, '্': 0,  'ৗ': 0,
            'অ': 0, 'আ': 0, 'ই': 0, 'ঈ': 0, 'উ': 0, 'ঊ': 0 ,'ঋ': 0 ,'এ': 0 ,'ঐ': 0, 'ও': 0, 'ঔ': 0,
            'ক': 0, 'খ': 0, 'গ': 0, 'ঘ': 0, 'ঙ': 0,
            'চ': 0, 'ছ': 0, 'জ': 0, 'ঝ': 0, 'ঞ': 0,
            'ট': 0, 'ঠ': 0, 'ড': 0, 'ঢ': 0, 'ণ': 0,
            'ত': 0, 'থ': 0, 'দ': 0, 'ধ': 0, 'ন': 0,
            'প': 0, 'ফ': 0, 'ব': 0, 'ভ': 0, 'ম': 0,
            'য': 0, 'র': 0, 'ল': 0, 'শ': 0, 'ৎ': 0,
            'ষ': 0, 'স': 0, 'হ': 0, 
            'ঽ': 0, 'ড়': 0, 'ঢ়': 0, 'য়': 0
        }

        num_freq = {'০': 0, '১': 0, '২': 0, '৩': 0, '৪': 0, 
            '৫': 0, '৬': 0, '৭': 0, '৮': 0, '৯': 0}

        special_char_freq = {'/': 0,':': 0,",": 0,'-': 0, '+':0, ' ':0}
        
        file_path = args.i + '/' + filename
        with open(file_path) as f:
            # reads the line
            line = f.readline().strip()
            # creates a list of words
            # word_list = line.split(' ')
            # for word in word_list:
                # checks every character of a word
            for i in range(len(line)):
                    if line[i] in special_characters:
                        special_char_freq[line[i]] += 1
                    elif line[i] in num_freq:
                        num_freq[line[i]] += 1
                    elif line[i] in char_freq:
                        char_freq[line[i]] += 1
            for word in special_characters:
                total_special_char_freq[word] += special_char_freq[word]
            for word in numbers:
                total_num_freq[word] += num_freq[word]
            for word in chars:
                total_char_freq[word] += char_freq[word]
    #print(total_word_freq)
    print(total_num_freq)
    print(total_special_char_freq)
    print(total_char_freq)
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