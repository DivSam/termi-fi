import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description='Processing personal finance via the command line')
    parser.add_argument('--purchase', type=str,
                        help='Add a purchase to the spreadsheet', required=True)

    return parser
