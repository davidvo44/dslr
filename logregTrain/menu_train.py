
from InquirerPy import inquirer
import os
import stat

def createDBFile():
    db_path = "datasets/db.csv"
    fileBuffer = """House,Bias,Arithmancy,Astronomy,Herbology,"Defense Against the Dark Arts",Divination,"Muggle Studies","Ancient Runes","History of Magic",Transfiguration,Potions,"Care of Magical Creatures",Charms,Flying
"""
    try:
        with open(db_path, 'w') as f:
            f.write(fileBuffer)
            return
    except Exception as e:
        os.chmod(db_path, stat.S_IRWXU | stat.S_IRWXG |stat.S_IRWXO)
        try:
            choice = resetFileChoice()
        except KeyboardInterrupt:
            click.echo(click.style(f"\nForce Quit...", fg='red'))
            return 
        if choice == "Yes":
            with open(db_path, 'w') as f:
                f.write(fileBuffer)

def houseStatInterface():
    result = {
        "Ravenclaw": {"index": "Ravenclaw", "bias": 0, "value": {}},
        "Slytherin":  {"index": "Slytherin", "bias": 0, "value": {}},
        "Gryffindor":  {"index": "Gryffindor", "bias": 0, "value": {}},
        "Hufflepuff":  {"index": "Hufflepuff", "bias": 0, "value": {}}
    }
    return result

def selectMenu():
    return inquirer.select(
        message="\n\nYour choice ?",
        choices=["Subject Choice", "Predefined Subject", "Quit"]
    ).execute()

def resetFileChoice():
    return inquirer.select(
        message="\n\nDatabase found, do you want to reset it",
        choices=["Yes", "No"]
    ).execute()


def selectSubject():
    chosenSubject = []
    subjectList = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]
    try:
        while True:
            choice = getSubject(subjectList)
            if choice == "Done":
                return chosenSubject
            subjectList.remove(choice)
            chosenSubject.append(choice)
            click.echo(click.style(f"\nChosen Subject: {chosenSubject}", fg='green'))
        
    except:
        click.echo(click.style(f"\nForce Quit...", fg='red'))
        return []


def getSubject(subjectList):
    choicesAdd = []
    for subject in  subjectList:
        choicesAdd.append(subject)
    choicesAdd.append("Done")
    return inquirer.select(
        message="\n\nSelect Your Subject ?",
        choices = choicesAdd
    ).execute()

