from pyexpat import features
import pandas as pd


def open_csv(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

def parse_csv(filepath):
    data = open_csv(filepath)
    if data is None:
        return None
    lines = data.strip().split('\n') # split the data into lines and remove the empty lines
    data_lines = lines[1:] # remove the header line
    features = [[] for _ in range(13)] # list of features
    personal_info = [[] for _ in range(6)] # list of personal information
    for line in data_lines:
        cols = line.split(',')
        for i in range(6):
            value = cols[i+1].strip()
            if value:
                personal_info[i].append(value)
        for i in range(13):
            value = cols[i+6].strip()
            if value:
                features[i].append(float(value))
    return features, personal_info

def checkFile_csv(filepath):
    data = pd.read_csv(filepath);
    if 'Hogwarts House' in data.columns and 'First Name' in data.columns and 'Last Name' in data.columns and \
        'Birthday' in data.columns and 'Best Hand' in data.columns and 'Arithmancy' in data.columns and \
        'Astronomy' in data.columns and 'Herbology' in data.columns and 'Defense Against the Dark Arts' in data.columns \
            and 'Divination' in data.columns and 'Muggle Studies' in data.columns and 'Ancient Runes' \
            in data.columns and 'History of Magic' in data.columns and 'Transfiguration' in data.columns \
                and 'Potions' in data.columns and 'Care of Magical Creatures' in data.columns \
                    and 'Charms' in data.columns and 'Flying' in data.columns:
        print("work!!!!");