#!/usr/bin/env python
# -♆- coding: utf-8 -♆-
# author: seven_lit 
# name:access_files.py time: 2020/4/14

file_path = r'C:\Users\guoqi\Desktop\learning_python.txt'

with open(file_path) as file_objects:
    # contact = file_objects.read()
    # print(contact.rstrip())
    #
    # for lines in file_objects:
    #     print(lines.rstrip())

    lines = file_objects.readlines()

for line in lines:
    print(line.replace('python', 'C').rstrip())
