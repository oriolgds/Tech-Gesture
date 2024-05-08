import random
from color_convert import *

classNames = ["A", "B", "C", "D", "E", "F", "G", "H", "HOLA", "I", "J", "K", "L", "LOVE", "M", "N", "NEGRO", "NO", "O", "P", "Q", "R", "S", "SÍ", "T", "U", "V", "W", "X", "Y"]
classColors = {}


colorPalette = ["#F9B5AC", "#AFA2FF", "#BAF2D8", "#7A5C58", "#FFC1000", "#9AA798"]

for i in range(len(classNames)):
    classColors[i] = hex_to_bgr(colorPalette[i % len(colorPalette)])

