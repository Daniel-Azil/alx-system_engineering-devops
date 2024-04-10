#!/usr/bin/python3
"""
    A module that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
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
        return 0
    else:
        return response.json().get('data', {}).get('subscribers')
