import json

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Successfully loaded JSON data from '{path}'.")
            return data
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{path}' is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")