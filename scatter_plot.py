import utils
import matplotlib.pyplot as plt
import os

HOUSE_COLORS = {
    "Gryffindor": "red",
    "Hufflepuff": "blue",
    "Ravenclaw": "purple",
    "Slytherin": "green",
    }

HOUSE_ORDER = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def scatter_plot(features, personal_info, course_name):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    count = len(features)

    os.makedirs('scatter_plots', exist_ok=True)
    for i in range(count):
        for y in range(i+1, count):
            features_data_x = features[i]
            features_data_y = features[y]
            house_personal = personal_info[0]
            len_x = len(features_data_x)
            len_y = len(features_data_y)
            lenn = 0
            if len_x > len_y:
                lenn = len_y
            else:
                lenn = len_x
            all_value_x = {value: [] for value in HOUSE_ORDER}
            all_value_y = {value: [] for value in HOUSE_ORDER}
            for j in range(lenn):
                if features_data_x[j] is None or features_data_y[j] is None:
                    continue
                if house_personal[j] not in HOUSE_ORDER:
                    continue
                house = house_personal[j]
                all_value_x[house].append(features_data_x[j])
                all_value_y[house].append(features_data_y[j])
            plt.figure(figsize=(10, 6))
            for house in HOUSE_ORDER:
                plt.scatter(all_value_x[house], all_value_y[house], color=HOUSE_COLORS[house], label=house)
            plt.legend()
            plt.title(f'Scatter plot of {course_name[i]} and {course_name[y]}')
            plt.xlabel(course_name[i])
            plt.ylabel(course_name[y])
            plt.savefig(f'scatter_plots/{course_name[i]}_and_{course_name[y]}.png')
            plt.close()

if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None:
        print("Error: Failed to load data")
        exit(1)
    scatter_plot(features, personal_info, course_name)