import utils
import matplotlib.pyplot as plt
import os

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


def histogram(features, personal_info, course_name):
    if features is None or personal_info is None:
        print("Error: Failed to load data")
        return None

    count = len(features)

    os.makedirs("histograms", exist_ok=True)
    for i in range(count):
        features_data = features[i]
        house_personal = personal_info[0]
        house_data = {house: [] for house in HOUSE_ORDER}

        if not features[i]:
            continue
        for student in range(len(features_data)):
            if features_data[student] is None:
                continue

            house = house_personal[student]
            if house not in HOUSE_ORDER:
                continue
            house_data[house].append(features_data[student])
        all_note = [v for v in features_data if v is not None]
        if not all_note:
            continue
        min_value = min_note(all_note)
        max_value = max_note(all_note)
        if min_value == max_value:
            continue
        bin_edges = [min_value + i * (max_value - min_value) / 10 for i in range(11)] # use the min and max value to create 10 bins ans is the same for all courses
        plt.figure(figsize=(10, 6))
        for house in HOUSE_ORDER:
            plt.hist(house_data[house], bins=bin_edges, color=HOUSE_COLORS[house], alpha=0.7, label=house)
        plt.title(f'Histogram of {course_name[i]}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig(f"histograms/{course_name[i]}.png")
        plt.close()



if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None :
        print("Error: Failed to load data")
        exit(1)
    histogram(features, personal_info, course_name)



