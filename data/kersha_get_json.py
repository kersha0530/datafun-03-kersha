import requests

def fetch_json():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        with open("data/sample.json", "w") as file:
            file.write(response.text)
        print("JSON file fetched and saved as data/sample.json.")
    else:
        print("Failed to fetch JSON file.")

if __name__ == "__main__":
    fetch_json()
