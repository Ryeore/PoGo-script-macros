
import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://pokemongo.gishan.net/friends/codes/"  # Replace with the URL of the website you want to scrape
lista = []
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <strong> tags
strong_tags = soup.find_all("strong")

# Extract the text within the <strong> tags
strong_text = [tag.get_text() for tag in strong_tags]

# Print the extracted text
for text in strong_text:
    text = text.replace(" ", "")
    if text == "Thereareongoingraids!":
        print("header skip")
    else:
        lista.append(text)

print(lista)