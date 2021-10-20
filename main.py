# Import necessary modules
from trending_repo import get_trend


# Get the treding dataframe
trend_df = get_trend()
print(trend_df.head())
