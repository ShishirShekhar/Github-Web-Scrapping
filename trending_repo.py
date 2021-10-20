# Import necessary modules
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_trend():
    # Url of the website
    url = "https://github.com/trending"
    response = requests.get(url)

    # Check if website is up and running
    if (response.status_code != 200):
        return pd.DataFrame([])
    else:
        # Get content of the website
        content = response.text
        soup = bs(content, "html.parser")

        # Get values of all block i.e. article tag
        block = soup.find_all("article", {"class": "Box-row"})

        # Create list of different details
        author_list = []
        repository_list = []
        language_list = []
        star_list = []
        fork_list = []

        # Iterate through each block of article tag
        for i in range(len(block)):
            # Get the values title text that is in h1 tag
            title = block[i].find_all("h1", {"class": "h3 lh-condensed"})[0].text
            # Remove extra spaceses from the text values
            title = title.strip().replace(" ", "")
            # Split on the basis of /
            value_list = title.split("/")
            # Append the values of author and repo
            author_list.append(value_list[0])
            repository_list.append(value_list[1][2:])

            # Get the values language that is in span tag
            language = block[i].find_all("span", {"itemprop": "programmingLanguage"})
            # Check if language available
            if (language):
                language_list.append(language[0].text)
            else:
                language_list.append(np.nan)

            # Get the values star that is in a tag
            star = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
            # Check if star_list available
            if (star):
                # Remove extra spaceses from the text values
                star_list.append(star[0].text.strip())
            else:
                star_list.append(np.nan)

            # Get the values fork that is in a tag
            fork = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
            # Check if star_list available
            if (fork):
                # Remove extra spaceses from the text values
                fork_list.append(fork[1].text.strip())
            else:
                fork_list.append(np.nan)

        # Create dict of trend values
        trend_dict = {
            "Author": author_list,
            "Repository": repository_list,
            "Language": language_list,
            "Star": star_list,
            "Fork": fork_list
        }

        # Create dataframe of trend values
        trend_df = pd.DataFrame(trend_dict)
        # Create CSV of the dataframe
        trend_df.to_csv("Treding Repos on GitHub.csv")
        return trend_df
