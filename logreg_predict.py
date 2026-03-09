import sys
from utils import checkFile_csv
import os,stat 
import pandas as pd
import math
from logreg_train import ft_exp


def houseStatInterface():
    result = {
    "Ravenclaw": {"index": "Ravenclaw", "value": 0},
    "Slytherin":  {"index": "Slytherin", "value": 0},
    "Gryffindor":  {"index": "Gryffindor", "value": 0},
    "Hufflepuff":  {"index": "Hufflepuff", "value": 0},
    }
    return result;


def main(file_path):
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);
    inputFile = pd.read_csv("dataset_train.csv");
    dataFile = pd.read_csv("db.csv");
    for i in range(len(inputFile)):
        firstName = inputFile["First Name"].iloc[i];
        lastName = inputFile["Last Name"].iloc[i];
        houseResult = predictmodel(dataFile, inputFile, i);
        houseResult =  str(inputFile["Index"].iloc[i]) + "," + houseResult;
        print(houseResult);
    return;


def predictmodel(dataFile, inputFile, i):
    result = houseStatInterface();
    count = 0;
    subjectList = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    houseList = ["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"];
    for i in  range (12):
        subject = subjectList[i];
        bias = dataFile[subject].iloc[0];
        if bias == 0:
            continue;
        count += 1;
        for iHouse in range (3):
            indexWeight =  dataFile[dataFile["House"] == houseList[iHouse]].index[0];
            result[houseList[iHouse]]["value"] = dataFile[subject].iloc[indexWeight];
    if count != 0:
        for iHouse in range (3):
            result[houseList[iHouse]]["value"] /= count;
    houseResult = "Ravenclaw";
    for iHouse in range (3):
        if result[houseList[iHouse]]["value"] > result[houseResult]["value"]:
            houseResult = houseList[iHouse];
    return houseResult;
                
                
            


def sigmoidFormula(weight, bias, studentScore):
    z = weight * studentScore + bias;
    return 1.0 / (1.0 + ft_exp(-z))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error argument file");
    else:
        file_path = "datasets/dataset_test.csv"
        if (checkFile_csv(sys.argv[1])== True):
            main(file_path);
        else:
            print("Invalid File");

