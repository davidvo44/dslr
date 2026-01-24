import pandas as pd
import math

def noteSubject(index, data):
    count = 0;
    result = 0;
    if pd.notna(data["Arithmancy"].iloc[index]):
        result += data["Arithmancy"].iloc[index];
        count += 1;
    if pd.notna(data["Astronomy"].iloc[index]):
        result += data["Astronomy"].iloc[index];
        count += 1;
    if pd.notna(data["Herbology"].iloc[index]):
        result += data["Herbology"].iloc[index];
        count += 1;
    if pd.notna(data["Defense Against the Dark Arts"].iloc[index]):
        result += data["Defense Against the Dark Arts"].iloc[index];
        count += 1;
    if pd.notna(data["Divination"].iloc[index]):
        result += data["Divination"].iloc[index];
        count += 1;
    if pd.notna(data["Muggle Studies"].iloc[index]):
        result += data["Muggle Studies"].iloc[index];
        count += 1;
    if pd.notna(data["Ancient Runes"].iloc[index]):
        result += data["Ancient Runes"].iloc[index];
        count += 1;
    if pd.notna(data["History of Magic"].iloc[index]):
        result += data["History of Magic"].iloc[index];
        count += 1;
    if pd.notna(data["Transfiguration"].iloc[index]):
        result += data["Transfiguration"].iloc[index];
        count += 1;
    if pd.notna(data["Potions"].iloc[index]):
        result += data["Potions"].iloc[index];
        count += 1;
    if pd.notna(data["Care of Magical Creatures"].iloc[index]):
        result += data["Care of Magical Creatures"].iloc[index];
        count += 1;
    if pd.notna(data["Charms"].iloc[index]):
        result += data["Charms"].iloc[index];
        count += 1;
    if pd.notna(data["Flying"].iloc[index]):
        result += data["Flying"].iloc[index];
        count += 1;
    result = result / count;
    return result;

def stdSubject(index, mean, data):
    result = noteSubject(index, data);
    result = pow(abs(result - mean), 2);
    return result;

# Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying

def minSubject(index, min, data):
    result = noteSubject(index, data);
    if min > result:
        return result;
    return min;

def maxSubject(index, max, data):
    result = noteSubject(index, data);
    if max < result:
        return result;
    return max;



#global
def normNumber(result):
    for subject in result.values():
        for k, v in subject.items():
            if isinstance(v, (int, float)):
                subject[k] = f"{v:.10g}"

#global
def getMean(result):
    for house in result.values():
        house["mean"] =  house["mean"] / house["count"];

#global
def getPercentile(result, list):
    for house in result.keys():
        list[house].sort();
        firstStepPercent = result[house]["count"]* 25 / 100;
        firstStepPercent = int(firstStepPercent);
        secondStepPercent = result[house]["count"]* 50 / 100;
        secondStepPercent = int(secondStepPercent);
        thirdStepPercent = result[house]["count"]* 75 / 100;
        thirdStepPercent = int(thirdStepPercent);
        result[house]["25%"] = list[house][firstStepPercent];
        result[house]["50%"] = list[house][secondStepPercent];
        result[house]["75%"] = list[house][thirdStepPercent];
    return;

# global
def getStd(result):
    for house in result.values():
        house["std"] = math.sqrt(house["std"] / house["count"]);