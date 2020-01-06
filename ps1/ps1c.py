# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:00:02 2019

@author: liujiang
"""

annual_salary=float(input('enter the starting salary:'))
monthly_salary=float(annual_salary/12)
x=5000
a=0
b=10000
total_cost=1000000
semi_annual_raise=.07
portion_down_payment=float(0.25*total_cost)
current_savings=0
r=0.04
months=0
bisection_search=0
for i in range(1,37):
    current_savings=float(monthly_salary+current_savings*r/12+current_savings)
    months=months+1
    if months%6==0:
        monthly_salary=float(monthly_salary*(1+semi_annual_raise)) 
if current_savings-portion_down_payment>0:
    while abs(current_savings-portion_down_payment)>100:
         current_savings=0
         portion_saved=float(x/10000)
         monthly_salary=float(annual_salary/12)
         for i in range(1,37):
             current_savings=float(portion_saved*monthly_salary+current_savings*r/12+current_savings)
             months=months+1
             if months%6==0:
                 monthly_salary=float(monthly_salary*(1+semi_annual_raise)) 
         if abs(current_savings-portion_down_payment)>100:
            if current_savings-portion_down_payment<0:
                a=x
                x=float((x+b)/2)
            else:
                b=x
                x=float((x+a)/2)
            bisection_search=bisection_search+1
    print('best saving rate:',portion_saved)
    print('steps in bisection search:',bisection_search)      
else:
    print('it is not possible to pay the down payment in three years')

