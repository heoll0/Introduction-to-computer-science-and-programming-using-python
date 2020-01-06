# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:32:49 2019

@author: liujiang
"""

annual_salary=float(input('enter your annual salary:'))
portion_saved=float(input('enter the percent of your salary to save, as a decimal:'))
total_cost=float(input('enter the cost of your dream house:'))
semi_annual_raise=float(input('enter the semi-annual raise,as a decimal:' ))
portion_down_payment=0.25*total_cost
current_savings=0
monthly_salary=annual_salary/12
r=0.04
months=0
while current_savings<portion_down_payment:
    current_savings=portion_saved*monthly_salary+current_savings*r/12+current_savings
    months=months+1
    if months%6==0:
        monthly_salary=monthly_salary*(1+semi_annual_raise)
print ('numbers of months：',months)