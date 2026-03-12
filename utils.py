from pyexpat import features
import pandas as pd
import click

HOUSE_ORDER = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

COLUMN_ORDER = {
        "Arithmancy": 1,
        "Astronomy": 2,
        "Herbology": 3,
        "Defense Against the Dark Arts": 4,
        "Divination": 5,
        "Muggle Studies": 6,
        "Ancient Runes": 7,
        "History of Magic": 8,
        "Transfiguration": 9,
        "Potions": 10,
        "Care of Magical Creatures": 11,
        "Charms": 12,
        "Flying": 13
    }

HOUSE_COLORS = {
        "Gryffindor": "red",
        "Hufflepuff": "brown",
        "Ravenclaw": "yellow",
        "Slytherin": "green",
    }

subjectList = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]


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

def ft_sqrt(a):
    if a == 0:
        return 0
    x = a / 2
    for i in range(6):
        x = 0.5 * (x + a / x)
    return x

def parse_csv(filepath):
    data = open_csv(filepath)
    if data is None:
        return None
    lines = data.strip().split('\n') # split the data into lines and remove the empty lines
    header = lines[0].split(",")
    course_name = [header[i+6].strip() for i in range(13)] 
    data_lines = lines[1:] # remove the header line
    features = [[] for _ in range(13)] # list of features
    personal_info = [[] for _ in range(6)] # list of personal information
    for line in data_lines:
        cols = line.split(',')
        for i in range(6):
            value = cols[i+1].strip()
            if value:
                personal_info[i].append(value)
            else:
                personal_info[i].append(None)
        for i in range(13):
            value = cols[i+6].strip()
            if value:
                features[i].append(float(value))
            else:
                features[i].append(None)
    return features, personal_info, course_name

def checkFile_csv(filepath):
    try:
        data = pd.read_csv(filepath);
    except Exception as e:
        click.echo(click.style(f"Error reading file {filepath} \n  -> {e}", fg='red'))
        return False
    if 'Hogwarts House' in data.columns and 'First Name' in data.columns and 'Last Name' in data.columns and \
        'Birthday' in data.columns and 'Best Hand' in data.columns and 'Arithmancy' in data.columns and \
        'Astronomy' in data.columns and 'Herbology' in data.columns and 'Defense Against the Dark Arts' in data.columns \
            and 'Divination' in data.columns and 'Muggle Studies' in data.columns and 'Ancient Runes' \
            in data.columns and 'History of Magic' in data.columns and 'Transfiguration' in data.columns \
                and 'Potions' in data.columns and 'Care of Magical Creatures' in data.columns \
                    and 'Charms' in data.columns and 'Flying' in data.columns:
        return True;
    return False;