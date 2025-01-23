import requests

def fetch_text():
    url = "http://www.gutenberg.org/cache/epub/100/pg100.txt"
    response = requests.get(url)
    if response.status_code == 200:
        with open("data/sample.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Text file fetched and saved as data/sample.txt.")
    else:
        print("Failed to fetch text file.")

if __name__ == "__main__":
    fetch_text()
