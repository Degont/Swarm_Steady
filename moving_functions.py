"""The objective of this file is to create a function that allows for the calculation of a path between two points and applying it to a moving object"""

def path_finder(pos_o, pos_f):
    """takes two points and charts path between them"""
    x_mag = pos_o[0]-pos_f[0]
    y_mag = pos_o[1]-pos_f[1]
    slope = (y_mag/x_mag)
