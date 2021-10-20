# Import necessary modules
from trending_repo import get_trend
from featured_topics import get_topic


if __name__ == "__main__":
    # Get the treding dataframe
    trend_df = get_trend()
    print(trend_df.head())

    # Get the featured topics dataframe
    topic_df = get_topic()
    print(topic_df.head())
