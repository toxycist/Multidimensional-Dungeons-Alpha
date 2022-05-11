import codecs
from time import *
from os import system

#screen height x screen width - 22 x 75

def printwb(list_of_strings, border_width_l = 4, border_width_u = 2):
    """Prints text with borders at left and up edges of the screen, so it looks cooler"""
    print("\n" * border_width_u)
    for string in list_of_strings:
        print(" " * border_width_l + string, end = "")

def read_lines(from_l, to_l):
    """Reads only several lines from a file"""
    list_of_lines = list()
    with codecs.open("Languages/ru-lang.txt", "r", encoding="UTF-8") as f:
        list_of_lines = f.readlines()
        f.close()
    return list_of_lines[from_l - 1: to_l]

printwb(read_lines(1, 6), 19, 10)
sleep(1)
system("cls")
printwb(read_lines(8, 13), 19, 10)
sleep(1)
system("cls")
printwb(read_lines(15, 20), 19, 10)
sleep(4)
system("cls")

input()