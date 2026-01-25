import os,stat 
from utils import checkFile_csv
import sys

def main():
    createDBFile();
    
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return;


def createDBFile():
    try:
        with open("db.csv", 'w') as f:
            f.write('tetha0,tetha1\n0,0\n');
            return;
    except Exception as e:
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
        print("file already exist\n");

if __name__ == '__main__':
    print(len(sys.argv));
    file_path = "datasets/dataset_train.csv"
    checkFile_csv(file_path);
    main()

