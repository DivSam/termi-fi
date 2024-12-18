import argparse
from parser_utils import get_argument_parser


def main():
    args = get_argument_parser().parse_args()
    print(f'Logging the purchase: {args.purchase}')


if __name__ == '__main__':
    main()
