#!/usr/bin/python3
"""
    A module that queries the Reddit API and prints the titles
"""
import requests


def number_of_subscribers(subreddit):
    """
        A function that queries the reddit API and returns the number of
        subscribers
    """

    url = 'https://api.reddit.com/r/{}/about/.json'.format(subreddit)

    user_agent = {'User-Agent': 'D_AzilAdvancedAPI/1.0 (by /u/Daniel_Azil)'}

    response = requests.get(url, headers=user_agent)

    if response.status_code != 200:
        print('None')
    else:
        top_ten = response.json()["data"]["children"]

        limit = 0

        for post in top_ten:
            print(post["data"]["title"])
            limit += 1
            if limit == 10:
                break
