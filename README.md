# Example of a multi-page application made with TKInter
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/8bc50621-f5ee-4cfc-be0b-5264630ac308)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/33713e78-1281-460a-8093-82b84c87aeeb)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/1ace94a0-a052-45bd-87fe-daa0bd9954c6)
![image](https://github.com/HaiyiWong/predict-house-price-app/assets/71823759/742e835d-72bb-44d5-aa4f-7df8eff13e98)



## Requirements

- Install tkinter
- Install customtkinter

### On MacOS

```brew install python-tk```

```pip3 install customtkinter```

### On Ubuntu

```sudo apt update```

```sudo apt install python3-tk```

```pip3 install customtkinter```

## WSL

If not working with WSL, go to the folder where the `main.py` file is, run `powershell.exe` and then `python main.py` to start the python application from Windows side.

# Other Development Tasks

## Adding a New Page

1. Create file PageNUMBER.py (you can just copy content of any old page)
2. In `App.py`, import the page on top after other pages
3. In `App.py` add the page into the member variable pages
