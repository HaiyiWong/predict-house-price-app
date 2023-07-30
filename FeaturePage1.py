import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
import pandas as pd






class Page2(tk.Frame):

 
  ##############
  # COMPONENTS #
  ##############
  backgroud : ctk.CTkLabel = None
  labelTitle1 : ctk.CTkLabel = None
  buttonTrain : ctk.CTkButton = None
  errorMessage : ctk.CTkLabel = None
  buttonBack : ctk.CTkButton = None
  buttonContinue : ctk.CTkButton = None

  ###################
  # STATE VARIABLES #
  ###################
  training_complete: bool = False
  #############
  # FUNCTIONS #
  #############
  def proceed(self):
    if self.training_complete:
      self.app.show_page(3)
    else:
          # If the training is not complete, show an error message
      self.errorMessage.configure(text="Please complete the training before proceeding.")



  def train_model(self, selected_headers):
    # Use self.app.selectedFilePath as the dataset filepath
    dataset_filepath = self.app.selectedFilePath
    
    # Load your dataset
    dataset = pd.read_csv(dataset_filepath)

    # Filter the dataset with the selected headers and target variable
    X = dataset[selected_headers]
    y = dataset['price']  # Replace 'target_variable' with the name of your target column

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Linear Regression model
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    # Calculate the training performance
    y_pred = model.predict(X_test)
  
    # Save the trained model for later use
    with open('trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    # Save the selected headers for later use
    with open('selected_headers.pkl', 'wb') as f:
        pickle.dump(selected_headers, f)
    # Update the training status
    self.training_complete = True
    # Return the training performance
    return model, X_test, y_test, y_pred
  
  def train_selected_model(self):
        # Get the selected columns based on the state of the switches
    selected_columns = [self.switch_to_column[switch] for switch in self.scrollableFrameSwitches if switch.get()]

    # Train the model with the selected columns and get the return values
    model, X_test, y_test, y_pred = self.train_model(selected_columns)

    # Calculate the R-Squared
    r2 = r2_score(y_test, y_pred)
    # Save the model after training
 
    # Update the labels with the R-Squared and MSE
    self.labelPerformance.configure(text=f"R-Squared: {r2:.2f}",fg_color="#FFF4ED")

    # Print the result
    print({'message': 'Training successful!', 'r2': r2})





  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.switch_to_column = {}
    

    self.app = app
    
    SECONDTITLE = app.styles.get("SECONDTITLE")

    # Image
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
    self.background = ctk.CTkImage(Image.open(os.path.join(image_path, "Background.png")),size=(3900, 7400))
    # Backgroud
    self.backgroud = ctk.CTkLabel(self,text="", image=self.background)
    self.backgroud.place(x=0, y=0, relwidth=1, relheight=1) 



    # Label
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Select fields for Training", font = SECONDTITLE,fg_color="#FFF4ED",text_color="#D0A37C")
    self.labelTitle1.place(relx=0.5, rely=0.07, anchor=tk.CENTER)
    
    # Create the scrollable frame
    dataset = pd.read_csv('house_zipcode_usa .csv')
    column_names = dataset.columns.tolist()

    self.scrollableFrame = ctk.CTkScrollableFrame(self, label_text="Training Columns")
    self.scrollableFrame.place(relx=0.2, rely=0.2)

    #  Create a switch for each column in the dataset
    self.scrollableFrameSwitches = []
    for i, column in enumerate(column_names): 
     switch = ctk.CTkSwitch(master=self.scrollableFrame,text=column)
     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
     self.switch_to_column[switch] = column
     self.scrollableFrameSwitches.append(switch)


    self.labelPerformance = ctk.CTkLabel(master=self, text="")
    self.labelPerformance.place(relx=0.33, rely=0.65, anchor=tk.CENTER)

    
    # Button to check training success
    self.buttonTrain = ctk.CTkButton(master=self, text="Train", command=self.train_selected_model)
    self.buttonTrain.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    
    # Button to go back
    self.buttonBack = ctk.CTkButton(master=self, text="Back", width=100,command= lambda : app.show_page(1))
    self.buttonBack.place(relx=0.33, rely=0.7, anchor=tk.CENTER)

    # Button to continue
    self.buttonContinue = ctk.CTkButton(master=self, text="Continue",width=100,command= lambda : self.proceed())
    self.buttonContinue.place(relx=0.66, rely=0.7, anchor=tk.CENTER)
    
    # Label under the continue button
    self.errorMessage = tk.Label(master=self, text="", fg="red")
    self.errorMessage.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    
