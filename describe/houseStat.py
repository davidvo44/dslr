from StatInterface import houseStatInterface
import pandas as pd
from utils import countSubject, noteSubject, stdSubject, minSubject, maxSubject
from sheetTemplate import sheetTemplate4Col
import click
import math

def houseStat():
    result = houseStatInterface();
    houseList = {
        "Ravenclaw": [],
        "Slytherin": [],
        "Gryffindor": [],
        "Hufflepuff": [],
    }
    try:
        data = pd.read_csv("dataset_train.csv");
        for i in range(len(data)):
            house = data["Hogwarts House"].iloc[i];
            if house == "Ravenclaw":
                getInfoHouse(result["Ravenclaw"], houseList['Ravenclaw'], data, i);
            if house == "Slytherin":
                getInfoHouse(result["Slytherin"], houseList['Slytherin'], data, i);
            if house == "Gryffindor":
                getInfoHouse(result["Gryffindor"], houseList['Gryffindor'], data, i);
            if house == "Hufflepuff":
                getInfoHouse(result["Hufflepuff"], houseList['Hufflepuff'], data, i);
        getMean(result);
        for i in range(len(data)):
            house = data["Hogwarts House"].iloc[i];
            if house == "Ravenclaw":
                result["Ravenclaw"]["std"] += stdSubject(i,result["Ravenclaw"]["mean"], data);
            if  house == "Slytherin":
                result["Slytherin"]["std"] += stdSubject(i,result["Slytherin"]["mean"], data);
            if  house == "Gryffindor":
                result["Gryffindor"]["std"] += stdSubject(i,result["Gryffindor"]["mean"], data);
            if  house == "Hufflepuff":
                result["Hufflepuff"]["std"] += stdSubject(i,result["Hufflepuff"]["mean"], data);
        getStd(result);
        getPercentile(result, houseList);
        normNumber(result);
        sheetTemplate4Col(result);
    except Exception as e:
        click.echo(f"\nerror: {e}");
    return;

def getInfoHouse(resultHouse, listHouse, data, index):
    resultHouse["count"] += 1;
    listHouse.append(noteSubject(index, data));
    resultHouse["mean"] += noteSubject(index, data);
    resultHouse["min"] = minSubject(index,resultHouse["min"] , data);
    resultHouse["max"] = maxSubject(index,resultHouse["max"] , data);
    return;

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

def getMean(result):
    for house in result.values():
        house["mean"] =  house["mean"] / house["count"];

def getStd(result):
    for house in result.values():
        house["std"] = math.sqrt(house["std"] / house["count"]);

def normNumber(result):
    for house in result.values():
        for k, v in house.items():
            if isinstance(v, (int, float)):
                house[k] = f"{v:.10g}"

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
