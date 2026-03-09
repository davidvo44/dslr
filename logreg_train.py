import utils
import os,stat 
HOUSE_ORDER = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def logreg_train(features, personal_info, course_name):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    all_theta_house = {}
    count = len(features)
    feat_idx = [1, 4, 7, 9]
    learning_rate = 0.01

    m = len(personal_info)
    n = len(feat_idx) + 1
    X = []
    for i in range(m):
        x = [1.0]
        has_None = False
        for idx in feat_idx:
            val = features[i][idx]
            if val is None:
                has_None = True
                break
            x.append(features[i][idx])
        if not has_None:
            X.append(x)
    for house in HOUSE_ORDER:
        y = []
        for i in range(m):
            y.append(1.0 if personal_info[i][2] == house else 0.0)
        theta = [0.0] * n

        theta = grad_descent(X, y, theta, 1000, 0.01)

        all_theta_house[house] = theta
    print("Gryffindor theta:", all_theta_house["Gryffindor"][:5])
    return all_theta_house

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
House,Arithmancy,Astronomy,Herbology,Defense Against the Dark Arts,Divination,Muggle Studies,Ancient Runes,History of Magic,Transfiguration,Potions,Care of Magical Creatures,Charms,Flying\n\
RavenclawBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
RavenclawWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
GryffundorBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
GryffundorWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
SlytherinBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
SlytherinWeight,0,0,0,0,0,0,0,0,0,0,0,0\n\
HufflepuffBias,0,0,0,0,0,0,0,0,0,0,0,0\n\
HufflepuffWeight,0,0,0,0,0,0,0,0,0,0,0,0\n");
            return;
    except Exception as e:
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
        # print("file already exist\n");




# def main(file_path):
#     createDBFile();
#     trainmodel(file_path);
#     os.chmod("db.csv", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH);
#     return;


if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error")
        exit(1)
    logreg_train(features, personal_info, course_name)