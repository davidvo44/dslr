from utils import ft_sqrt

def logreg_mean(value):
    m = len(value)
    result = 0
    j = 0
    for i in range(len(value)):
        if value[i] is not None:
            result += value[i]
            j += 1
    return result / j

def logreg_standard_deviation(value):
    mean = logreg_mean(value)
    result = 0
    j = 0
    for i in range(len(value)):
        if value[i] is not None:
            result += (value[i] - mean) ** 2
            j += 1
    return (ft_sqrt(result / j), mean)

def logreg_normalized_value(value):
    standard_deviation, mean = logreg_standard_deviation(value)
    X = []
    result = 0
    for i in range(len(value)):
        if value[i] is not None:
            result = (value[i] - mean) / standard_deviation
            X.append(result)
        else:
            X.append(None)
    return (X, standard_deviation, mean)