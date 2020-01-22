# -*- coding: utf-8 -*-

import textwrap
import matplotlib.pyplot as plt
from src.biosim.simulation import BioSim
from src.biosim.simulation import Herbivore, Carnivore
from src.biosim.simulation import Jungle, Savannah

"""
Compatibility check for BioSim simulations.

This script shall function with biosim packages written for
the INF200 project January 2019.
"""

__author__ = "Hans Ekkehard Plesser, NMBU"
__email__ = "hans.ekkehard.plesser@nmbu.no"


if __name__ == "__main__":
    plt.ion()

    geogr = """\
               OOOOOOOOOOOOOOOOOOOOO
               OOOOOOOOSMMMMJJJJJJJO
               OSSSSSJJJJMMJJJJJJJOO
               OSSSSSSSSSMMJJJJJJOOO
               OSSSSSJJJJJJJJJJJJOOO
               OSSSSSJJJDDJJJSJJJOOO
               OSSJJJJJDDDJJJSSSSOOO
               OOSSSSJJJDDJJJSOOOOOO
               OSSSJJJJJDDJJJJJJJOOO
               OSSSSJJJJDDJJJJOOOOOO
               OOSSSSJJJJJJJJOOOOOOO
               OOOSSSSJJJJJJJOOOOOOO
               OOOOOOOOOOOOOOOOOOOOO"""
    geogr = textwrap.dedent(geogr)

    ini_herbs = [
        {
            "loc": (10, 10),
            "pop": [
                {"species": "Herbivore", "age": 5, "weight": 20}
                for _ in range(100)
            ],
        }
    ]
    ini_carns = [
        {
            "loc": (10, 10),
            "pop": [
                {"species": "Carnivore", "age": 5, "weight": 20}
                for _ in range(100)
            ],
        }
    ]
    # Should specify the total_years
    sim = BioSim(island_map=geogr, ini_pop=ini_herbs, seed=123456,
                 total_years = 500, img_base='Raw_Images', cmax_animals=
                 {'Herbivore': 100, 'Carnivore': 100})

    sim.set_animal_parameters("Herbivore", {"zeta": 3.2})
    sim.set_animal_parameters(
        "Carnivore",
        {
            "a_half": 70,
            "phi_age": 0.5,
            "omega": 0.3,
            "F": 65,
            "DeltaPhiMax": 9.0,
        },
    )
    # print(Carnivore.animal_params)
    # print(Herbivore.animal_params)

    # print(Savannah.parameters)
    sim.set_landscape_parameters("S", {'f_max': 200 })
    # print(Savannah.parameters)

    sim.simulate(num_years=15, vis_years=1, img_years=1)
    sim.add_population(population=ini_carns)
    sim.simulate(num_years=150, vis_years=1, img_years=1)
    sim.make_movie()

    plt.savefig("check_sim.pdf")

    input("Press ENTER")
