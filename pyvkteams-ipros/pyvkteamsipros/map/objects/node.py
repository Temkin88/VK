from pyvkteamsipros.map.enums import Tag


class Node:
    def __init__(self, istr):
        tset = istr.getTlvset()
        self.name = tset[Tag.NODE_NAME].getAll()
