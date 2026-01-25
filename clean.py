import os,stat 

def main():
    try:
        with open("db.csv", 'w') as file:
            return;
    except FileNotFoundError:
        return;
    except Exception as e:
        os.chmod("db.csv", stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO);
    os.remove("db.csv");
    return;

if __name__ == '__main__':
    main()

