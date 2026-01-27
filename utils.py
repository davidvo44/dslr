from pyexpat import features


def open_csv(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

def parse_csv(filepath):
    data = open_csv(filepath)
    if data is None:
        return None
    lines = data.strip().split('\n') # split the data into lines and remove the empty lines
    header = lines[0].split(",")
    course_name = [header[i+6].strip() for i in range(13)] 
    data_lines = lines[1:] # remove the header line
    features = [[] for _ in range(13)] # list of features
    personal_info = [[] for _ in range(6)] # list of personal information
    for line in data_lines:
        cols = line.split(',')
        for i in range(6):
            value = cols[i+1].strip()
            if value:
                personal_info[i].append(value)
            else:
                personal_info[i].append(None)
        for i in range(13):
            value = cols[i+6].strip()
            if value:
                features[i].append(float(value))
            else:
                features[i].append(None)
    return features, personal_info, course_name