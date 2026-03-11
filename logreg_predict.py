import sys
from utils import checkFile_csv
import os,stat 
import click
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
    return result


def main(file_path):
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    inputFile = pd.read_csv(file_path)
    dataFile = pd.read_csv("db.csv").set_index("House")
    normFile = pd.read_csv("normalization.csv").set_index("Subject")
    for i in range(len(inputFile)):
        firstName = inputFile["First Name"].iloc[i]
        lastName = inputFile["Last Name"].iloc[i]
        houseResult = predictmodel(dataFile, inputFile, i, normFile)
        houseResult =  str(inputFile["Index"].iloc[i]) + "," + houseResult
        print(houseResult)
#        if i == 2:
#           return
    return


def predictmodel(dataFile, inputFile, indexStudent, normFile):
    result = houseStatInterface()
    count = 0
    subjectList = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    houseList = ["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"]
    
    for subject in  subjectList:
        count += 1
        for idxHouse in houseList:
            bias = dataFile.loc[idxHouse, 'Bias']
            weight =  dataFile.loc[idxHouse, subject]
            if weight == 0.0 or pd.isna(weight):
                continue
            studentScore = inputFile[subject].iloc[indexStudent]
            if pd.isna(studentScore):
                continue
            mean = normFile.loc[subject, "mean"]
            std  = normFile.loc[subject, "std"]
            studentScore = (studentScore - mean) / std
            result[idxHouse]["value"] += studentScore * weight
            #click.echo(click.style(f"\nDEBUG MODE: {result[idxHouse]['value']}", fg='cyan'))
    if count != 0:
        for idxHouse in houseList:
            bias = dataFile.loc[idxHouse, 'Bias']
            if bias == 0:
                continue
            #print (result[idxHouse]["value"])
            result[idxHouse]["value"] += bias
            result[idxHouse]["value"] = sigmoidFormula(result[idxHouse]["value"])
    houseResult = "Ravenclaw"
    for idxHouse in houseList:
        if result[idxHouse]["value"] > result[houseResult]["value"]:
            houseResult = idxHouse
    return houseResult
                
                
            


def sigmoidFormula(z):
    return 1.0 / (1.0 + ft_exp(-z))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error argument file")
    else:
        file_path = "datasets/dataset_test.csv"
        if (checkFile_csv(sys.argv[1])== True):
            main(sys.argv[1])
        else:
            print("Invalid File")
