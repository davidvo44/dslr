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

def pair_plot(features, personal_info, course_name):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    count = len(features)
    os.makedirs('pair_plots', exist_ok=True)
    fig, axes = plt.subplots(count, count, figsize=(13*4, 13*4))

    for row in range(count):
        for col in range(count):
            ax = axes[row][col]
            if col > row:
                ax.set_axis_off()
                continue
            house_personal = personal_info[0]
            if row == col:
                for house in HOUSE_ORDER:
                    house_vals = [v for v in features[row] if v is not None and house_personal[v] == house]
                    ax.hist(house_vals, density=True, alpha=0.5, color=HOUSE_COLORS[house],bins=10)
                continue
            features_data_x = features[col]
            features_data_y = features[row]
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
            for house in HOUSE_ORDER:
                ax.scatter(all_value_x[house], all_value_y[house], color=HOUSE_COLORS[house])
    plt.tight_layout()
    plt.savefig(f'pair_plots/pair_plot.png')
    plt.close()
    return None


if __name__ == "__main__":
    file_path = "datasets/dataset_train.csv"
    features, personal_info, course_name = utils.parse_csv(file_path)
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        exit(1)
    pair_plot(features, personal_info, course_name)