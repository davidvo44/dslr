import pandas as pd

def countSubject(index, data):
    result = 0;
    if pd.notna(data["Arithmancy"].iloc[index]):
        result += 1;
    if pd.notna(data["Astronomy"].iloc[index]):
        result += 1;
    if pd.notna(data["Herbology"].iloc[index]):
        result += 1;
    if pd.notna(data["Defense Against the Dark Arts"].iloc[index]):
        result += 1;
    if pd.notna(data["Divination"].iloc[index]):
        result += 1;
    if pd.notna(data["Muggle Studies"].iloc[index]):
        result += 1;
    if pd.notna(data["Ancient Runes"].iloc[index]):
        result += 1;
    if pd.notna(data["History of Magic"].iloc[index]):
        result += 1;
    if pd.notna(data["Transfiguration"].iloc[index]):
        result += 1;
    if pd.notna(data["Potions"].iloc[index]):
        result += 1;
    if pd.notna(data["Care of Magical Creatures"].iloc[index]):
        result += 1;
    if pd.notna(data["Charms"].iloc[index]):
        result += 1;
    if pd.notna(data["Flying"].iloc[index]):
        result += 1;
    return result;

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
    result = 0;
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
