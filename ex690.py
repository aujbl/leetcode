# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:04:59 2021

@author: lee
"""

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps_dict = {}
        for emp in employees:
            emps_dict[emp.id] = [emp.importance, emp.subordinates]
            
        def importance(emps_dict, empid):
            if not emps_dict[empid][1]:
                return emps_dict[empid][0]
            res = emps_dict[empid][0]
            for sub in emps_dict[empid][1]:
                res += importance(emps_dict, sub)
            return res
        return importance(emps_dict, id)