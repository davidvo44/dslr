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
    return data.split('\n')

