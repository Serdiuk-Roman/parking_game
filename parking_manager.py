#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import random

from vehicles import Motorcycle, Car, Bus
from places import Mini_place, Compact_place, Large_place


class Parking:
    def __init__(self, height=5, width=12):
        self.height = height
        self.width = width
        self.field = []
        self.cell_types_list = [Mini_place, Compact_place, Large_place]
        self.free_place = {}

    def gen_field(self):
        # Генерує матрицю і заповнює лічильник вільних місць
        for row in range(self.height):
            self.field.append([])
            index = row % len(self.cell_types_list)
            cell_type = self.cell_types_list[index]
            for cell in range(self.width):
                cell_obj = cell_type()
                self.field[row].append(cell_obj)
                cell_obj.__class__.add_total_free_places()


    def counter_of_free_places(self):
        for i in self.cell_types_list:
            print(
                i,
                " = ",
                i.get_total_free_places()
            )

    def show_field(self):
        pass

    def counter_of_vehicles(self):
        pass

    def check_availability(self, vehicle):
        pass

    def show_message(self):
        pass



if __name__ == "__main__":
    p = Parking()
    p.gen_field()
    for i in p.field:
        print(i)

    p.counter_of_free_places()
