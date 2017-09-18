#!/usr/bin/env python3

import os
from PIL import Image
import webcolors
from pandas import DataFrame

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
    try:
        name = filename.split('/')[-1].split('.')[0]
        color_list = [(count, color_tuple[0], color_tuple[1], color_tuple[2], color_tuple,
                       name, get_colour_name(websafe(color_tuple)))
                      for count, color_tuple in colors_in_flag]
        return color_list
    except:
        pass

def convert_flags_to_values_in_dir(dir):
    z = []
    for filename in os.listdir(dir):
        try:
            z.extend(get_colors_from_flag(dir  + filename))
        except:
            pass
    df = DataFrame(z, columns=['Number of Pixels', 'Red', 'Green', 'Blue', 'RGB', 'Country', 'Color'])
    f = open('data.csv', 'w')
    f.write(df.to_csv())
    f.close()
    return df
