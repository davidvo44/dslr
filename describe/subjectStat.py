from StatInterface import subjectStatInterface
import pandas as pd
from utils import countSubject, noteSubject, stdSubject, minSubject, maxSubject
from sheetTemplate import sheetTemplate13Col
import click
import math

def subjectStat():
    result = subjectStatInterface();
    sheetTemplate13Col(result);
    return;
    ravenclawList = [];
    slytherinList = [];
    gryffindorList = [];
    hufflepuffList = [];
    try:
        data = pd.read_csv("dataset_train.csv");
        # yop = data["Hogwarts House"].mean();
        for i in range(len(data)):
            house = data["Hogwarts House"].iloc[i];
            if house == "Ravenclaw":
                result["count0"] += 1;
                ravenclawList.append(noteSubject(i, data));
                result["mean0"] += noteSubject(i, data);
                result["min0"] = minSubject(i,result["min0"] , data);
                result["max0"] = maxSubject(i,result["max0"] , data);
            if  house == "Slytherin":
                result["count1"] += 1;
                slytherinList.append(noteSubject(i, data));
                result["mean1"] += noteSubject(i, data);
                result["min1"] = minSubject(i,result["min1"] , data);
                result["max1"] = maxSubject(i,result["max1"] , data);
            if  house == "Gryffindor":
                result["count2"] += 1;
                gryffindorList.append(noteSubject(i, data));
                result["mean2"] += noteSubject(i, data);
                result["min2"] = minSubject(i,result["min2"] , data);
                result["max2"] = maxSubject(i,result["max2"] , data);
            if  house == "Hufflepuff":
                result["count3"] += 1;
                hufflepuffList.append(noteSubject(i, data));
                result["mean3"] += noteSubject(i, data);
                result["min3"] = minSubject(i,result["min3"] , data);
                result["max3"] = maxSubject(i,result["max3"] , data);
        getPercentile(result, ravenclawList, slytherinList, gryffindorList, hufflepuffList);
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
        getStd(result);
        normNumber(result);
    except Exception as e:
        click.echo(f"\nerror: {e}");
    return;



def getPercentile(result, ravenclawList: list, slytherinList: list, gryffindorList: list, hufflepuffList: list):
    ravenclawList.sort;
    slytherinList.sort;
    gryffindorList.sort;
    hufflepuffList.sort;

    firstStepPercent0 = result["count0"]* 25 / 100;
    firstStepPercent0 = int(firstStepPercent0);
    secondStepPercent0 = result["count0"]* 50 / 100;
    secondStepPercent0 = int(secondStepPercent0);
    thirdStepPercent0 = result["count0"]* 75 / 100;
    thirdStepPercent0 = int(thirdStepPercent0);
    result["25%0"] = ravenclawList[firstStepPercent0];
    result["50%0"] = ravenclawList[secondStepPercent0];
    result["75%0"] = ravenclawList[thirdStepPercent0];

    firstStepPercent1 = result["count1"]* 25 / 100;
    firstStepPercent1 = int(firstStepPercent1);
    secondStepPercent1 = result["count1"]* 50 / 100;
    secondStepPercent1 = int(secondStepPercent1);
    thirdStepPercent1 = result["count1"]* 75 / 100;
    thirdStepPercent1 = int(thirdStepPercent1);
    result["25%1"] = ravenclawList[firstStepPercent1];
    result["50%1"] = ravenclawList[secondStepPercent1];
    result["75%1"] = ravenclawList[thirdStepPercent1];

    firstStepPercent2 = result["count2"]* 25 / 100;
    firstStepPercent2 = int(firstStepPercent2);
    secondStepPercent2 = result["count2"]* 50 / 100;
    secondStepPercent2 = int(secondStepPercent2);
    thirdStepPercent2 = result["count2"]* 75 / 100;
    thirdStepPercent2 = int(thirdStepPercent2);
    result["25%2"] = ravenclawList[firstStepPercent2];
    result["50%2"] = ravenclawList[secondStepPercent2];
    result["75%2"] = ravenclawList[thirdStepPercent2];

    firstStepPercent3 = result["count3"]* 25 / 100;
    firstStepPercent3 = int(firstStepPercent3);
    secondStepPercent3 = result["count3"]* 50 / 100;
    secondStepPercent3 = int(secondStepPercent3);
    thirdStepPercent3 = result["count3"]* 75 / 100;
    thirdStepPercent3 = int(thirdStepPercent3);
    result["25%3"] = ravenclawList[firstStepPercent3];
    result["50%3"] = ravenclawList[secondStepPercent3];
    result["75%3"] = ravenclawList[thirdStepPercent3];


def getMean(result):
    result["mean0"] =  result["mean0"] /  result["count0"];
    result["mean1"] =  result["mean1"] /  result["count1"];
    result["mean2"] =  result["mean2"] /  result["count2"];
    result["mean3"] =  result["mean3"] /  result["count3"];

def getStd(result):
    result["std0"] = math.sqrt(result["std0"] / result["count0"]);
    result["std1"] = math.sqrt(result["std1"] / result["count1"]);
    result["std2"] = math.sqrt(result["std2"] / result["count2"]);
    result["std3"] = math.sqrt(result["std3"] / result["count3"]);

def normNumber(result):
    result["mean0"] = f"{result['mean0']:.10g}";
    result["mean1"] = f"{result['mean1']:.10g}";
    result["mean2"] = f"{result['mean2']:.10g}";
    result["mean3"] = f"{result['mean3']:.10g}";
    result["std0"] = f"{result['std0']:.10g}";
    result["std1"] = f"{result['std1']:.10g}";
    result["std2"] = f"{result['std2']:.10g}";
    result["std3"] = f"{result['std3']:.10g}";
    result["min0"] = f"{result['min0']:.10g}";
    result["min1"] = f"{result['min1']:.10g}";
    result["min2"] = f"{result['min2']:.10g}";
    result["min3"] = f"{result['min3']:.10g}";
    result["max0"] = f"{result['max0']:.10g}";
    result["max1"] = f"{result['max1']:.10g}";
    result["max2"] = f"{result['max2']:.10g}";
    result["max3"] = f"{result['max3']:.10g}";
    result["25%0"] = f"{result['25%0']:.10g}";
    result["25%1"] = f"{result['25%1']:.10g}";
    result["25%2"] = f"{result['25%2']:.10g}";
    result["25%3"] = f"{result['25%3']:.10g}";
    result["50%0"] = f"{result['50%0']:.10g}";
    result["50%1"] = f"{result['50%1']:.10g}";
    result["50%2"] = f"{result['50%2']:.10g}";
    result["50%3"] = f"{result['50%3']:.10g}";
    result["75%0"] = f"{result['75%0']:.10g}";
    result["75%1"] = f"{result['75%1']:.10g}";
    result["75%2"] = f"{result['75%2']:.10g}";
    result["75%3"] = f"{result['75%3']:.10g}";