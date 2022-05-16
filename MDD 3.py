import codecs
from time import *
from os import system
from keyboard import *

#screen height x screen width - 22 x 75

list_to_update = list()

class MainMenu():
    def __init__(self):
        self.buttons = [read_lines(27, 27), read_lines(29, 29), read_lines(31, 31)]
        self.selected_button = -1

    def select_next(self, name):
        if self.selected_button < 2:
            self.selected_button += 1
        else:
            self.selected_button = 0
        self.display()

    def select_previous(self, name):
        if self.selected_button > 0:
            self.selected_button -= 1
        else:
            self.selected_button = 2
        self.display()

    def display(self):
        clear_screen()
        printwb(true_append(read_lines(23, 23), "\n" * 2))
        for index, button in enumerate(self.buttons):
            if self.selected_button == index:
                printwb(["[" + button[0] + "]"])
            else:
                printwb(button)
        printwb(true_append(["\n" * 2], read_lines(35, 35)[0]))
    
    def bind(self):
        on_press_key("down", self.select_next)
        on_press_key("up", self.select_previous)

def clear_screen():
    """Clears all text from the screen"""
    sleep(0.5)
    system("cls")

def printwb(list_of_strings, border_width_l = 4, border_width_u = 2):
    """Prints text with borders at left and up edges of the screen, so it looks cooler. Returns 0 if all's ok and 1 if list_of_strings == None"""
    print("\n" * border_width_u)
    if list_of_strings != None:
        for string in list_of_strings:
            print(" " * border_width_l + string)
        return 0
    else:
        return 1

def read_lines(from_l, to_l):
    """Reads only several lines from a file"""
    list_of_lines = list()
    with codecs.open("Languages/ru-lang.txt", "r", encoding="UTF-8") as f:
        list_of_lines = f.readlines()
        f.close()
    sliced_list_of_lines = list_of_lines[from_l - 1: to_l]
    for line in sliced_list_of_lines:
        sliced_list_of_lines[sliced_list_of_lines.index(line)] = line.strip("\r\n")
    return sliced_list_of_lines

def true_append(list, element):
    """Appends an element to the list and returns THE NEW LIST"""
    list.append(element)
    return list

def display_loading_screen():
    """Displays loading screen"""
    printwb(read_lines(1, 6), 19, 10)
    clear_screen()
    printwb(read_lines(8, 13), 19, 10)
    clear_screen()
    printwb(read_lines(15, 20), 19, 10)
    sleep(1.5)
    clear_screen()

display_loading_screen()
main_menu = MainMenu()

main_menu.display()
main_menu.bind()

while True:
    input()