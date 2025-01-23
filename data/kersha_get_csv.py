import requests

def fetch_csv():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    response = requests.get(url)
    if response.status_code == 200:
        with open("data/sample.csv", "wb") as file:
            file.write(response.content)
        print("CSV file fetched and saved as data/sample.csv.")
    else:
        print("Failed to fetch CSV file.")

if __name__ == "__main__":
    fetch_csv()
