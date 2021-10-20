# Import necessary modules
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def get_topic():
    # Url of the website
    url = "https://github.com/topics"
    response = requests.get(url)

    # Check if website is up and running
    if (response.status_code != 200):
        return pd.DataFrame([])
    else:
        # Get content of the website
        content = response.text
        soup = bs(content, "html.parser")

        # Get values of all block i.e. article tag
        block = soup.find_all("div", {"class": "py-4 border-bottom"})

        # Create list of different details
        title_list = []
        description_list = []

        # Iterate through each block of div tag
        for i in range(len(block)):
            # Get the values title text that is in p tag
            title = block[i].find_all("p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"})[0].text
            # Remove extra spaceses from the text values
            title = title.strip().replace(" ", "")
            # Append the values of title
            title_list.append(title)

            # Get the values description that is in p tag
            description = block[i].find_all("p", {"class": "f5 color-text-secondary mb-0 mt-1"})
            # Check if description available
            if (description):
                description = description[0].text.replace("\n", "").strip()
                description_list.append(description)
            else:
                description.append(np.nan)

        # Create dict of trend values
        topic_dict = {
            "Title": title_list,
            "Description": description_list
        }

        # Create dataframe of trend values
        topic_df = pd.DataFrame(topic_dict)
        # Create CSV of the dataframe
        topic_df.to_csv("Featured Topic on GitHub.csv")
        return topic_df
