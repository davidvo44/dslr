
import utils
from . import normalization
from . import menu_train
import os
import stat
import pandas as pd
import click
from alive_progress import alive_bar
import sys
from utils import checkFile_csv


bar = None

def start_bar(total):
    global bar
    ctx = alive_bar(total)
    bar = ctx.__enter__()
    return ctx

def update_bar():
    bar()

def logreg_train(features, personal_info, course_name, subjectChosen):
    ctx = start_bar(100)
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    #Initialization#
    learning_rate = 0.01

    subjectTheta = {}
    X = []
    subjectStats = {}
    valid_indices = []
    col = []
    normalized = [[] for _ in range(len(subjectChosen))]

    count = len(features)
    lenPersonalInfo= len(personal_info[2])
    lenSubjectChosen = len(subjectChosen) + 1
    

    subjectValue = menu_train.houseStatInterface()
    for subject in subjectChosen:
        subjectTheta[subject] = 0
    
    #Normalization#
    for i, col_subject in enumerate(subjectChosen):
        cols_idx = utils.COLUMN_ORDER[col_subject] - 1
        col = features[cols_idx]
        normalized[i], std, avg = normalization.logreg_normalized_value(col)
        subjectStats[col_subject] = {"std": std, "mean": avg}

    #Tab for note of all student#
    for idxPersonal in range(lenPersonalInfo):
        x = [1.0]
        has_None = False
        for idxSubject in range(len(subjectChosen)):
            val = normalized[idxSubject][idxPersonal]
            if val is None:
                has_None = True
                break
            x.append(val)
        if not has_None:
            X.append(x)
            valid_indices.append(idxPersonal)

    #One for all#
    for house in utils.HOUSE_ORDER:
        y = []
        for idxPersonal in valid_indices:
            y.append(1.0 if personal_info[0][idxPersonal] == house else 0.0)
            
        theta = [0.0] * lenSubjectChosen

        theta = grad_descent(X, y, theta, 2000, 0.01)

        subjectValue[house]['bias'] = theta[0]
        subjectValue[house]['value'] = dict(zip(subjectChosen, theta[1:]))

    return subjectValue, subjectStats


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
        if i % 80 == 0:
            update_bar()
    return theta


def updateData(subjectChosen, thetaHouse, subjectStats):
    db_path = "datasets/db.csv"
    dataFile = pd.read_csv(db_path).set_index("House")
    for iHouse in range (len(utils.HOUSE_ORDER)):
        dataFile.loc[utils.HOUSE_ORDER[iHouse], 'Bias'] = thetaHouse[utils.HOUSE_ORDER[iHouse]]["bias"]
        for subject in subjectChosen:
            # click.echo(click.style(f"\nDEBUG MODE: {utils.HOUSE_ORDER[iHouse], subject, thetaHouse[utils.HOUSE_ORDER[iHouse]]['value'][subject]}", fg='cyan'))
            dataFile.loc[utils.HOUSE_ORDER[iHouse], subject] = thetaHouse[utils.HOUSE_ORDER[iHouse]]["value"][subject]
    dataFile.to_csv(db_path)
    rows = []
    for subject, stats in subjectStats.items():
        rows.append({
            "Subject": subject,
            "mean": stats["mean"],
            "std": stats["std"]
        })
    df = pd.DataFrame(rows)
    df.to_csv("datasets/normalization.csv", index=False)


def main(file_path):
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error")
        exit(1)
    menu_train.createDBFile()
    subjectChosen = []
    try:
        choice = menu_train.selectMenu()
    except KeyboardInterrupt:
        click.echo(click.style(f"\nForce Quit...", fg='red'))
        return 
    if choice == "Subject Choice":
        subjectChosen = menu_train.selectSubject()
    elif choice == "Predefined Subject":
        subjectChosen = [
        "Defense Against the Dark Arts",  # Gryffindor
        "Potions",                       # Slytherin  
        "Arithmancy",                    # Ravenclaw
        "Herbology",                     # Hufflepuff
        "Charms",                        # Gryffindor+
        "Ancient Runes"                  # Ravenclaw+
    ]
        click.echo(click.style(f"\nChosen Subject: {subjectChosen}", fg='green'))
    elif choice == "Quit":
        click.echo(click.style(f"\nLeaving....", fg='red'))
        return
    if len(subjectChosen) == 0:
        return;
    thetaHouse, subjectStats = logreg_train(features, personal_info, course_name, subjectChosen)
    updateData(subjectChosen, thetaHouse, subjectStats)
    click.echo(click.style(f"\nDone\n", fg='green'))

    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error argument file")
    else:
        if (checkFile_csv(sys.argv[1])== True):
            main(sys.argv[1])
            os.chmod("datasets/db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
