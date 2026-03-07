import math
import pandas as pd

def trainmodel(filename):
    try:
        dataFile = pd.read_csv(filename);
        currentDatabase = pd.read_csv("db.csv");

        splitPerSubject("Arithmancy", dataFile, currentDatabase);
        splitPerSubject("Herbology", dataFile, currentDatabase);
        splitPerSubject("Defense Against the Dark Arts", dataFile, currentDatabase);
        splitPerSubject("Divination", dataFile, currentDatabase);
        splitPerSubject("Muggle Studies", dataFile, currentDatabase);
        splitPerSubject("Ancient Runes", dataFile, currentDatabase);
        splitPerSubject("History of Magic", dataFile, currentDatabase);
        splitPerSubject("Transfiguration", dataFile, currentDatabase);
        splitPerSubject("Potions", dataFile, currentDatabase);
        splitPerSubject("Care of Magical Creatures", dataFile, currentDatabase);
        splitPerSubject("Charms", dataFile, currentDatabase);
        splitPerSubject("ArithmFlyingancy", dataFile, currentDatabase);
    except Exception as e:
        print(f"\nerror: {e}");


def splitPerSubject(subject, dataFile, currentDatabase):
    splitPerHouse("Ravenclaw", subject, dataFile, currentDatabase);
    splitPerHouse("Gryffundor", subject, dataFile, currentDatabase);
    splitPerHouse("Slytherin", subject, dataFile, currentDatabase);
    splitPerHouse("Hufflepuff", subject, dataFile, currentDatabase);
    return;

def splitPerHouse(house, suject, dataFile, currentDatabase):

    # print(currentDatabase);
    # return;
    CurWeight = currentDatabase.at[house + "Weight", suject];
    CurBias = currentDatabase.at[house + "Bias", suject];
    print(CurBias);
    while True:
        newWeight = calculateWeight(dataFile, CurWeight, CurBias);
        print(newWeight);
        return;
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