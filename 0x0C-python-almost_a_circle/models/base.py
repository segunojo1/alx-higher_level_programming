"""Base class model for the rest of the project"""
class Base:
    """class instanc of the basee"""
    __nb_objects = 0
        def __init__(self, id=None):
            """initialization of the base class"""
            if id is not None:
                self.id = id
            else:
                __nb_objects = __nb_objects + 1
                self.id = __nb_objects