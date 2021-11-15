import glob
if __name__ == "__main__":
    str_length = []
    for fn in glob.glob("/home/arowa/work/porichoy/porichoy-dataset-v1/ground_truth-all/all/*.txt"):
        with open(fn) as f:
            line = f.readline().strip()
            str_length.append(len(line))
    print(max(str_length))