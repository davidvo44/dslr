from StatInterface import subjectStatInterface
import pandas as pd
from utils import countSubject, noteSubject, stdSubject
from sheetTemplate import sheetTemplate13Col
import click
import math

def subjectStat():
    result = subjectStatInterface();
    subjectList = {
        "Arithmancy": [],
        "Astronomy": [],
        "Herbology": [],
        "DATDA": [],
        "Divination": [],
        "MuggleStudies": [],
        "Ancient Runes": [],
        "Magic History": [],
        "Transfigurati": [],
        "Potions": [],
        "Care Creature": [],
        "Charms": [],
        "Flying": [],
    }
    try:
        data = pd.read_csv("dataset_train.csv");
        for i in range(len(data)):
            subjectSearch(data, i, subjectList, result);
        getMean(result);
        getPercentile(result, subjectList);
    except Exception as e:
        click.echo(f"\nerror: {e}");
    normNumber(result);
    sheetTemplate13Col(result);
    return;

def subjectSearch(data, index, subjectList, result):
    if pd.notna(data["Arithmancy"].iloc[index]):
        getInfoSubject(result["Arithmancy"], subjectList["Arithmancy"], data["Arithmancy"].iloc[index]);
    if pd.notna(data["Astronomy"].iloc[index]):
        getInfoSubject(result["Astronomy"], subjectList["Astronomy"], data["Astronomy"].iloc[index]);
    if pd.notna(data["Herbology"].iloc[index]):
        getInfoSubject(result["Herbology"], subjectList["Herbology"], data["Herbology"].iloc[index]);
    if pd.notna(data["Defense Against the Dark Arts"].iloc[index]):
        getInfoSubject(result["DATDA"], subjectList["DATDA"], data["Defense Against the Dark Arts"].iloc[index]);
    if pd.notna(data["Divination"].iloc[index]):
        getInfoSubject(result["Divination"], subjectList["Divination"], data["Divination"].iloc[index]);
    if pd.notna(data["Muggle Studies"].iloc[index]):
        getInfoSubject(result["MuggleStudies"], subjectList["MuggleStudies"], data["Muggle Studies"].iloc[index]);
    if pd.notna(data["Ancient Runes"].iloc[index]):
        getInfoSubject(result["Ancient Runes"], subjectList["Ancient Runes"], data["Ancient Runes"].iloc[index]);
    if pd.notna(data["History of Magic"].iloc[index]):
        getInfoSubject(result["Magic History"], subjectList["Magic History"], data["History of Magic"].iloc[index]);
    if pd.notna(data["Transfiguration"].iloc[index]):
        getInfoSubject(result["Transfigurati"], subjectList["Transfigurati"], data["Transfiguration"].iloc[index]);
    if pd.notna(data["Potions"].iloc[index]):
        getInfoSubject(result["Potions"], subjectList["Potions"], data["Potions"].iloc[index]);
    if pd.notna(data["Care of Magical Creatures"].iloc[index]):
        getInfoSubject(result["Care Creature"], subjectList["Care Creature"], data["Care of Magical Creatures"].iloc[index]);
    if pd.notna(data["Charms"].iloc[index]):
        getInfoSubject(result["Charms"], subjectList["Charms"], data["Charms"].iloc[index]);
    if pd.notna(data["Flying"].iloc[index]):
        getInfoSubject(result["Flying"], subjectList["Flying"], data["Flying"].iloc[index]);
    return;

def getInfoSubject(resultSubject, listSubject, value):
    resultSubject["count"] += 1;
    listSubject.append(value);
    resultSubject["mean"] += value;
    resultSubject["min"] = minSubject(resultSubject["min"] , value);
    resultSubject["max"] = maxSubject(resultSubject["max"] , value);

def minSubject(min, value):
    if min > value:
        return value;
    return min;

def maxSubject(max, value):
    if max < value:
        return value;
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
        list[house].sort;
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
