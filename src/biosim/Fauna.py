# -*- coding: utf-8 -*-

__author__ = "Anders Huse, Bishnu Poudel"
__email__ = "anhuse@nmbu.no; bipo@nmbu.no"

from biosim.Geography import Geo

class Fauna:
    def __init__(self,  position, Land_type, age=0):
        self.age = age
<<<<<<< HEAD

    def feeding(self):
        pass

    def fitness(self):
        pass

    def migration(self):
        pass

    def procreation(self):
        pass

    def aging(self):
        pass

    def loss_of_weigth(self):
        pass

    def death(self):
        pass


class Herbevoir(Fauna):
    """Animals with herbevoir characteristics"""
    params_herb = {
        "w_birth": 8.0,
        "sigma_birth": 1.5,
        "beta": 0.9,
        "eta": 0.05,
        "a_half": 40.0,
        "phi_age": 0.2,
        "w_half": 10.0,
        "phi_weight": 0.1,
        "mu": 0.25,
        "lambda": 1.0,
        "gamma": 0.2,
        "zeta": 3.5,
        "xi": 1.2,
        "omega": 0.4,
        "F": 10.0,
    }
    def __init__(self, params_herbs):
        self.params_herbs = params_herbs

        super().__init__()


class Carnevoir(Fauna):
    """Animals with carnevoir characteristics"""
    params_carn = {
        "w_birth": 6.0,
        "sigma_birth": 1.0,
        "beta": 0.75,
        "eta": 0.125,
        "a_half": 60.0,
        "phi_age": 0.4,
        "w_half": 4.0,
        "phi_weight": 0.4,
        "mu": 0.4,
        "lambda": 1.0,
        "gamma": 0.8,
        "zeta": 3.5,
        "xi": 1.1,
        "omega": 0.9,
        "F": 50.0,
        "DeltaPhiMax": 10.0
    }
    def __init__(self, params_carn):
        self.params_carn = params_carn

        super().__init__()
=======
        self.position = position
        self.Land_type= Land_type

class Herbivore(Fauna):
    """Herbivores"""
    def __init__(self,position, Land_type,  age=0 ):
        super().__init__(position, Land_type,age)


if __name__ == "__main__":
    g = Geo("""\
       OOOOOOOOOOOOOOOOOOOOO
       OOOOOOOOJMMMMJJJJJJJO
       OSSSSSJJJJJJJJJJJJJOO
       OOOOOOOOOOOOOOOOOOOOO""")

    ini_herbs = {'loc': (10, 10), \
                'pop': [{'species': 'Herbivore', \
                'age': 5, \
                'weight': 20} \
                for _ in range(150)] }
    print(ini_herbs['loc'])
    print(ini_herbs['pop'][149])
    # print(ini_herbs[0])
    # print(ini_herbs['pop'])

    # for row_num, row_list in enumerate(g.geo_ob_array):
    #     print(row_num,row_list)
    #     for column_num, obj in enumerate(row_list):
    #         if obj.is_migratable:
    #             H = Herbivore((row_num,column_num), type(obj).__name__ )
    #             print (H.age)
>>>>>>> master
