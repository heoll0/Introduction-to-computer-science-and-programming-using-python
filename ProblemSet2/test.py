# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:19:19 2019

@author: liujiang
"""

#
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
my_word='te_ t'
other_word='tact'
a=0
b=True
i=0
boolean=False
_number=0
letters_number=0
letters_location=[]
myletters_location=[]
_location=[]
#    for i in range(len(my_word)):
#        if str.isalpha(my_word[i]):
#            letters_number+=1
#            letters_location.append(int(i-_number/2))
#        else:
#            _location.append(int(i-_number/2))
#            _number+=1
while i < len(my_word):
    if str.isalpha(my_word[i]):
        letters_number+=1
        letters_location.append(i-_number)
        myletters_location.append(i)
        i=i+1
    else:
        _location.append(i-_number)
        _number+=1
        i=i+2
word_len=int((len(my_word)-letters_number)/2+letters_number)
if word_len==len(other_word):
    for j in range(len(letters_location)):
        if my_word[myletters_location[j]]==other_word[letters_location[j]]:
            a=a+1
        for k in range(len(_location)):
            if other_word[letters_location[j]]==other_word[_location[k]]:
                b=False
    if b and a==len(letters_location):
        boolean=True
    else:
        boolean=False
