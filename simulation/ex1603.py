# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 08:08:25 2021

@author: lee
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.par = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.par[carType-1] == 0:
            return False
        else:
            self.par[carType-1] -= 1
            return True
        



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)