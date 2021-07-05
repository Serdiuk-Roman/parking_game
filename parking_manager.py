#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import random

from vehicles import Motorcycle, Car, Bus
from places import Mini_place, Compact_place, Large_place


class Parking:
    def __init__(self, height=8, width=12):
        self.height = height
        self.width = width
        self.field = []
        self.cell_types_list = [Mini_place, Compact_place, Large_place]

    def gen_field(self):
        # Генерує матрицю і заповнює лічильник вільних місць
        for row in range(self.height):
            self.field.append([])
            index = row % len(self.cell_types_list)
            cell_type = self.cell_types_list[index]
            for cell in range(self.width):
                cell_obj = cell_type()
                self.field[row].append(cell_obj)
                cell_obj.__class__.add_number_free_places()

    def counter_of_free_places(self):
        for i in self.cell_types_list:
            print(
                i,
                " = ",
                i.get_number_free_places()
            )

    def show_field(self):
        for i in self.field:
            row = '{}{}{}{}'.format(
                i[0].short_label,
                " |",
                " ".join([x.vehicle.label if x.vehicle else " " for x in i]),
                " |"
            )
            print(row)

    def check_availability(self, vehicle):
        for row in self.fields:
            counter = 0
            for cell in row:
                if cell.is_free() and cell.check_availability()
                counter += 1
                if counter => vehicle.size:



    def counter_of_vehicles(self):
        pass

    def check_availability(self, vehicle):
        pass

    def show_message(self):
        pass



if __name__ == "__main__":
    p = Parking()
    p.gen_field()
    c = Car()
    d = Motorcycle()
    p.field[1][2].set_vehicle(c)
    p.field[0][0].set_vehicle(d)
    p.show_field()
    p.counter_of_free_places()
