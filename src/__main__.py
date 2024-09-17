import sys
from src.cli import cli
from src.gui import gui


def main():
    if len(sys.argv) > 1:
        cli()
    else:
        gui()


if __name__ == "__main__":
    main()
