# === List comprehensions for time-stamped data ===

# import file directory
import os
# get information about current directory
print(os.getcwd())
# open directory in which the data is stored
os.chdir(r'D:\Data Science\Data Camp\Python Data Science Toolbox 1')
# import pandas
import pandas as pd
# import twitter DataFrame: tweets_df
tweets_df = pd.read_csv('tweets.csv')
# extract the created_at column from df: tweet_time
tweet_time = tweets_df['created_at']
# extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]
# print the extracted times
print(tweet_clock_time)

# === Conditional list comprehensions for time-stamped data ===

# extract the created_at column from df: tweet_time
tweet_time = tweets_df['created_at']
# extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
# print the extracted times
print(tweet_clock_time)
