# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:05:06 2019

@author: liujiang
"""

annual_salary=float(input('enter your annual salary:'))
portion_saved=float(input('enter the percent of your salary to save, as a decimal:'))
total_cost=float(input('enter the cost of your dream house:'))
portion_down_payment=0.25*total_cost
current_savings=0
monthly_salary=annual_salary/12
r=0.04
months=0
while current_savings<portion_down_payment:
    current_savings=portion_saved*monthly_salary+current_savings*r/12+current_savings
    months=months+1
print ('numbers of months：',months)