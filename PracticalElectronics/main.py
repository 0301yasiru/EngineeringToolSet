import argparse

argument_parser = argparse.ArgumentParser(description="Practical Electronic Components")
argument_parser.add_argument('-c', '--component', type=str, help="Path to the component list")

args = argument_parser.parse_args()


def main():
    pass

if __name__ == '__main__':
    main()