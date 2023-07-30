# House Price Prediction Software
This application is designed to provide users with an intuitive way to predict house prices based on various features.

Built with Python, the app employs a range of libraries and technologies to deliver a sleek, easy-to-use GUI experience. These libraries include Tkinter and CustomTkinter for the interface, pandas for data manipulation, and scikit-learn for machine learning tasks.

## Installation
To install the application, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/house-price-prediction-app.git
```

Navigate to the cloned repository:
```bash
cd house-price-prediction-app

```
## Running the Application
Once you have installed the necessary libraries and cloned the repository, you can run the application using Python:
```bash
python main.py
```
## The application consists of four main pages:

HomePage: This is the starting point of the application. Here, users can choose to load their dataset from a local CSV file, an SQLite database, or a URL. They can also navigate to the "About Us" page for additional information about the app.

FeaturePage1: In this section, users can select the features they wish to use for training the model. This is achieved through a series of switch widgets, each corresponding to a different column in the user's dataset.

FeaturePage2: On this page, users can train a Random Forest Regressor model on their selected features. The performance of the trained model, measured by the R-squared score, is displayed once the training is complete.

AboutUsPage: Here, users can find information about the development of the application and its intended purpose.

To use the application, simply navigate through the pages using the 'Back' and 'Continue' buttons, select your desired features, and initiate the model training. Once your model is trained, you can use it to make predictions about house prices based on your input data.

We hope this application will serve as a valuable tool for all your house price prediction needs. Enjoy exploring and using the House Price Prediction App!

## Requirements

- Install tkinter
```bash
python -m tkinter
```
- Install customtkinter
 ```bash
  pip nstall customtkinter
```
- Install os
   
- Install pandas
```bash
pip install pandas
```
- Install scikit-learn
```bash
pip install scikit-learn
```
- Install numpy
```bash
pip install numpy
```
## Software Screenhots
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/8bc50621-f5ee-4cfc-be0b-5264630ac308)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/33713e78-1281-460a-8093-82b84c87aeeb)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/1ace94a0-a052-45bd-87fe-daa0bd9954c6)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/742e835d-72bb-44d5-aa4f-7df8eff13e98)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


