#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from vehicles import Motorcycle, Car, Bus

class Place:
    
    NUMBER_FREE_PLACES = 0

    def __init__(self, type_of_place, short_label, available_list = []):
        self.type_of_place = type_of_place
        self.short_label = short_label
        self.free = True
        self.available_list = available_list
        self.vehicle = None
       
    @classmethod
    def add_number_free_places(cls):
        cls.NUMBER_FREE_PLACES += 1
       
    @classmethod
    def reduce_number_free_places(cls):
        cls.NUMBER_FREE_PLACES -= 1

    @classmethod
    def get_number_free_places(cls):
        return cls.NUMBER_FREE_PLACES

    def check_availability(self, vehicle):
        return vehicle.vehicle_type in self.available_list

    def is_free(self):
        return self.free

    def set_free(self, new_status):
        self.free = new_status

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.__class__.reduce_number_free_places()

    def del_vehicle(self):
        self.vehicle = None
        self.__class__.add_number_free_places()

    def __repr__(self):
        return self.short_label


class Mini_place(Place):
    # тільки для мотоциклів
    def __init__(self):
        super().__init__("mini_place", "S", ["motorcycle", ])


class Compact_place(Place):
    # для мотоциклів та автомобілів
    def __init__(self):
        super().__init__("compact_place", "M", ["motorcycle", "car"])


class Large_place(Place):
    # для мотоциклів та автомобілів
    # для автобуса потрібно 5 штук
    def __init__(self):
        super().__init__("large_place", "L", ["motorcycle", "car", "bus"])



if __name__ == "__main__":
    from vehicles import Motorcycle, Car, Bus

    ducati = Motorcycle()
    ford = Car()
    ikarus = Bus()

    space = Mini_place()
    compact_space = Compact_place()
    large_place = Large_place()

    print(space.check_availability(ducati))
    print(space.check_availability(ford))
    print(space.check_availability(ikarus))
    print()

    print(compact_space.check_availability(ducati))
    print(compact_space.check_availability(ford))
    print(compact_space.check_availability(ikarus))
    print()

    print(large_place.check_availability(ducati))
    print(large_place.check_availability(ford))
    print(large_place.check_availability(ikarus))
    print()
