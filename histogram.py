import utils
import matplotlib.pyplot as plt
import sys
import os
from utils import COLUMN_ORDER, checkFile_csv

HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "brown",
    "Ravenclaw": "yellow",
    "Slytherin": "green",
    }

HOUSE_ORDER = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def min_note(all_note):
    min_note = all_note[0]
    for note in all_note:
        if note < min_note:
            min_note = note
    return min_note

def max_note(all_note):
    max_note = all_note[0]
    for note in all_note:
        if note > max_note:
            max_note = note
    return max_note


def calculate_mean(features, personal_info):
    nb_features = len(features)

    count = {house: [0.0 for _ in range(nb_features)] for house in HOUSE_ORDER}
    mean_house = {house: [0.0 for _ in range(nb_features)] for house in HOUSE_ORDER}

    for i in range(nb_features):
        for j in range(len(features[i])):
            feature = features[i][j]
            if feature is None:
                continue
            house = personal_info[0][j]
            if house not in mean_house:
                continue
            mean_house[house][i] += feature
            count[house][i] += 1
    for house in HOUSE_ORDER:
        for j in range(len(mean_house[house])):
            if count[house][j] != 0:
                mean_house[house][j] = mean_house[house][j] / count[house][j]
            else:
                mean_house[house][j] = None
    
    return mean_house

def calculate_mean_by_feature_by_house(mean_house, features, course_name):
    nb_features = len(features)

    mean_feature_house = [0.0 for _ in range(nb_features)]
    variance = [None for _ in range(nb_features)]

    for i in range(nb_features):
        valid_houses = 0
        for house in HOUSE_ORDER:
            if mean_house[house][i] is not None:
                mean_feature_house[i] += mean_house[house][i]
                valid_houses += 1
        if valid_houses != 0:
            mean_feature_house[i] = mean_feature_house[i] / valid_houses
        else:
            mean_feature_house[i] = None

    for i in range(nb_features):
        if mean_feature_house[i] is None:
            continue
        count_house = 0
        variance_sum = 0.0
        for house in HOUSE_ORDER:
            if mean_house[house][i] is not None:
                variance_sum += (mean_house[house][i] - mean_feature_house[i]) ** 2
                count_house += 1
        if count_house != 0:
            variance[i] = variance_sum / count_house

    small = None
    feature = None
    for i in range(nb_features):
        if variance[i] is None:
            continue
        if small is None or variance[i] < small:
            small = variance[i]
            feature = i

    if feature is None:
        return None
    return course_name[feature], variance


def histogram(features, personal_info, course_name, best_course, variance):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None
    if best_course is None:
        print("Error: No best course found")
        return None

    os.makedirs("histograms", exist_ok=True)

    course_index = None
    for i in range(len(course_name)):
        if course_name[i] == best_course:
            course_index = i
            break

    if course_index is None:
        print("Error: Best course not found in course_name")
        return None

    features_data = features[course_index]
    house_personal = personal_info[0]
    house_data = {house: [] for house in HOUSE_ORDER}

    for student in range(len(features_data)):
        if features_data[student] is None:
            continue
        house = house_personal[student]
        if house not in HOUSE_ORDER:
            continue
        house_data[house].append(features_data[student])

    all_note = [v for v in features_data if v is not None]
    if not all_note:
        print("Error: No valid data for best course")
        return None

    min_value = min_note(all_note)
    max_value = max_note(all_note)
    if min_value == max_value:
        print("Error: All values are identical")
        return None

    bin_edges = [min_value + i * (max_value - min_value) / 25 for i in range(26)]

    plt.figure(figsize=(10, 6))
    for house in HOUSE_ORDER:
        plt.hist(
            house_data[house],
            bins=bin_edges,
            color=HOUSE_COLORS[house],
            alpha=0.5,
            label=house,
        )

    plt.title(f'Histogram of {best_course} variance {variance[course_index]}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig("histograms/best_course.png")
    plt.close()



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error argument file")
    else:
        if (checkFile_csv(sys.argv[1])== True):
            features, personal_info, course_name = utils.parse_csv(sys.argv[1])
            if features is None or personal_info is None :
                print("Error: Failed to load data")
                exit(1)
            
            mean_house = calculate_mean(features, personal_info)
            best_course, variance = calculate_mean_by_feature_by_house(mean_house, features, course_name)
            histogram(features, personal_info, course_name, best_course, variance)
            print(best_course)