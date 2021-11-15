if __name__ == '__main__':
   
    file_path = '/home/arowa/work/porichoy/article_keep_list.txt'
    with open(file_path) as f:
        # reads the lines
        lines = f.readlines()
        # creates a list of articles
        article_list = []
        for line in lines:
            article_list.append(line.split('\n')[0])
        for i, article in enumerate(article_list):
            file_path = '/home/arowa/work/porichoy/bn_corpus/' + article
            with open(file_path) as f:
                line = f.readline().strip()
                txt_file_path = '/home/arowa/work/porichoy/bn_corpus.txt'
                with open(txt_file_path, 'a+') as f:
                    f.write(str(line))
                    f.write('\n')

    print(i)
