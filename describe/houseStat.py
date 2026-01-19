from StatInterface import houseStatInterface
import pandas as pd
from utils import countSubject, noteSubject, stdSubject
from sheetTemplate import sheetTemplate4Col
import click

def houseStat():
    result = houseStatInterface();
    try:
        data = pd.read_csv("dataset_train.csv");
        # yop = data["Hogwarts House"].mean();
        for i in range(len(data)):
            house = data["Hogwarts House"].iloc[i];
            if house == "Ravenclaw":
                result["count0"] += 1;
                result["countSubject0"] += countSubject(i,data);
                result["mean0"] += noteSubject(i, data);
            if  house == "Slytherin":
                result["count1"] += 1;
                result["countSubject1"] += countSubject(i,data);
                result["mean1"] += noteSubject(i, data);
            if  house == "Gryffindor":
                result["count2"] += 1;
                result["countSubject2"] += countSubject(i,data);
                result["mean2"] += noteSubject(i, data);
            if  house == "Hufflepuff":
                result["count3"] += 1;
                result["countSubject3"] += countSubject(i,data);
                result["mean3"] += noteSubject(i, data);
        getMean(result);
        for i in range(len(data)):
            house = data["Hogwarts House"].iloc[i];
            if house == "Ravenclaw":
                result["std0"] += stdSubject(i,result["mean0"], data);
            if  house == "Slytherin":
                result["std1"] += stdSubject(i,result["mean1"], data);
            if  house == "Gryffindor":
                result["std2"] += stdSubject(i,result["mean2"], data);
            if  house == "Hufflepuff":
                result["std3"] += stdSubject(i,result["mean3"], data);
        normNumber(result);
        sheetTemplate4Col(result);
    except Exception as e:
        click.echo(f"\nerror: {e}");
    return;

def getMean(result):
    result["mean0"] =  result["mean0"] /  result["countSubject0"];
    result["mean1"] =  result["mean1"] /  result["countSubject1"];
    result["mean2"] =  result["mean2"] /  result["countSubject2"];
    result["mean3"] =  result["mean3"] /  result["countSubject3"];

def normNumber(result):
    result["mean0"] = f"{result['mean0']:.10g}";
    result["mean1"] = f"{result['mean1']:.10g}";
    result["mean2"] = f"{result['mean2']:.10g}";
    result["mean3"] = f"{result['mean3']:.10g}";