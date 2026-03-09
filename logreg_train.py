import utils

HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "brown",
    "Ravenclaw": "yellow",
    "Slytherin": "green",
    }

def logreg_train(features, personal_info, course_name):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    all_theta_house = {}
    count = len(features)
    feat_idx = [1, 4, 7, 9]
    learning_rate = 0.01

    m = len(personal_info)
    for i in m:
        house = personal_info[2]

def score_lineaire(student, poid): #formule theta^t * x
    count = len(student)
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


if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error")
        exit(1)
    logreg_train(features, personal_info, course_name)