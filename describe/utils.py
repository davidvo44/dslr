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
    result = 0;
    if pd.notna(data["Arithmancy"].iloc[index]):
        result += data["Arithmancy"].iloc[index];
    if pd.notna(data["Astronomy"].iloc[index]):
        result += data["Astronomy"].iloc[index];
    if pd.notna(data["Herbology"].iloc[index]):
        result += data["Herbology"].iloc[index];
    if pd.notna(data["Defense Against the Dark Arts"].iloc[index]):
        result += data["Defense Against the Dark Arts"].iloc[index];
    if pd.notna(data["Divination"].iloc[index]):
        result += data["Divination"].iloc[index];
    if pd.notna(data["Muggle Studies"].iloc[index]):
        result += data["Muggle Studies"].iloc[index];
    if pd.notna(data["Ancient Runes"].iloc[index]):
        result += data["Ancient Runes"].iloc[index];
    if pd.notna(data["History of Magic"].iloc[index]):
        result += data["History of Magic"].iloc[index];
    if pd.notna(data["Transfiguration"].iloc[index]):
        result += data["Transfiguration"].iloc[index];
    if pd.notna(data["Potions"].iloc[index]):
        result += data["Potions"].iloc[index];
    if pd.notna(data["Care of Magical Creatures"].iloc[index]):
        result += data["Care of Magical Creatures"].iloc[index];
    if pd.notna(data["Charms"].iloc[index]):
        result += data["Charms"].iloc[index];
    if pd.notna(data["Flying"].iloc[index]):
        result += data["Flying"].iloc[index];
    return result;

def stdSubject(index, mean, data):
    result = 0;
    if pd.notna(data["Arithmancy"].iloc[index]):
        result += abs(data["Arithmancy"].iloc[index] - mean);
    if pd.notna(data["Astronomy"].iloc[index]):
        result += abs(data["Astronomy"].iloc[index] - mean);
    if pd.notna(data["Herbology"].iloc[index]):
        result += abs(data["Herbology"].iloc[index] - mean);
    if pd.notna(data["Defense Against the Dark Arts"].iloc[index]):
        result += abs(data["Defense Against the Dark Arts"].iloc[index] - mean);
    if pd.notna(data["Divination"].iloc[index]):
        result += abs(data["Divination"].iloc[index] - mean);
    if pd.notna(data["Muggle Studies"].iloc[index]):
        result += abs(data["Muggle Studies"].iloc[index] - mean);
    if pd.notna(data["Ancient Runes"].iloc[index]):
        result += abs(data["Ancient Runes"].iloc[index] - mean);
    if pd.notna(data["History of Magic"].iloc[index]):
        result += abs(data["History of Magic"].iloc[index] - mean);
    if pd.notna(data["Transfiguration"].iloc[index]):
        result += abs(data["Transfiguration"].iloc[index] - mean);
    if pd.notna(data["Potions"].iloc[index]):
        result += abs(data["Potions"].iloc[index] - mean);
    if pd.notna(data["Care of Magical Creatures"].iloc[index]):
        result += abs(data["Care of Magical Creatures"].iloc[index] - mean);
    if pd.notna(data["Charms"].iloc[index]):
        result += abs(data["Charms"].iloc[index] - mean);
    if pd.notna(data["Flying"].iloc[index]):
        result += abs(data["Flying"].iloc[index] - mean);
    return result;
# Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying
