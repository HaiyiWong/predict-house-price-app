import tkinter as tk
import customtkinter as ctk
import os
import pickle
from PIL import Image
import numpy as np

class Page3(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None
  buttonContinue : ctk.CTkButton = None
  EntryBedNum = None
  EntryBathNum = None
  EntryHouseSize = None
  EntryAcreSize = None
  EntryZipCode = None

  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############
  def predict_model(self, input_data):
    print("Predicting...")
    
    # Load the trained model
    with open('trained_model.pkl', 'rb') as f:
        print("Loading model...")
        model = pickle.load(f)
    print("Model loaded.")

    # Load the selected headers
    with open('selected_headers.pkl', 'rb') as f:
        print("Loading headers...")
        selected_headers = pickle.load(f)
    print("Headers loaded.")

    # Create the input array for prediction
    input_array = []
    for header in selected_headers:
        if header in input_data:
            input_array.append(input_data[header])
        else:
            raise KeyError(f"Missing required input: {header}")

    # Make a prediction using the loaded model
    print("Making prediction...")
    pred = model.predict(np.array(input_array).reshape(1, -1))[0]
    print("Prediction made.")

    # Return the predicted price
    return pred



  def predict_button_function(self):
        # Collect user inputs
    bath_str = self.EntryBathNum.get()
    bed_str = self.EntryBedNum.get()
    house_size_str = self.EntryHouseSize.get()
    acre_lot_str = self.EntryAcreSize.get()
    zip_code_str = self.EntryZipCode.get()

    # Check if any inputs are missing
    if not bath_str or not bed_str or not house_size_str or not acre_lot_str or not zip_code_str:
        self.predicted_price_label.configure(text="All inputs must be provided.", fg="red")
        return

    try:
        # Convert inputs to integers
        bath = int(bath_str)
        bed = int(bed_str)
        house_size = int(house_size_str)
        acre_lot = int(acre_lot_str)
        zip_code = int(zip_code_str)
    except ValueError:
        self.predicted_price_label.configure(text="All inputs must be integers.", fg="red")
        return

    # Create the input data dictionary
    input_data = {
        'bath': bath,
        'bed': bed,
        'house_size': house_size,
        'acre_lot': acre_lot,
        'zip_code': zip_code
    }

    try:
        # Predict the price using the input data
        predicted_price = self.predict_model(input_data)

        # Display the predicted price to the user
        self.predicted_price_label.configure(text=f"Predicted Price: {predicted_price}", fg="green")
    except Exception as e:
        self.predicted_price_label.configure(text=f"An error occurred: {str(e)}", fg="red")

  def load_model(self):
         # Open a file dialog and get the selected file path
    selected_model_file = ctk.filedialog.askopenfile(title="Open Model", filetypes=(("Pickle files", "*.pkl"), ("All files", "*.*")))
    # Check if a file was selected
    if selected_model_file is not None:
        self.model_filepath = selected_model_file.name
        # Try to read the model file
        try:
            with open(self.model_filepath, 'rb') as f:
                self.model = pickle.load(f)
            self.training_complete = True
            print("Model loaded successfully.")
        except Exception:
            print("The selected file is not a valid model file.")


   


# Load Model button





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
    self.logo = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")),size = (120,80))

    # Backgroud
    self.backgroud = ctk.CTkLabel(self,text="", image=self.background)
    self.backgroud.place(x=0, y=0, relwidth=1, relheight=1) 
    
    # Title label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Predict House Price", font = SECONDTITLE,fg_color="#FFF4ED",text_color="#D0A37C")
    self.labelTitle1.place(relx=0.5, rely=0.07, anchor=tk.CENTER)


    # Label for logo
    self.logo = ctk.CTkLabel(self,text="", image=self.logo)
    self.logo.place(relx=0.7, rely=0.15, anchor=tk.CENTER)

    # Button for load model
    self.buttonLoadModel = ctk.CTkButton(master=self, text="Load Model", command=self.load_model)
    self.buttonLoadModel.place(relx=0.3, rely=0.15, anchor=tk.CENTER)

    # Entry bedroom number
    self.bedNum = ctk.CTkLabel(master=self, text="Bedroom Number", font = NORMALFONT,fg_color="#FFF4ED",text_color="#7C6166")
    self.bedNum.place(relx=0.3, rely=0.25, anchor=tk.CENTER)

    self.EntryBedNum = ctk.CTkEntry(self, placeholder_text="")
    self.EntryBedNum.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

    # Entry bathroom number
    self.bathNum = ctk.CTkLabel(master=self, text="Bathroom Number", font = NORMALFONT,fg_color="#FFF4ED",text_color="#7C6166")
    self.bathNum.place(relx=0.7, rely=0.25, anchor=tk.CENTER)

    self.EntryBathNum = ctk.CTkEntry(self, placeholder_text="")
    self.EntryBathNum.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    # Entry house size
    self.houseSize = ctk.CTkLabel(master=self, text="House Size", font = NORMALFONT,fg_color="#FFF4ED",text_color="#7C6166")
    self.houseSize.place(relx=0.3, rely=0.35, anchor=tk.CENTER)

    self.EntryHouseSize = ctk.CTkEntry(self, placeholder_text="")
    self.EntryHouseSize.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

    # Entry acre size
    self.acreSize = ctk.CTkLabel(master=self, text="Acre Size", font = NORMALFONT,fg_color="#FFF4ED",text_color="#7C6166")
    self.acreSize.place(relx=0.7, rely=0.35, anchor=tk.CENTER)

    self.EntryAcreSize = ctk.CTkEntry(self, placeholder_text="")
    self.EntryAcreSize.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    # Entry zipcode
    self.zipCode = ctk.CTkLabel(master=self, text="Zip Code", font = NORMALFONT,fg_color="#FFF4ED",text_color="#7C6166")
    self.zipCode.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    self.EntryZipCode = ctk.CTkEntry(self, placeholder_text="")
    self.EntryZipCode.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Button back
    self.buttonBack = ctk.CTkButton(self, text="Back", width=100, command=lambda : app.show_page(2))
    self.buttonBack.place(relx=0.33, rely=0.6, anchor=tk.CENTER)

    # Button predict
    self.buttonPredict = ctk.CTkButton(self, text="Predict", width=100, command=lambda : self.predict_button_function())
    self.buttonPredict.place(relx=0.66, rely=0.6, anchor=tk.CENTER)

    self.predicted_price_label = tk.Label(self,text="", fg="#7C6166")
    self.predicted_price_label.place(relx=0.5,rely=0.65,anchor=tk.CENTER)
  

 

