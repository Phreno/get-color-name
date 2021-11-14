#!/usr/bin/python3

import re
import sys

from colors import COLORS
from colors import Color


def get_color_name(color):
    """
    Get the name of a color.
    """
    r, g, b = color
    min_colors = {}
    for key, value in COLORS.items():
        r_c, g_c, b_c = value
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colors[(rd + gd + bd)] = key
    return min_colors[min(min_colors.keys())]


def main():
    """
    Main function.
    """
    color = sys.argv[1]
    if re.match(r'^#?[0-9a-f]{6}$', color, re.IGNORECASE):
        color = color.lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        print(get_color_name(Color(r, g, b)))
    else:
        print('Invalid color')


if __name__ == '__main__':
    main()
