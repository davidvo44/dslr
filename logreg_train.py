import utils
import os,stat 
import pandas as pd

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

def logreg_train(features, personal_info, course_name, subjectChosen):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    subjectTheta = {}

    for subject in subjectChosen:
        subjectTheta[subject] = 0;
    
    count = len(features)
    feat_idx = [1, 4, 7, 9, 2];
    learning_rate = 0.01

    m = len(personal_info)
    n = len(subjectChosen) + 1
    X = []
    for i in range(m):
        x = [1.0]
        has_None = False
        for idx in subjectChosen:
            val = features[i][COLUMN_ORDER[idx]]
            if val is None:
                has_None = True
                break
            x.append(features[i][COLUMN_ORDER[idx]])
        if not has_None:
            X.append(x)
    for house in HOUSE_ORDER:
        y = []
        for i in range(m):
            y.append(1.0 if personal_info[i][2] == house else 0.0)
        theta = [0.0] * n

        theta = grad_descent(X, y, theta, 1000, 0.01)

        subjectTheta[house] = theta;
    
    print("Gryffindor theta:", subjectTheta["Gryffindor"][2]);
    return subjectTheta

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
    try:
        with open("db.csv", 'w') as f:
            f.write("\
House,Bias,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying\n\
Ravenclaw,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
Gryffindor,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
Slytherin,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
Hufflepuff,0,0,0,0,0,0,0,0,0,0,0,0,0\n");
            return;
    except Exception as e:
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
        # print("file already exist\n");

def updateData(subjectChosen, thetaHouse):
    dataFile = pd.read_csv("db.csv");
    for iHouse in range (len(HOUSE_ORDER)):
        for subject in subjectChosen:
            indexHouse =  dataFile[dataFile["House"] == HOUSE_ORDER[iHouse]].index[0];
            dataFile[subject].iloc[indexHouse] = thetaHouse[HOUSE_ORDER][iHouse]["value"][subject];

def houseStatInterface():
    result = {
    "Ravenclaw": {"index": "Ravenclaw", "bias": 0, "value": {}},
    "Slytherin":  {"index": "Slytherin", "bias": 0, "value": {}},
    "Gryffindor":  {"index": "Gryffindor", "bias": 0, "value": {}},
    "Hufflepuff":  {"index": "Hufflepuff", "bias": 0, "value": {}}
    }
    return result;

if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error")
        exit(1)
    createDBFile();
    subjectChosen = ["Arithmancy", "Astronomy", "Herbology", "Muggle Studies"];
    thetaHouse = logreg_train(features, personal_info, course_name, subjectChosen);
    updateData(subjectChosen, thetaHouse);
    os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);
