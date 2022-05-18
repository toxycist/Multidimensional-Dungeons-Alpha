import codecs
from time import *
from os import system
from keyboard import *
from importlib import *

with open("current-lang.txt") as file:
    language = import_module(file.readline())

#screen height x screen width - 22 x 75

class Button():
    def __init__(self, name, command):
        self.name = name
        self.command = command

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
                printwb(["[" + button.name + "]"], border_width_u = 0)
            else:
                printwb(button.name, border_width_u = 0)
        if self.additional_info != "":
            printwb("\n" * 7, border_width_u = 0)
            printwb(self.additional_info, border_width_u = 0)
    
    def button_do(self, name):
        if self.selected_button != -1:
            self.buttons[self.selected_button].command()
    
    def activate_menu(self):
        self.remove_handler_down = on_press_key("down", self.select_next)
        self.remove_handler_up = on_press_key("up", self.select_previous)
        self.remove_handler_enter = on_press_key("enter", self.button_do)
        self.display()
    
    def deactivate_menu(self):
        self.remove_handler_down()
        self.remove_handler_up()
        self.remove_handler_enter()

def change_language(nextl):
    with open("current-lang.txt", "w") as file:
        file.write(nextl)
    global language
    language = import_module(nextl)
    clear_screen()
    printwb(language.restart_to_change_the_language_message)

class LanguageMenu(Menu):
    def __init__(self):
        super().__init__()
        self.buttons = [Button(language.language_menu_ru, lambda: change_language("ru")), 
                        Button(language.language_menu_en, lambda: change_language("en")), 
                        Button(language.language_menu_de, lambda: change_language("de")),
                        Button(language.language_menu_back, lambda: change_menu(self, main_menu))]
        self.title = language.main_menu_language

language_menu = LanguageMenu()

class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.buttons = [Button(language.main_menu_new_game, input), 
                        Button(language.main_menu_saved_game, input), 
                        Button(language.main_menu_language, lambda: change_menu(self, language_menu))]
        self.title = language.main_menu_title
        self.additional_info = language.main_menu_credits

main_menu = MainMenu()

def change_menu(previousm, nextm):
    previousm.deactivate_menu()
    nextm.activate_menu()

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

def true_append(list, element):
    """Appends an element to the list and returns the new list"""
    list.append(element)
    return list

def display_loading_screen():
    """Displays loading screen"""
    printwb(language.loading_screen_phase1, 19, 10)
    clear_screen()
    printwb(language.loading_screen_phase2, 19, 10)
    clear_screen()
    printwb(language.loading_screen_phase3, 19, 10)
    sleep(1.5)
    clear_screen()

display_loading_screen()

main_menu.activate_menu()

while True:
    pass