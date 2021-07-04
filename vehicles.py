#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def check_needed_places():
        # перевірка необхідної кількості та типу парковочних місць
        pass


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("motorcycle")


class Car(Vehicle):
    def __init__(self):
        super().__init__("car")


class Bus(Vehicle):
    def __init__(self):
        super().__init__("bus")
