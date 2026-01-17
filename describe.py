import click
import time
from click.testing import CliRunner
from InquirerPy import inquirer
import pandas as pd

@click.command()

def main():
    try:
        while True:
            choice = selectMenu()
            if choice == "House Stat":
                houseStat()
            # elif choice == "New Data":
            #     newData()
            # elif choice == "Graph":
            #     createGraph()
            elif choice == "Quit":
                break
            # UpdateTheta();
    except KeyboardInterrupt:
        print("\n...Leaving....");
    except click.exceptions.Abort:
        print("\n...Leaving....");

def selectMenu():
    return inquirer.select(
        message="\n\nYour choice ?",
        choices=["House Stat", "Subject Stat", "Personal Info Stat", "Quit"]
    ).execute()


def houseStat():
    click.echo(click.style(f"\nEstimate Price for the car is", fg='green'));
    return;

if __name__ == '__main__':
    main()