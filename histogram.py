import utils
import matplotlib.pyplot as plt
import os


def histogram(features, personal_info):
    if features is None or personal_info is None:
        print("Error: Failed to load data")
        return None

    count = len(features)
    HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "gold",
    "Ravenclaw": "blue",
    "Slytherin": "green",
    }
    HOUSE_ORDER = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

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
        plt.figure(figsize=(10, 6))
        for house in HOUSE_ORDER:
            plt.hist(house_data[house], bins=10, color=HOUSE_COLORS[house], alpha=0.7, label=house)
        plt.title(f'Histogram of {features[i]}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig(f"histograms/histogram_{i+1}.png")
        plt.close()


if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info = utils.parse_csv(file_path)
    if features is None or personal_info is None :
        print("Error: Failed to load data")
        exit(1)
    histogram(features, personal_info)



