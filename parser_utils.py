import argparse


def get_argument_parser():
    parser = argparse.ArgumentParser(
        description='Processing personal finance via the command line')
    parser.add_argument('--purchase', type=str,
                        help='Add a purchase to the spreadsheet', required=False)
    parser.add_argument('--name', type=str, help='Name of the purchase',
                        required=True)
    parser.add_argument('--amount', type=float,
                        help='Amount of the purchase', required=True)
    parser.add_argument('--category', type=str,
                        # todo this needs to be a part of a specific list
                        help='Category of the purchase', required=True)
    parser.add_argument('--date', type=str, help='Date of the purchase',
                        required=False)  # todo this needs to be a specific format, default to the current date

    return parser
