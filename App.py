import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os
from PIL import Image
from HomePage import Page1
from FeaturePage1 import Page2
from FeaturePage2 import Page3
from AboutUsPage import Page4


class App(tk.Tk):

  ################
  # APP SETTINGS #
  ################

  name = "Spruce House"                      # Name of the app
  width = 390                               # Width of the app window
  height = 740                              # Height of the app window
  pages = [ Page1, Page2, Page3, Page4] 
  initial_page = 1                          # Initial page to show, from 1 to upwards

  # Custom styles for the app
  styles = {
    "TITLE": ("Times",50),
    "SECONDTITLE":("Times",30),
    "LARGEFONT": ("Inter", 50),
    "MIDDLEFONT": ("Inter", 25),
    "NORMALFONT": ("Inter", 15),
  }
  
  ###################
  # STATE VARIABLES #
  ###################
  
  # Global selected option example
  selectedFilePath = ""

  #############
  # FUNCTIONS #
  #############

  # Show a certain page, from 1 to upwards
  def show_page(self, page_number : int):
    self.frames.get(page_number).tkraise()
  
  # Get a certain page, from 1 to upwards
  def get_page(self, page_number : int):
    return self.frames.get(page_number)

  ######################
  # INITIALIZE THE APP #
  ######################
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self) 
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    self.geometry(f"{self.width}x{self.height}")
    self.title(self.name)
    self.resizable(False, False)

    # Theme settings for the app
    # https://github.com/TomSchimansky/CustomTkinter/wiki/Themes
    ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    
    # Create all the pages
    self.frames = {}
    i : int = 1
    for F in self.pages:
      frame = F(container, self)
      self.frames[i] = frame
      frame.grid(row = 0, column = 0, sticky ="nsew")
      i = i + 1
    
    # Initial page to show
    self.show_page(self.initial_page)