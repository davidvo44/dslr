from StatInterface import houseStatInterface
import pandas as pd
from utilsDescribe import  getMean, getStd, getPercentile, normNumber
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
