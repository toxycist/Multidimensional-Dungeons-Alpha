import codecs
from time import *
from os import system
from keyboard import *

#screen height x screen width - 22 x 75

list_to_update = list()

class Menu():
    def __init__(self):
        self.buttons = []
        self.selected_button = -1
        self.title = ""
        self.additional_info = ""
    
    def select_next(self, name):
        if self.selected_button < len(self.buttons) - 1:
            self.selected_button += 1
        else:
            self.selected_button = 0
        self.display()

    def select_previous(self, name):
        if self.selected_button > 0:
            self.selected_button -= 1
        else:
            self.selected_button = len(self.buttons) - 1
        self.display()
    
    def display(self):
        clear_screen()
        if self.title != "":
            printwb(self.title + "\n" * 4)
        for index, button in enumerate(self.buttons):
            if self.selected_button == index:
                printwb(["[" + button + "]"], border_width_u = 0)
            else:
                printwb(button, border_width_u = 0)
        if self.additional_info != "":
            printwb("\n" * 7, border_width_u = 0)
            printwb(self.additional_info, border_width_u = 0)
    
    def bind(self):
        on_press_key("down", self.select_next)
        on_press_key("up", self.select_previous)

class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.buttons = [read_lines(27, 27), read_lines(29, 29), read_lines(31, 31)]
        self.title = read_lines(23, 23)
        self.additional_info = read_lines(35, 35)

def clear_screen():
    """Clears all text from the screen"""
    sleep(0.5)
    system("cls")

def printwb(string, border_width_l = 4, border_width_u = 2):
    """Prints text with borders at left and up, so it looks cooler. params: string can be str or list(every element must be str and will be printed on a new line), border_width_u: how many lines will separate text from the previous text(the up border of the window), border_width_l: how many lines will separate text from the left border of the window. Returns 0 if all's ok and 1 if string is not list or str."""
    print("\n" * border_width_u)
    if isinstance(string, str):
        print(" " * border_width_l + string)
        return 0
    elif isinstance(string, list):
        for element in string:
            print(" " * border_width_l + element)
        return 0
    else:
        return 1

def read_lines(from_l, to_l):
    """Reads only several lines from a file. params: from_l: from where to start, to_l: where to finish. Returns list of lines or a string if there was only one line to read"""
    list_of_lines = list()
    with codecs.open("Languages/ru-lang.txt", "r", encoding="UTF-8") as f:
        list_of_lines = f.readlines()
        f.close()
    sliced_list_of_lines = list_of_lines[from_l - 1: to_l]
    for line in sliced_list_of_lines:
        sliced_list_of_lines[sliced_list_of_lines.index(line)] = line.strip("\r\n")
    if len(sliced_list_of_lines) == 1:
        return sliced_list_of_lines[0]
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
    pass