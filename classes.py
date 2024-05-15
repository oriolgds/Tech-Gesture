import random
from color_convert import *

classNames = ["A", "AMANECER", "ANGUSTIA", "B", "BRONZE", "C", "D", "E", "ESCRIBIR", "F", "G", "GRACIAS", "H", "HOLA", "I", "J", "JUEVES", "K", "L", "LOVE", "M", "MIERCOLES", "N", "NEGRO", "NO", "O", "P", "PAZ", "Q", "QUERER", "R", "S", "SÍ", "T", "TECH GESTURE", "TRABAJAR", "TU", "U", "V", "W", "X", "Y"]
classColors = {}


colorPalette = ["#F9B5AC", "#AFA2FF", "#BAF2D8", "#7A5C58", "#FFC1000", "#9AA798"]

for i in range(len(classNames)):
    classColors[i] = hex_to_bgr(colorPalette[i % len(colorPalette)])

