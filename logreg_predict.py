import sys
from utils import checkFile_csv
import os,stat 
import pandas as pd
import math

def main(file_path):
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);
    inputFile = pd.read_csv("dataset_train.csv");
    dataFile = pd.read_csv("db.csv");
    for i in range(len(inputFile)):
        firstName = inputFile["First Name"].iloc[i];
        lastName = inputFile["Last Name"].iloc[i];
        print(i, " " , firstName, lastName );
        predictmodel(dataFile, inputFile, i);
    return;

def predictmodel(dataFile, inputFile, i):
    result = 0;
    count = 0;
    subjectList = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    houseList = ["Ravenclaw", "Gryffundor", "Slytherin", "Hufflepuff"];
    for i in  range (12):
        subject = subjectList[i];
        for iHouse in range (3):
            indexWeight =  dataFile[dataFile["House"] == houseList[iHouse] + "Weight"].index[0];
            weight = dataFile[subject].iloc[indexWeight];
            indexBias =  dataFile[dataFile["House"] == houseList[iHouse] + "Bias"].index[0];
            bias = dataFile[subject].iloc[indexBias];
            if weight != 0 and bias != 0:
                result += sigmoidFormula();
                count += 1;
        result = result / count;
        

def sigmoidFormula(weight, bias, studentScore):
    z = weight * studentScore + bias;
    return 1 /(1 + pow(math.e,-z));


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error argument file");
    else:
        file_path = "datasets/dataset_test.csv"
        if (checkFile_csv(sys.argv[1])== True):
            main(file_path);
        else:
            print("Invalid File");

