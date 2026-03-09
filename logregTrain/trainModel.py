import math
import pandas as pd

def trainmodel(filename):
    dataFile = pd.read_csv(filename);
    currentDatabase = pd.read_csv("db.csv");
    CurWeight = currentDatabase["Weight"].iloc[0];
    CurBias = currentDatabase["Bias"].iloc[0];
    print(CurBias);
    while True:
        newWeight = calculateWeight(dataFile, CurWeight, CurBias);
        print(newWeight);
        return;
    return;

def calculateWeight(dataFile, Weight, Bias):
    Arithmancy = dataFile['Arithmancy'];
    return sigmoidFormula(Arithmancy, Weight, Bias).sum();


def sigmoidFormula(x, Weight, Bias):
    z = Weight * x + Bias;
    return 1 /(1 + pow(math.e,-z));

# a = learning rate, n: number elem, tmpY = Y from sigmoidFormula
# def calculateWeight(a, n, tmpY, dataFile):
#     dataFile
#     sumWeight = 
#     w - a * (1 / n) * km = dataFile["km"];