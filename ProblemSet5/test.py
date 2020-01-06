# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:54:44 2020

@author: liujiang
"""
import string
def is_phrase_in(phrase,text):
    num1=0
    num2=0
    boolean=False
    #phrase=PhraseTrigger.get_phrase(self)
    lower_phrase=phrase.lower()
    lower_text=text.lower()
    for i in string.punctuation:
        lower_text=lower_text.replace(i,' ')
    split_text=lower_text.split()
    split_phrase=lower_phrase.split()
    for i in split_phrase:
        if i in split_text:
            num1 += 1
    if num1==len(split_phrase):
        num2 += 1
    join_phrase=''.join(split_phrase)
    join_text=''.join(split_text)
    if join_phrase in join_text:
        num2 += 1
    if num2==2:
        boolean=True
    return boolean

def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    triggerlist=[]
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    dic1={'TITLE':TitleTrigger,'DESCRIPTION':DescriptionTrigger,'AFTER':AfterTrigger,'BEFORE':BeforeTrigger,'OR':OrTrigger,'NOT':NotTrigger,'AND':AndTrigger}
    dic2={}
    for i in lines:
        split_line=i.split(',')
        if split_line[0]!='ADD':
            if split_line[1]=='AND' or split_line[1]=='OR':
                dic2[split_line[0]]=dic1[split_line[1]](dic2[split_line[2]],dic2[split_line[3]])
            else:
                dic2[split_line[0]]=dic1[split_line[1]](split_line[2])
        else:
            for j in range(1,len(split_line)):
                triggerlist.append(dic2[split_line(j)])
    return triggerlist
    print(lines) # for now, print it so you see what it contains!