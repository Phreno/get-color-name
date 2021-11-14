#!/usr/bin/python3

from colors import COLORS


def print_color(color_name):
    """
    Given a `color_name` (ex: gainsboro) print a square on the console with the given color on background
    """
    color = COLORS[color_name]
    print(color_name, '\x1b[48;2;{};{};{}m\x1b[38;2;{};{};{}m{}\x1b[0m'.format(
        color.r, color.g, color.b,
        color.r, color.g, color.b,
        ' ' * 10
    ))


def parse_args():
    """
    Parse command line arguments
    """
    import argparse
    parser = argparse.ArgumentParser(description='Print colors on the console')
    parser.add_argument('color', nargs='?', default='white', help='Color to print')
    parser.add_argument('-l', '--list', action='store_true', help='List all available colors')
    return parser.parse_args()


def main():
    """
    Main function
    """
    args = parse_args()
    if args.list:
        for color in COLORS:
            print(color)
    else:
        print_color(args.color)


if __name__ == '__main__':
    main()
