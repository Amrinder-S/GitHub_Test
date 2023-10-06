import json

# Function to load existing JSON data from the file
def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Function to add a new entry to the JSON data
def add_entry(data):
    name = input("Enter name: ")
    crn = input("Enter CRN: ")
    gender = input("Enter gender (m/f): ").lower()

    new_entry = {
        "name": name,
        "CRN": crn,
        "gender": gender
    }

    data.append(new_entry)

# Function to save JSON data to the file
def save_json_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    filename = "data.json"
    data = load_json_data(filename)

    add_entry(data)

    save_json_data(filename, data)

if __name__ == "__main__":
    main()
