import utils
import os,stat 
import pandas as pd
from InquirerPy import inquirer
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

def ft_sqrt(a):
    if a == 0:
        return 0
    x = a / 2
    for i in range(6):
        x = 0.5(x + a/x)
    return x

def logreg_average(value):
    m = len(value)
    for i in range(len(value)):
        result += value
    return result / m

# def logreg_standard_deviation()
    

# def logreg_normalized_value()


def logreg_train(features, personal_info, course_name, subjectChosen):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    subjectTheta = {}
    subjectValue = houseStatInterface()
    for subject in subjectChosen:
        subjectTheta[subject] = 0
    
    count = len(features)
    learning_rate = 0.01

    lenPersonalInfo= len(personal_info)
    lenSubjectChosen = len(subjectChosen) + 1
    X = []
    for idxPersonal in range(lenPersonalInfo):
        x = [1.0]
        has_None = False
        for idxSubject in subjectChosen:
            val = features[idxPersonal][COLUMN_ORDER[idxSubject]]
            if val is None:
                has_None = True
                break
            x.append(val)
        if not has_None:
            X.append(x)
    for house in HOUSE_ORDER:
        y = []
        for idxPersonal in range(lenPersonalInfo):
            y.append(1.0 if personal_info[idxPersonal][2] == house else 0.0)
        theta = [0.0] * lenSubjectChosen

        theta = grad_descent(X, y, theta, 1000, 0.01)

        subjectValue[house]['bias'] = theta[0]
        theta.remove(theta[0])
        theta = dict(zip(subjectChosen, theta))
        subjectValue[house]['value'] = theta
        
    print(subjectValue)
    
    # print("Gryffindor theta:", subjectValue["Gryffindor"]);
    return subjectValue

def score_lineaire(student, poid): #formule theta^t * x
    count = len(student)
    result = 0.0
    for i in range(count):
        result += student[i] * poid[i]
    return result 

def ft_exp(x):
    if x < -20:
        return 0
    if x > 20:
        x = 20.0
    i = 1
    term = 1.0
    resultat = 1.0
    while i <= 30:
        term = term * (x / i)
        resultat = resultat + term
        i += 1
    return resultat

"""σ(z) = 1/(1+e^{-z})"""

def sigmoid(z):
    return 1.0 / (1.0 + ft_exp(-z))

def grad_descent(X, y, theta , nb_iteration, learning_rate):
    for i in range(nb_iteration):
        gradient = [0.0] * len(theta)
        for eleve_idx in range(len(X)):
            z = score_lineaire(X[eleve_idx], theta)
            h = sigmoid(z)
            e = h - y[eleve_idx]

            for para_idx in range(len(theta)):
                gradient[para_idx] += e * X[eleve_idx][para_idx]
        
        for para_idx in range(len(theta)):
            gradient[para_idx] /= len(X)

        for para_idx in range(len(theta)): 
            theta[para_idx] -= learning_rate * gradient[para_idx]
    
    return theta


def createDBFile():
    fileBuffer = "\
House,Bias,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying\n\
Ravenclaw,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n\
Gryffindor,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n\
Slytherin,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n\
Hufflepuff,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n"
    try:
        with open("db.csv", 'w') as f:
            f.write(fileBuffer);
            return;
    except Exception as e:
        print("YOOO");
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
        try:
            choice = resetFileChoice();
        except KeyboardInterrupt:
            click.echo(click.style(f"\nForce Quit...", fg='red'));
            return ;
        if choice == "Yes":
            with open("db.csv", 'w') as f:
                f.write(fileBuffer);

    

def updateData(subjectChosen, thetaHouse):
    
    dataFile = pd.read_csv("db.csv").set_index("House");
    for iHouse in range (len(HOUSE_ORDER)):
        dataFile.loc[HOUSE_ORDER[iHouse], 'Bias'] = thetaHouse[HOUSE_ORDER[iHouse]]["bias"];
        for subject in subjectChosen:
            # click.echo(click.style(f"\nDEBUG MODE: {HOUSE_ORDER[iHouse], subject, thetaHouse[HOUSE_ORDER[iHouse]]['value'][subject]}", fg='cyan'));
            dataFile.loc[HOUSE_ORDER[iHouse], subject] = thetaHouse[HOUSE_ORDER[iHouse]]["value"][subject];
    dataFile.to_csv("db.csv");

def houseStatInterface():
    result = {
    "Ravenclaw": {"index": "Ravenclaw", "bias": 0, "value": {}},
    "Slytherin":  {"index": "Slytherin", "bias": 0, "value": {}},
    "Gryffindor":  {"index": "Gryffindor", "bias": 0, "value": {}},
    "Hufflepuff":  {"index": "Hufflepuff", "bias": 0, "value": {}}
    }
    return result;

def selectMenu():
    return inquirer.select(
        message="\n\nYour choice ?",
        choices=["Subject Choice", "Predefined Subject", "Quit"]
    ).execute()

def resetFileChoice():
    return inquirer.select(
        message="\n\nDatabase found, do you want to reset it",
        choices=["Yes", "No"]
    ).execute()


def selectSubject():
    chosenSubject = [];
    subjectList = ["Arithmancy",
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
        "Flying"]

    try:
        while True:
            choice = getSubject(subjectList)
            if choice == "Done":
                return chosenSubject;
            subjectList.remove(choice);
            chosenSubject.append(choice);
            click.echo(click.style(f"\nChosen Subject: {chosenSubject}", fg='green'));
        
    except:
        click.echo(click.style(f"\nForce Quit...", fg='red'));
        return [];


def getSubject(subjectList):
    choicesAdd = [];
    for subject in  subjectList:
        choicesAdd.append(subject);
    choicesAdd.append("Done");
    return inquirer.select(
        message="\n\nSelect Your Subject ?",
        choices = choicesAdd
    ).execute()



def main():
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error")
        exit(1)
    createDBFile();
    subjectChosen = [];
    try:
        choice = selectMenu();
    except KeyboardInterrupt:
        click.echo(click.style(f"\nForce Quit...", fg='red'));
        return ;
    if choice == "Subject Choice":
        subjectChosen = selectSubject();
    elif choice == "Predefined Subject":
        subjectChosen = ["Arithmancy",
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
        "Flying"]
        click.echo(click.style(f"\nChosen Subject: {subjectChosen}", fg='green'));
    elif choice == "Quit":
        click.echo(click.style(f"\nLeaving....", fg='red'));
        return;
    thetaHouse = logreg_train(features, personal_info, course_name, subjectChosen);
    updateData(subjectChosen, thetaHouse);

if __name__ == "__main__":
        main();
        os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);


# TO DO, split les fonctions en plusieures fichiers