import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os
from PIL import Image

class Page4(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None
  labelTitle2 : ctk.CTkLabel = None
  buttonContinue : ctk.CTkButton = None
  sliderLabel : ctk.CTkLabel = None
  slider : ctk.CTkSlider = None
  switch : ctk.CTkSwitch = None

  ###################
  # STATE VARIABLES #
  ###################

  # For controlling / containing the switch state
  switch_var = None

  #############
  # FUNCTIONS #
  #############


  def process(self):
    self.app.show_page(1)

  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    SECONDTITLE = app.styles.get("SECONDTITLE")

    # Image
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
    self.background = ctk.CTkImage(Image.open(os.path.join(image_path, "Background.png")),size=(3900, 7400))
    self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
    self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
    self.logo = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")),size = (120,80))
    self.page4image1 = ctk.CTkImage(Image.open(os.path.join(image_path, "page4image1.png")),size = (120,120))
    self.page4image2 = ctk.CTkImage(Image.open(os.path.join(image_path, "page4image2.png")),size = (180,120))

    # Backgroud
    self.backgroud = ctk.CTkLabel(self,text="", image=self.background)
    self.backgroud.place(x=0, y=0, relwidth=1, relheight=1)

    # Home Button
    self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
    self.navigation_frame.grid(row=0, column=0, sticky="nsew")
    self.navigation_frame.grid_rowconfigure(4, weight=1)

    self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                               fg_color="transparent", text_color=("gray40"), hover_color=("gray70", "gray30"),
                                               image=self.home_image, anchor="w", command=lambda : self.process())
    self.home_button.grid(row=1, column=1, sticky="w")

    #About us Button
    self.About_us_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About Us",
                                                      fg_color="transparent", text_color=("gray10"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w")
    self.About_us_button.grid(row=1, column=2, sticky="ew")

    self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.home_frame.grid_columnconfigure(0, weight=1)
    # Title label
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Welcome to Spruce House!", font = SECONDTITLE,fg_color="#FFF4ED",text_color="#D0A37C")
    self.labelTitle1.place(relx=0.45, rely=0.1, anchor=tk.CENTER)

    # Label for description1
    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="Our House Price Prediction service provides",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.4, rely=0.3, anchor=tk.CENTER)

    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="valuable reference information regardless of",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.4, rely=0.36, anchor=tk.CENTER)

    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="whether you are a buyer or seller.",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.31, rely=0.42, anchor=tk.CENTER)
    
    # Label for logo
    self.logo = ctk.CTkLabel(self,text="", image=self.logo)
    self.logo.place(relx=0.8, rely=0.20, anchor=tk.CENTER)

    # Label for page4image1
    self.page4image1 = ctk.CTkLabel(self,text="", image=self.page4image1)
    self.page4image1.place(relx=0.2, rely=0.55, anchor=tk.CENTER)

    # Label for page4image2
    self.page4image2 = ctk.CTkLabel(self,text="", image=self.page4image2)
    self.page4image2.place(relx=0.7, rely=0.55, anchor=tk.CENTER)

    # Label for description2
    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="We use state-of-the-art machine learning algorithms",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.45, rely=0.74, anchor=tk.CENTER)

    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="and advanced data analysis techniques to deliver",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.42, rely=0.8, anchor=tk.CENTER)

    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="accurate predictions for your home.",fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitleDescription.place(relx=0.31, rely=0.86, anchor=tk.CENTER)
