#!/usr/bin/env python3


from PIL import Image
import webcolors

# Pre-calc the wbesafe lookup table
tbl = tuple(51*((int(i)+25)//51) for i in range(256))

def get_colour_name(rgb_triplet):
    """
    Given a color tuple, convert it to a CSS 2.1 name
    """
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def websafe(color_tuple):
    """
    Given a color tuple in RGB space converts them a color tuple of nearest websafe 256 colors
    """
    return tuple(tbl[c] for c in color_tuple)

def get_colors_from_flag(filename):
    colors_in_flag = Image.open(filename).convert("RGB").getcolors()
    return [(count, color_tuple, get_colour_name(websafe(color_tuple))) for count, color_tuple in colors_in_flag
    ]
