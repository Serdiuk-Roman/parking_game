#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vehicle:
    def __init__(self, vehicle_type, size = 1):
        self.vehicle_type = vehicle_type
        self.size = size

    def check_needed_places(self):
        # перевірка необхідної кількості та типу парковочних місць
        pass


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("motorcycle", 1)


class Car(Vehicle):
    def __init__(self):
        super().__init__("car", 1)


class Bus(Vehicle):
    def __init__(self):
        super().__init__("bus", 5)
