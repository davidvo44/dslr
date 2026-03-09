import os,stat 
from utils import checkFile_csv
import sys
from logregTrain.trainModel import trainmodel

def main(file_path):
    createDBFile();
    trainmodel(file_path);
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);
    return;


def createDBFile():
    try:
        with open("db.csv", 'w') as f:
            f.write("\
House,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying\n\
RavenclawBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
RavenclawWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
GryffundorBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
GryffundorWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
SlytherinBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
SlytherinWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
HufflepuffBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
HufflepuffWeight,0,0,0,0,0,0,0,0,0,0,0,0\n");
            return;
    except Exception as e:
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
        # print("file already exist\n");

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error argument file");
    else:
        file_path = "datasets/dataset_train.csv"
        if (checkFile_csv(sys.argv[1])== True):
            main(file_path);
        else:
            print("Invalid File");

