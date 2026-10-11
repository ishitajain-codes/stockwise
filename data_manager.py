import json

def save_data(data):
    try :
        with open("portfolio.json", "w") as file:
            json.dump(data,file,indent=4)
    except OSError:
       print("Error: Unable to save portfolio data.")

def load_data():
    try:
        with open("portfolio.json" , "r") as file:
            data=json.load(file)
            return data
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
       return[]