import sys
from utils import checkFile_csv
import os,stat 
import click
import pandas as pd
import math

bar = None

def houseStatInterface():
    result = {
    "Ravenclaw": {"index": "Ravenclaw", "value": 0},
    "Slytherin":  {"index": "Slytherin", "value": 0},
    "Gryffindor":  {"index": "Gryffindor", "value": 0},
    "Hufflepuff":  {"index": "Hufflepuff", "value": 0},
    }
    return result



def main(file_path):
    db_path = "datasets/db.csv"
    try:
        os.chmod(db_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    except:
        click.echo(click.style(f"No Database File", fg='red'))
        return
    inputFile = pd.read_csv(file_path)
    dataFile = pd.read_csv(db_path).set_index("House")
    normFile = pd.read_csv("datasets/normalization.csv").set_index("Subject")
    try:
        with open("datasets/houses.csv", 'w') as f:
            f.write("Index,Hogwarts House\n")
            for i in range(len(inputFile)):
                firstName = inputFile["First Name"].iloc[i]
                lastName = inputFile["Last Name"].iloc[i]
                houseResult, prob = predictmodel(dataFile, inputFile, i, normFile)
                houseResult =  str(inputFile["Index"].iloc[i]) + "," + houseResult
                f.write(f"{houseResult}\n")
                print(f"{houseResult} ({prob:.1f}%)")
    except Exception as e:
        click.echo(click.style(f"Database empty{e}", fg='red'))
    return


def predictmodel(dataFile, inputFile, indexStudent, normFile):
    result = houseStatInterface()
    count = 0
    subjectList = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    houseList = ["Ravenclaw", "Gryffindor", "Slytherin", "Hufflepuff"]
    probs = {}
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
    if count != 0:
        for idxHouse in houseList:
            bias = dataFile.loc[idxHouse, 'Bias']
            if bias == 0:
                continue
            result[idxHouse]["value"] += bias
            result[idxHouse]["value"] = sigmoidFormula(result[idxHouse]["value"])
            probs[idxHouse] = result[idxHouse]["value"] * 100
    houseResult = "Ravenclaw"
    for idxHouse in houseList:
        if result[idxHouse]["value"] > result[houseResult]["value"]:
            houseResult = idxHouse
    return houseResult, probs[houseResult]
                
              
       
def ft_exp(x):
    if x < -20:
        return 0
    if x > 20:
        x = 20.0
    i = 1
    term = 1.0
    resultat = 1.0
    while i <= 30:
        term = term * (x / i)
        resultat = resultat + term
        i += 1
    return resultat
     


def sigmoidFormula(z):
    return 1.0 / (1.0 + ft_exp(-z))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("error argument file")
    else:
        if (checkFile_csv(sys.argv[1])== True):
            main(sys.argv[1])
