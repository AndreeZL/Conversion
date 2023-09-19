import math


class Conversion:
    def grados_a_radianes(grados):
        radianes = grados * (math.pi / 180)
        return radianes

    def radianes_a_grados(radianes):
        grados = radianes * (180 / math.pi)
        return grados