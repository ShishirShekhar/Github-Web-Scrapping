# Import necessary modules
import numpy as np
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
lang = []
star = []
fork = []

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

    # Get the values language that is in span tag
    lang_list = block[i].find_all("span", {"itemprop": "programmingLanguage"})
    # Check if lang_list available
    if (lang_list):
        lang.append(lang_list[0].text)
    else:
        lang.append(np.nan)

    # Get the values star that is in a tag
    star_list = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
    # Check if star_list available
    if (star_list):
        # Remove extra spaceses from the text values
        star.append(star_list[0].text.strip())
    else:
        star.append(np.nan)

    # Get the values fork that is in a tag
    fork_list = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
    # Check if star_list available
    if (fork_list):
        # Remove extra spaceses from the text values
        fork.append(fork_list[1].text.strip())
    else:
        fork.append(np.nan)



# Print details of the treding repos
print("\n")
print("Details of Trending Repos")
print("*" * 50)
for i in range(len(author)):
    print("Author   ==>", author[i])
    print("Repo     ==>", repo[i])
    print("Language ==>", lang[i])
    print("Star     ==>", star[i])
    print("Fork     ==>", fork[i])
    print("-" * 50)
    print("\n")