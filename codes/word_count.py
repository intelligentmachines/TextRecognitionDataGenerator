import os
if __name__ == '__main__':
   path = '/home/arowa/work/porichoy/bn-corp-proc'
   word_count = 0
   all_words = []
   for filename in os.listdir(path):
      file_path = path + '/' + filename
      with open(file_path) as f:
        # reads the line
        line = f.readline().strip()
        word_list = line.split(" ")
        word_list = list(dict.fromkeys(word_list))
        for word in word_list:
            all_words.append(word)
   all_words = list(dict.fromkeys(all_words))
   new_file_path = 'all-words.txt'
   with open(new_file_path, 'w') as f:
      for word in all_words:
         f.write(word)
         f.write('\n')

   word_count += len(all_words)
   print(word_count)