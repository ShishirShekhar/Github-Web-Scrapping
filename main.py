# Import necessary modules
import requests
from bs4 import BeautifulSoup as bs


# Url of the website
url = "https://github.com/trending"
response = requests.get(url)

# Check if website is up and running
if (response.status_code != 200):
    print("Error!")

# Get content of the website
content = response.text
soup = bs(content, "html.parser")

# Get values of all block i.e. article tag
block = soup.find_all("article", {"class": "Box-row"})

# Create list of different details
author = []
repo = []

# Iterate through each block of article tag
for i in range(len(block)):
    # Get the values title text that is in h1 tag
    title = block[i].find_all("h1", {"class": "h3 lh-condensed"})[0].text
    # Remove extra spaceses from the text values
    title = title.strip().replace(" ", "")
    # Split on the basis of /
    value_list = title.split("/")
    # Append the values of author and repo
    author.append(value_list[0])
    repo.append(value_list[1][2:])

# Print author and repo
for i in range(len(author)):
    print(author[i], "==>", repo[i])
    print("-"*50)