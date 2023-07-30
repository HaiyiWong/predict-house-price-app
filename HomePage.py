import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
import pandas as pd
import sqlite3



class Page1(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  backgroud : ctk.CTkLabel = None
  samplePicture : ctk.CTkLabel = None
  labelTitle1 : ctk.CTkLabel = None
  labelTitleDescription : ctk.CTkLabel = None
  labelSelectedFile : ctk.CTkLabel = None
  buttonSelectFile : ctk.CTkButton = None
  buttonContinue : ctk.CTkButton = None
  labelContinue : ctk.CTkLabel = None
  navigation_frame : ctk.CTkFrame = None
  home_button : ctk.CTkButton = None
  About_us_button : ctk.CTkButton = None
  home_frame : ctk.CTkFrame = None
  buttonSelectDatabase : ctk.CTkButton = None
  url_entry : ctk.CTkEntry = None
  url_button : ctk.CTkButton = None


  #############
  # FUNCTIONS #
  #############

  def selectFile(self):
    # Open a file dialog and get the selected file path
    selected_file = ctk.filedialog.askopenfile(title="Open File", filetypes=(("Open a .csv file", "*.csv"), ("All files", "*.*")))
    # Check if a file was selected
    if selected_file is not None:
        self.app.selectedFilePath = selected_file.name
        # Update text for a label
        self.labelSelectedFile.configure(text=f"We have selected a file: {self.app.selectedFilePath}",fg_color="#FFF4ED")
        # Try to read the CSV file
        try:
            dataset = pd.read_csv(self.app.selectedFilePath)
            self.app.columnNames = dataset.columns.tolist()
            # No exception occurred, so the CSV file was read successfully
            # Now we can clear the error message
            self.error_message.configure(text="")
        except Exception:
            # If an error occurs while reading, it is not a valid CSV
            self.error_message.configure(text="The selected file is not a valid CSV file.")


  def proceed(self):
        # Check if a file has been selected
    if self.app.selectedFilePath is None:
        # If no file is selected, show an error message
        self.error_message.configure(text="Please select a valid CSV file before proceeding.")
    else:
        try:
            # Try to read the CSV file
            pd.read_csv(self.app.selectedFilePath)
            # If it is a valid CSV, remove the error message and proceed to the next page
            self.error_message.configure(text="")
            self.app.show_page(2)
        except Exception:
            # If an error occurs while reading, it is not a valid CSV
            self.error_message.configure(text="Please select a valid CSV file before proceeding.")

  def selectDatabase(self):
        # Open a file dialog and get the selected file path
        selected_database_file = ctk.filedialog.askopenfile(title="Open Database", filetypes=(("SQLite files", "*.db"), ("All files", "*.*")))
        # Check if a file was selected
        if selected_database_file is not None:
            self.app.selectedDatabasePath = selected_database_file.name
            # Update text for a label
            self.labelSelectedFile.configure(text=f"Selected database: {self.app.selectedDatabasePath}", fg_color="#FFF4ED")
            # Try to read the database
            try:
                conn = sqlite3.connect(self.app.selectedDatabasePath)
                self.app.dataset = pd.read_sql_query("SELECT * FROM house_zipcode_usa", conn)
                # Replace 'your_table_name' with the name of your table
                self.app.columnNames = self.app.dataset.columns.tolist()
                # No exception occurred, so the database was read successfully
                # Now we can clear the error message
                self.error_message.configure(text="")
            except Exception as e:
                # If an error occurs while reading, it is not a valid SQLite database
                self.error_message.configure(text="Error: " + str(e))
  
  def selectURL(self):
        # Get the URL from the user input
    url = self.url_entry.get()

    # Try to load the data from the URL
    try:
        self.app.dataset = pd.read_csv(url)
        self.app.columnNames = self.app.dataset.columns.tolist()

        # If the data loaded successfully, clear any error messages
        self.error_message.configure(text="")
    except Exception as e:
        # If an error occurred, display an error message
        self.error_message.configure(text=f"Error loading data: {e}")


  def aboutUs(self):
    self.app.show_page(4)




  #######################
  # INITIALIZE THE PAGE #
  #######################
  
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    MIDDLEFONT = app.styles.get("MIDDLEFONT")
    TITLE = app.styles.get("TITLE")

       
    # Image
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
    self.background = ctk.CTkImage(Image.open(os.path.join(image_path, "Background.png")),size=(3900, 7400))
    self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
    self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
    self.sample1 = ctk.CTkImage(Image.open(os.path.join(image_path, "sample1.png")),size = (400,400))

    # Backgroud
    self.backgroud = ctk.CTkLabel(self,text="", image=self.background)
    self.backgroud.place(x=0, y=0, relwidth=1, relheight=1)   
    # sample Image
    self.samplePicture = ctk.CTkLabel(self,text="", image=self.sample1)
    self.samplePicture.place(relx=0.5, rely=0.73, anchor=tk.CENTER)



    # Label for title
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Spruce House", font = TITLE,fg_color="#FFF4ED",text_color="#7C6166")
    self.labelTitle1.place(relx=0.4, rely=0.15, anchor=tk.CENTER)
    
    # Label for description
    self.labelTitleDescription = ctk.CTkLabel(master=self, font = NORMALFONT, text="Smarter Real Estate Decisions",fg_color="#FFF4ED",text_color="#D0A37C")
    self.labelTitleDescription.place(relx=0.31, rely=0.22, anchor=tk.CENTER)

    # Label for selected file
    self.labelSelectedFile = ctk.CTkLabel(master=self, text = "", font = NORMALFONT,bg_color="#FFF4ED",text_color="#D0A37C")
    self.labelSelectedFile.place(relx=0.5, rely=0.35, anchor=tk.CENTER)


    # Button to select a file, calls the selectFile function inside this class
    self.buttonSelectFile = ctk.CTkButton(master=self, text="Select File",bg_color="#FFF4ED", command = lambda : self.selectFile())
    self.buttonSelectFile.place(relx=0.5, rely=0.3,anchor=tk.CENTER)

    self.labelContinue = ctk.CTkLabel(master=self, text="Predict Your House Now!", font = MIDDLEFONT,fg_color="#3B8ED0",text_color="white")
    self.labelContinue.place(relx=0.4, rely=0.8, anchor=tk.CENTER)

    # Button to continue to the next page, calls the proceed function inside this class
    self.buttonContinue = ctk.CTkButton(master=self, width=40, text="→", command= lambda : self.proceed())
    self.buttonContinue.place(relx=0.85, rely=0.8, anchor=tk.CENTER)
 

    # create navigation frame
    self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
    self.navigation_frame.grid(row=0, column=0, sticky="nsew")
    self.navigation_frame.grid_rowconfigure(4, weight=1)

    # Home Button
    self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                               fg_color="transparent", text_color=("gray10"), hover_color=("gray70", "gray30"),
                                               image=self.home_image, anchor="w")
    self.home_button.grid(row=1, column=1, sticky="w")

    #About us Button
    self.About_us_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About Us",
                                                      fg_color="transparent", text_color=("gray40"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",command= lambda : self.aboutUs())
    self.About_us_button.grid(row=1, column=2, sticky="ew")

    self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.home_frame.grid_columnconfigure(0, weight=1)

    #Error message
    self.error_message = tk.Label(master=self, text="",fg="red")
    self.error_message.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    #Loading the CSV data from a sqlite3 database
    self.buttonSelectDatabase = ctk.CTkButton(master=self, text="Select Database", width=100, command=self.selectDatabase)
    self.buttonSelectDatabase.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    #Loading the CSV data from URL
    self.url_entry = ctk.CTkEntry(self,width=340)
    self.url_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    self.url_button = ctk.CTkButton(self, text="Load data from URL", command=self.selectURL)
    self.url_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
