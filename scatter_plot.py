import utils
import matplotlib.pyplot as plt
import os
import sys
from utils import checkFile_csv


def mean(values):
    if not values:
        return None
    total = 0.0
    for value in values:
        total += value
    return total / len(values)


def pearson_correlation(x_values, y_values):
    if len(x_values) != len(y_values) or len(x_values) < 2:
        return None

    mean_x = mean(x_values)
    mean_y = mean(y_values)
    if mean_x is None or mean_y is None:
        return None

    numerator = 0.0
    sum_x = 0.0
    sum_y = 0.0

    for i in range(len(x_values)):
        dx = x_values[i] - mean_x
        dy = y_values[i] - mean_y
        numerator += dx * dy
        sum_x += dx * dx
        sum_y += dy * dy

    if sum_x == 0 or sum_y == 0:
        return None

    return numerator / ((sum_x ** 0.5) * (sum_y ** 0.5))

def ft_abs(value):
    if value < 0:
        return -value
    return value

def scatter_plot(features, personal_info, course_name):
    if features is None or personal_info is None or course_name is None:
        print("Error: Failed to load data")
        return None

    count = len(features)
    house_personal = personal_info[0]

    best_corr = None
    best_i = None
    best_j = None
    best_house_x = None
    best_house_y = None

    for i in range(count):
        for j in range(i + 1, count):
            features_data_x = features[i]
            features_data_y = features[j]

            lenn = len(features_data_x)
            if len(features_data_y) < lenn:
                lenn = len(features_data_y)
            if len(house_personal) < lenn:
                lenn = len(house_personal)


            x_values = []
            y_values = []
            all_value_x = {house: [] for house in utils.HOUSE_ORDER}
            all_value_y = {house: [] for house in utils.HOUSE_ORDER}

            for k in range(lenn):
                if features_data_x[k] is None or features_data_y[k] is None:
                    continue
                if house_personal[k] not in utils.HOUSE_ORDER:
                    continue

                house = house_personal[k]
                x_val = features_data_x[k]
                y_val = features_data_y[k]

                x_values.append(x_val)
                y_values.append(y_val)
                all_value_x[house].append(x_val)
                all_value_y[house].append(y_val)

            corr = pearson_correlation(x_values, y_values)
            if corr is None:
                continue

            if best_corr is None or ft_abs(corr) > ft_abs(best_corr):
                best_corr = corr
                best_i = i
                best_j = j
                best_house_x = all_value_x
                best_house_y = all_value_y

    if best_i is None or best_j is None:
        print("No valid pair of features found")
        return None

    os.makedirs("scatter_plots", exist_ok=True)

    plt.figure(figsize=(10, 6))
    for house in utils.HOUSE_ORDER:
        plt.scatter(
            best_house_x[house],
            best_house_y[house],
            color=utils.HOUSE_COLORS[house],
            label=house,
            alpha=0.7
        )

    plt.legend()
    plt.title(
        f"Scatter plot of {course_name[best_i]} and {course_name[best_j]}\n"
    )
    plt.xlabel(course_name[best_i])
    plt.ylabel(course_name[best_j])
    plt.tight_layout()
    plt.savefig("scatter_plots/scatter_plot.png")
    plt.close()

    print(f"Most similar features: {course_name[best_i]} and {course_name[best_j]}")

    return course_name[best_i], course_name[best_j], best_corr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error argument file")
    else:
        if checkFile_csv(sys.argv[1]) is True:
            features, personal_info, course_name = utils.parse_csv(sys.argv[1])
            if features is None or personal_info is None or course_name is None:
                print("Error: Failed to load data")
                exit(1)
            scatter_plot(features, personal_info, course_name)