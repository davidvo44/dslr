import click
import time
from click.testing import CliRunner
from InquirerPy import inquirer
import pandas as pd
from .houseStat import houseStat
from .subjectStat import subjectStat
from utils import parse_csv

@click.command()
@click.argument("dataset_path", required=False, default="datasets/dataset_train.csv")
def main(dataset_path):
    try:
        while True:
            choice = selectMenu()
            if choice == "House Stat":
                houseStat(dataset_path)
            elif choice == "Subject Stat":
                subjectStat(dataset_path)
            elif choice == "Quit":
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n...Leaving....")
    except click.exceptions.Abort:
        print("\n...Leaving....")

def selectMenu():
    return inquirer.select(
        message="\n\nYour choice ?",
        choices=["House Stat", "Subject Stat", "Quit"]
    ).execute()

if __name__ == "__main__":
    main()