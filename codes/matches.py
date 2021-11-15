import glob
import os
from argparse import ArgumentParser


if __name__ == '__main__':
   
    file_path = '/home/arowa/work/porichoy/article-keep-lists/char_keep_list.txt'
    with open(file_path) as f:
        # reads the lines
        lines = f.readlines()
        char_article_names = []
        for line in lines:
            char_article_names.append(line.split(' ')[0])
    
    file_path = '/home/arowa/work/porichoy/article-keep-lists/num_keep_list.txt'
    with open(file_path) as f:
        # reads the lines
        lines = f.readlines()
        num_article_names = []
        for line in lines:
            num_article_names.append(line.split(' ')[0])

    list1_as_set = set(char_article_names)
    intersection = list1_as_set.intersection(num_article_names)

    intersection_as_list = list(intersection)
    txt_file_path = '/home/arowa/work/porichoy/article_keep_list.txt'
    with open(txt_file_path, 'a+') as f:
        for name in sorted(intersection_as_list):
            f.write(name)
            f.write('\n')
